import json
import logging
import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from flask_caching import Cache
from flask_dash.index import app as _app

cache_enabled = _app.config.get("cache", {}).get("enabled", False)
if cache_enabled:
    # todo: Add caching for storing daily data
    CACHE_CONFIG = {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_URL": app.config.get("cache", {}).get("url"),
    }
    cache = Cache()
    cache.init_app(server, config=CACHE_CONFIG)
if __name__ == "__main__":
    _app.logger.info("Processing default request")
    debug = _app.config.get("DEBUG", False)
    _app.run_server( debug=True, threaded=True)