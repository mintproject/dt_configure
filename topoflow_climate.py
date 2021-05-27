import argparse
from typing import List
from string import Template
from utils import get_spec, write_to_yaml
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

def _generate_inputs(
    input_dir : str,
    temp_dir: str,
    output_file: str,
    var_name: str,
    bounding_box: List[float],
    xres_arcsecs: int,
    yres_arcsecs: int,
    dt_template_file: str,
    dt_output_file: str
):
    _data = locals()
    _spec = get_spec(Path(dt_template_file))
    for key, default_value in _spec['inputs'].items():
        if key in _data:
            new_value = _data[key]
            _spec['inputs'][key] = new_value
            logging.info(f"""Setting {key} in {new_value}""")

    write_to_yaml(dt_output_file, _spec)


def _main():
    parser = argparse.ArgumentParser(
        description="Data transformation to generate TopoFlow-ready precipitation files (RTS) from Global Precipitation Measurement (GPM) data sources"
    )
    parser.add_argument('--input-dir', type=str, required=True)
    parser.add_argument('--temp-dir', type=str, required=True)
    parser.add_argument('--output-file', type=str, required=True)
    parser.add_argument('--var-name', type=str, choices=['precipitation'], required=True)
    parser.add_argument('--bounding-box', type=float, nargs=4)
    parser.add_argument('--xres_arcsecs', type=int, required=True)
    parser.add_argument('--yres_arcsecs', type=int, required=True)
    parser.add_argument('--dt-output-file', type=str, default='topoflow_climate.yaml')
    parser.add_argument('--dt-template-file', type=str, default='./templates/topoflow_climate.yaml')
    args = parser.parse_args()

    _generate_inputs(**vars(args))
if __name__ == "__main__":
    _main()