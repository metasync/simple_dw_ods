from pathlib import Path

from dagster_sling import SlingResource, sling_assets

data_dir = Path(__file__).joinpath("..", "..", "..", "..", "data", "jaffle_shop")

replication_config = {
  "source": "local",
  "target": "simple_dw",
  "defaults": {
    "mode": "full-refresh",
  },
  "streams": {
    f"file://{data_dir.joinpath("raw_customers.csv").resolve()}": {
      "object": "jaffle_shop.ods_customers",
    },
    f"file://{data_dir.joinpath("raw_items.csv").resolve()}": {
      "object": "jaffle_shop.ods_items",
    },
    f"file://{data_dir.joinpath("raw_orders.csv").resolve()}": {
      "object": "jaffle_shop.ods_orders",
      "columns": { "ordered_at": "datetime" },
    },
    f"file://{data_dir.joinpath("raw_products.csv").resolve()}": {
      "object": "jaffle_shop.ods_products"
    },
    f"file://{data_dir.joinpath("raw_stores.csv").resolve()}": {
      "object": "jaffle_shop.ods_stores",
      "columns": { "opened_at": "datetime" },
    },
    f"file://{data_dir.joinpath("raw_supplies.csv").resolve()}": {
      "object": "jaffle_shop.ods_supplies",
    },
    f"file://{data_dir.joinpath("raw_tweets.csv").resolve()}": {
      "object": "jaffle_shop.ods_tweets",
      "columns": { "tweeted_at": "datetime" },
    },
  },
}

@sling_assets(replication_config=replication_config)
def raw_assets(context, sling: SlingResource):
  yield from sling.replicate(context=context)
  for row in sling.stream_raw_logs():
    context.log.info(row)
