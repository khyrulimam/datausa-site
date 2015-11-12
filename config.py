# -*- coding: utf-8 -*-
import os

''' Default debugging to True '''
DEBUG = not os.environ.get("DATAUSA_PRODUCTION", False)

''' Base URL used for API calls '''
API = os.environ.get("DATAUSA_API", "http://postgres.datawheel.us")
PROFILES = ["cip", "soc", "naics", "geo"]
CROSSWALKS = ["acs_ind", "acs_occ"]

''' Use a filesystem cache '''
basedir = os.path.abspath(os.path.dirname(__file__))
CACHE_TYPE = 'filesystem'
CACHE_DIR = os.path.join(basedir, 'cache_data/')
CACHE_DEFAULT_TIMEOUT = os.environ.get("CACHE_DEFAULT_TIMEOUT", (60 * 60))

SPLASH_IMG_DIR = os.path.join(basedir, "datausa/static/img/{}/{}/")
