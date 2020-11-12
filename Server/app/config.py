from typing import Dict
from flask import Flask


class ConfigProvider:
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

    @staticmethod
    def apply_to_app(flask_app: Flask):
        configs: Dict[str, str] = vars(ConfigProvider)
        for (k, v) in configs.items():
            flask_app.config[k] = v
