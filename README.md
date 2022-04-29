# District Tiler Example

This is an FastAPI tile server utilizing the amazing [TiMVT](https://github.com/developmentseed/timvt) library.

Initially this is just their "Minimal Application" example but with CORS enabled, and it also includes a compose file for launching the latest default version of PostGIS. See [here](https://pithological.com/building-a-district-tile-server/) for more detail.

![District Tiler](https://pithological.com/content/images/2022/04/dynamic_tiling_network_panel-1.gif)
![District Tiler with Base Map](https://pithological.com/content/images/2022/04/map_with_base_layer.gif)

## Getting Started

Clone this project and set up a virtual environment for installing required packages.

### Prerequisites

- Python 3.6+
- python3-venv
- docker-compose (if using compose file for PostGIS)

### Installing

```bash
> python3 -m venv ./venv
> source ./venv/bin/activate
> pip install -r requirements.txt
```

### Running

- Copy the `.example.env` file to `.env` and fill out environmental variables
- Source the `.env` file
- `> docker-compose up` to launch PostGIS
- Load data into PostGIS
- `> python main.py`