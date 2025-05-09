from dagster import Definitions
from .environment import dagster_env
from .assets import assets
from .resources import resources


defs = Definitions(
  assets=assets(dagster_env),
  resources=resources(dagster_env),
)
