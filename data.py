__all__ = ["UncertainDataset", "ds_single", "ds_pressure"]

from dataclasses import dataclass
from pathlib import Path

data = Path("/scratch/project_2008523/era5")

import numpy as np
import xarray as xr

@dataclass
class UncertainDataset:
    mean: xr.Dataset
    spread: xr.Dataset

def _load_single_dataset() -> UncertainDataset:
    ds_depth_below_land_layer_06_2023_mean = xr.open_dataset(data / "e589c4ae559b6f88ca6198b668ca58d5" / "data_0.nc", chunks={})
    ds_depth_below_land_layer_06_2023_spread = xr.open_dataset(data / "e589c4ae559b6f88ca6198b668ca58d5" / "data_1.nc", chunks={})
    ds_height_above_ground_06_2023_mean = xr.open_dataset(data / "e589c4ae559b6f88ca6198b668ca58d5" / "data_2.nc", chunks={})
    ds_height_above_ground_06_2023_spread = xr.open_dataset(data / "e589c4ae559b6f88ca6198b668ca58d5" / "data_3.nc", chunks={})
    ds_mean_sea_06_2023_mean = xr.open_dataset(data / "e589c4ae559b6f88ca6198b668ca58d5" / "data_4.nc", chunks={})
    ds_mean_sea_06_2023_spread = xr.open_dataset(data / "e589c4ae559b6f88ca6198b668ca58d5" / "data_5.nc", chunks={})
    ds_surface_06_2023_mean = xr.open_dataset(data / "e589c4ae559b6f88ca6198b668ca58d5" / "data_6.nc", chunks={})
    ds_surface_06_2023_spread = xr.open_dataset(data / "e589c4ae559b6f88ca6198b668ca58d5" / "data_7.nc", chunks={})
    
    ds_single_06_2023_mean = xr.Dataset({
        **ds_depth_below_land_layer_06_2023_mean,
        **ds_height_above_ground_06_2023_mean,
        **ds_mean_sea_06_2023_mean,
        **ds_surface_06_2023_mean,
    })
    ds_single_06_2023_spread = xr.Dataset({
        **ds_depth_below_land_layer_06_2023_spread,
        **ds_height_above_ground_06_2023_spread,
        **ds_mean_sea_06_2023_spread,
        **ds_surface_06_2023_spread,
    })
    
    ds_depth_below_land_layer_12_2023_mean = xr.open_dataset(data / "3e36e22482d4e90c2f7d18740c1ba838" / "data_0.nc", chunks={})
    ds_depth_below_land_layer_12_2023_spread = xr.open_dataset(data / "3e36e22482d4e90c2f7d18740c1ba838" / "data_1.nc", chunks={})
    ds_height_above_ground_12_2023_mean = xr.open_dataset(data / "3e36e22482d4e90c2f7d18740c1ba838" / "data_2.nc", chunks={})
    ds_height_above_ground_12_2023_spread = xr.open_dataset(data / "3e36e22482d4e90c2f7d18740c1ba838" / "data_3.nc", chunks={})
    ds_mean_sea_12_2023_mean = xr.open_dataset(data / "3e36e22482d4e90c2f7d18740c1ba838" / "data_4.nc", chunks={})
    ds_mean_sea_12_2023_spread = xr.open_dataset(data / "3e36e22482d4e90c2f7d18740c1ba838" / "data_5.nc", chunks={})
    ds_surface_12_2023_mean = xr.open_dataset(data / "3e36e22482d4e90c2f7d18740c1ba838" / "data_6.nc", chunks={})
    ds_surface_12_2023_spread = xr.open_dataset(data / "3e36e22482d4e90c2f7d18740c1ba838" / "data_7.nc", chunks={})
    
    ds_single_12_2023_mean = xr.Dataset({
        **ds_depth_below_land_layer_12_2023_mean,
        **ds_height_above_ground_12_2023_mean,
        **ds_mean_sea_12_2023_mean,
        **ds_surface_12_2023_mean,
    })
    ds_single_12_2023_spread = xr.Dataset({
        **ds_depth_below_land_layer_12_2023_spread,
        **ds_height_above_ground_12_2023_spread,
        **ds_mean_sea_12_2023_spread,
        **ds_surface_12_2023_spread,
    })
    
    ds_single_mean = xr.concat([ds_single_06_2023_mean, ds_single_12_2023_mean], dim="valid_time")
    ds_single_spread = xr.concat([ds_single_06_2023_spread, ds_single_12_2023_spread], dim="valid_time")

    return UncertainDataset(mean=ds_single_mean, spread=ds_single_spread)

ds_single = _load_single_dataset()

def _load_pressure_dataset() -> UncertainDataset:
    ds_pressure_50hPa_mean = xr.open_dataset(data / "7e1c0bd4d52e1ba86a2a118ae5f4c23" / "data_0.nc", chunks={})
    ds_pressure_50hPa_spread = xr.open_dataset(data / "7e1c0bd4d52e1ba86a2a118ae5f4c23" / "data_1.nc", chunks={})
    
    ds_pressure_500hPa_mean = xr.open_dataset(data / "c547d3206292f3f1b36230ee235468a8" / "data_0.nc", chunks={})
    ds_pressure_500hPa_spread = xr.open_dataset(data / "c547d3206292f3f1b36230ee235468a8" / "data_1.nc", chunks={})
    
    ds_pressure_850hPa_mean = xr.open_dataset(data / "e5ee4377910fa2e5532774b02401b268" / "data_0.nc", chunks={})
    ds_pressure_850hPa_spread = xr.open_dataset(data / "e5ee4377910fa2e5532774b02401b268" / "data_1.nc", chunks={})
    
    ds_pressure_1000hPa_mean = xr.open_dataset(data / "4a0d4aa0d64927f4a7e1d9994c7bc12e" / "data_0.nc", chunks={})
    ds_pressure_1000hPa_spread = xr.open_dataset(data / "4a0d4aa0d64927f4a7e1d9994c7bc12e" / "data_1.nc", chunks={})
    
    ds_pressure_mean = xr.concat([
        ds_pressure_50hPa_mean, ds_pressure_500hPa_mean, ds_pressure_850hPa_mean, ds_pressure_1000hPa_mean,
    ], dim="pressure_level")
    ds_pressure_spread = xr.concat([
        ds_pressure_50hPa_spread, ds_pressure_500hPa_spread, ds_pressure_850hPa_spread, ds_pressure_1000hPa_spread,
    ], dim="pressure_level")

    return UncertainDataset(mean=ds_pressure_mean, spread=ds_pressure_spread)

ds_pressure = _load_pressure_dataset()

