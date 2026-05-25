__all__ = ["UncertainDataset", "ds_single", "ds_pressure"]

from dataclasses import dataclass
from pathlib import Path

data = Path("data")

import numpy as np
import xarray as xr

@dataclass
class UncertainDataset:
    mean: xr.Dataset
    spread: xr.Dataset

def _load_single_dataset() -> UncertainDataset:
    dss_single_mean = []
    dss_single_spread = []
    
    for a, b in [("enda", "accum"), ("enda", "avg"), ("enda", "instant"), ("enda", "max"), ("ewda", "instant")]:
        dss_single_mean.append(xr.concat([
            xr.open_dataset(p, chunks={}) for p in sorted(data.glob(
                str(Path("reanalysis-era5-single-levels_ensemble_mean_*_*") / f"data_stream-{a}_stepType-{b}.nc")
            ))
        ], dim="valid_time").sortby("valid_time"))

        dss_single_spread.append(xr.concat([
            xr.open_dataset(p, chunks={}) for p in sorted(data.glob(
                str(Path("reanalysis-era5-single-levels_ensemble_spread_*_*") / f"data_stream-{a}_stepType-{b}.nc")
            ))
        ], dim="valid_time").sortby("valid_time"))
    
    ds_single_mean = xr.Dataset({ k: v for ds in dss_single_mean for k, v in ds.items() })
    ds_single_spread = xr.Dataset({ k: v for ds in dss_single_spread for k, v in ds.items() })

    return UncertainDataset(mean=ds_single_mean, spread=ds_single_spread)

ds_single = _load_single_dataset()

def _load_pressure_dataset() -> UncertainDataset:
    ds_pressure_mean = xr.open_mfdataset(sorted(data.glob(str(Path("reanalysis-era5-pressure-levels_ensemble_mean_*_*") / "data_stream-enda_stepType-instant.nc"))), chunks={})
    ds_pressure_spread = xr.open_mfdataset(sorted(data.glob(str(Path("reanalysis-era5-pressure-levels_ensemble_spread_*_*") / "data_stream-enda_stepType-instant.nc"))), chunks={})

    return UncertainDataset(mean=ds_pressure_mean, spread=ds_pressure_spread)

ds_pressure = _load_pressure_dataset()
