import uvicorn
from timvt.db import close_db_connection, connect_to_db
from timvt.factory import VectorTilerFactory
from timvt.layer import FunctionRegistry
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8001",
]

# enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Function registry to the application state
app.state.function_catalog = FunctionRegistry()

# Register Start/Stop application event handler to setup/stop the database connection
# and populate `app.state.table_catalog`
@app.on_event("startup")
async def startup_event():
    """Application startup: register the database connection and create table list."""
    await connect_to_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    """Application shutdown: de-register the database connection."""
    await close_db_connection(app)


# Register endpoints.
mvt_tiler = VectorTilerFactory(
    with_tables_metadata=True,
    with_functions_metadata=True,  # add Functions metadata endpoints (/functions.json, /{function_name}.json)
    with_viewer=True,
)
app.include_router(mvt_tiler.router, tags=["Tiles"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", debug=True)
