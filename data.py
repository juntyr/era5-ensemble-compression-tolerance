__all__ = ["UncertainDataset", "ds_single", "ds_pressure"]

from dataclasses import dataclass
from pathlib import Path

data = Path("/ec/res4/scratch/ecm5945/era5-data")

import numpy as np
import xarray as xr

@dataclass
class UncertainDataset:
    mean: xr.Dataset
    spread: xr.Dataset


def _load_single_dataset() -> UncertainDataset:
    subfolder = "single_data"
    month_ranges = ["01_02", "03_04", "05_06", "07_08", "09_10", "11_12"]
    file_patterns = {
        "depth_mean": "data_months{0}_0.nc",
        "depth_spread": "data_months{0}_1.nc",
        "height_mean": "data_months{0}_2.nc",
        "height_spread": "data_months{0}_3.nc",
        "sea_mean": "data_months{0}_4.nc",
        "sea_spread": "data_months{0}_5.nc",
        "surface_mean": "data_months{0}_6.nc",
        "surface_spread": "data_months{0}_7.nc"
    }

    ds_single_mean_list, ds_single_spread_list = [], []
    for months in month_ranges:
        ds_single_mean = xr.open_mfdataset(
            [Path(data) / subfolder / file_patterns[var].format(months) for var in ["depth_mean", "height_mean", "sea_mean", "surface_mean"]],
            combine='by_coords', chunks={},compat='override')
        
        ds_single_spread = xr.open_mfdataset(
            [Path(data) / subfolder / file_patterns[var].format(months) for var in ["depth_spread", "height_spread", "sea_spread", "surface_spread"]],
            combine='by_coords', chunks={},compat='override')

        ds_single_mean_list.append(ds_single_mean)
        ds_single_spread_list.append(ds_single_spread)

    ds_single_mean = xr.concat(ds_single_mean_list, dim="valid_time")
    ds_single_spread = xr.concat(ds_single_spread_list, dim="valid_time")

    return UncertainDataset(mean=ds_single_mean, spread=ds_single_spread)


ds_single = _load_single_dataset()



def _load_pressure_dataset() -> UncertainDataset:
    subfolder = "pressure_data"
    pressure_levels = [50, 500, 850, 1000]
    
    ds_mean_list = []
    ds_spread_list = []

    for level in pressure_levels:
        ds_mean = xr.open_dataset(data / subfolder / f"data_{level}_0.nc", chunks={})
        ds_spread = xr.open_dataset(data / subfolder / f"data_{level}_1.nc", chunks={})

        ds_mean_list.append(ds_mean)
        ds_spread_list.append(ds_spread)

    ds_pressure_mean = xr.concat(ds_mean_list, dim="pressure_level")
    ds_pressure_spread = xr.concat(ds_spread_list, dim="pressure_level")

    return UncertainDataset(mean=ds_pressure_mean, spread=ds_pressure_spread)
    
ds_pressure = _load_pressure_dataset()

