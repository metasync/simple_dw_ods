from dagster_sling import SlingResource, sling_assets

replication_config = {
  "source": "local",
  "target": "simple_dw",
  "defaults": {
    "mode": "full-refresh",
  },
  "streams": {
    "file:///home/jovyan/projects/simple-dw/data/jaffle_shop/raw_customers.csv": {
      "object": "jaffle_shop.ods_customers",
    },
    "file:///home/jovyan/projects/simple-dw/data/jaffle_shop/raw_items.csv": {
      "object": "jaffle_shop.ods_items",
    },
    "file:///home/jovyan/projects/simple-dw/data/jaffle_shop/raw_orders.csv": {
      "object": "jaffle_shop.ods_orders",
      "columns": { "ordered_at": "datetime" },
    },
    "file:///home/jovyan/projects/simple-dw/data/jaffle_shop/raw_products.csv": {
      "object": "jaffle_shop.ods_products"
    },
    "file:///home/jovyan/projects/simple-dw/data/jaffle_shop/raw_stores.csv": {
      "object": "jaffle_shop.ods_stores",
      "columns": { "opened_at": "datetime" },
    },
    "file:///home/jovyan/projects/simple-dw/data/jaffle_shop/raw_supplies.csv": {
      "object": "jaffle_shop.ods_supplies",
    },
    "file:///home/jovyan/projects/simple-dw/data/jaffle_shop/raw_tweets.csv": {
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
