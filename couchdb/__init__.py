# -*- coding: utf-8 -*-
#
# Copyright (C) 2007 Christopher Lenz
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from .client import Database, Document, Server
from .http import HTTPError, PreconditionFailed, Resource, \
        ResourceConflict, ResourceNotFound, ServerError, Session, \
        Unauthorized, Forbidden

try:
    from importlib.metadata import version as _dist_version
except ImportError:  # Python < 3.8
    def _dist_version(name):
        return __import__('pkg_resources').get_distribution(name).version

try:
    __version__ = _dist_version('CouchDB')
except Exception:
    __version__ = '?'
