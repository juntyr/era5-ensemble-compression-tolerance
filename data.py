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
    month_ranges = ["01_02", "03_04"] # , "05_06", "07_08", "09_10", "11_12"

    ds_mean_list = []
    ds_spread_list = []

    for months in month_ranges:
        ds_depth_mean = xr.open_dataset(data / subfolder / f"data_months{months}_0.nc", chunks={})
        ds_depth_spread = xr.open_dataset(data / subfolder / f"data_months{months}_1.nc", chunks={})
        ds_height_mean = xr.open_dataset(data / subfolder / f"data_months{months}_2.nc", chunks={})
        ds_height_spread = xr.open_dataset(data / subfolder / f"data_months{months}_3.nc", chunks={})
        ds_sea_mean = xr.open_dataset(data / subfolder / f"data_months{months}_4.nc", chunks={})
        ds_sea_spread = xr.open_dataset(data / subfolder / f"data_months{months}_5.nc", chunks={})
        ds_surface_mean = xr.open_dataset(data / subfolder / f"data_months{months}_6.nc", chunks={})
        ds_surface_spread = xr.open_dataset(data / subfolder / f"data_months{months}_7.nc", chunks={})

        ds_single_mean = xr.Dataset({
            **ds_depth_mean,
            **ds_height_mean,
            **ds_sea_mean,
            **ds_surface_mean,
        })

        ds_single_spread = xr.Dataset({
            **ds_depth_spread,
            **ds_height_spread,
            **ds_sea_spread,
            **ds_surface_spread,
        })

        ds_mean_list.append(ds_single_mean)
        ds_spread_list.append(ds_single_spread)

    ds_single_mean = xr.concat(ds_mean_list, dim="valid_time")
    ds_single_spread = xr.concat(ds_spread_list, dim="valid_time")

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

