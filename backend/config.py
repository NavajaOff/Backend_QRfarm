"""Configuration module for the application."""
import os
from typing import Dict, Any

class Config:
    """Configuration class."""

    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')

    # Database configuration
    DB_CONFIG: Dict[str, Any] = {
        'host': os.environ.get('DB_HOST', 'shortline.proxy.rlwy.net'),
        'user': os.environ.get('DB_USER', 'root'),
        'password': os.environ.get('DB_PASSWORD', 'JoE6XNQo0oXrLoNGKyp0tWuEgRQojRwl'),
        'database': os.environ.get('DB_NAME', 'ferrocarril'),
        'port': int(os.environ.get('DB_PORT', '39213')),
        'raise_on_warnings': True,
        'autocommit': False,  # We want to control transactions explicitly
        'pool_name': 'qr_farm_pool',
        'pool_size': int(os.environ.get('DB_POOL_SIZE', '5')),
        'pool_reset_session': True
    }

    # JWT configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'dev')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', '3600'))  # 1 hour in seconds

    # Application configuration
    DEBUG = os.environ.get('FLASK_ENV') == 'development'
    TESTING = False
    JSON_SORT_KEYS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max-limit for file uploads
