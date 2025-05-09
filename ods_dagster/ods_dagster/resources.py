import os

from dagster_sling import SlingConnectionResource, SlingResource
from dagster import EnvVar

from .environment import data_dir

sling_resource = SlingResource(
  connections=[
    SlingConnectionResource(
      name="local",
      type="LOCAL",
    ),
    SlingConnectionResource(
      name="simple_dw",
      type="starrocks",
      host=EnvVar("DW_HOST").get_value(),
      port=EnvVar("DW_PORT").get_value(),
      # database=EnvVar("DW_SCHEMA").get_value(),
      database=os.getenv("DW_SCHEMA", "sys"),
      user=EnvVar("DW_USER").get_value(),
      password=EnvVar("DW_PASSWORD").get_value(),
      fe_url=f"http://{EnvVar("DW_HOST").get_value()}:{EnvVar("DW_HTTP_PORT").get_value()}",
    ),
  ]
)

resources_by_env = {
  "dev": {
    "sling": sling_resource,
  },
  "snd": {
    "sling": sling_resource,
  },
  "prod": {
    "sling": sling_resource,
  }
}

def resources(dagster_env: str):
  return resources_by_env[dagster_env]
