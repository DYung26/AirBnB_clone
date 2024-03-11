#!/usr/bin/python3
"""
Initialization Script: __init__.py
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
