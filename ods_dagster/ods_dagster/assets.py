from importlib import import_module

from dagster import load_assets_from_modules
from .environment import dagster_env


def assets(dagster_env: str):
  return load_assets_from_modules(
      modules=map(__import_assets_module, ["jaffle_shop"]),
      group_name="jaffle_shop",
  )

def __import_assets_module(source, dagster_env=dagster_env):
  module_name = f"ods_dagster.{source}.{dagster_env}_assets"
  assets_module = import_module(module_name)
  if assets_module is not None:
    return assets_module
  else:
    raise ValueError(f"{module_name} cannot be found")
