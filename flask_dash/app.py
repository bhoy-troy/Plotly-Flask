import json
import logging
import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from flask_caching import Cache

app = dash.Dash(__name__)
server = app.server
cache_enabled = app.config.get("cache", {}).get("enabled", False)
if cache_enabled:
    # todo: Add caching for storing daily data
    CACHE_CONFIG = {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_URL": app.config.get("cache", {}).get("url"),
    }
    cache = Cache()
    cache.init_app(server, config=CACHE_CONFIG)
