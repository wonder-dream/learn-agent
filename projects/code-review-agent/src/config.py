import os
from functools import lru_cache
from fastapi import Depends

class Settings:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_DEEPSEEK_API_KEY", "")
        self.model = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-pro")
        
@lru_cache
def get_settings():
    return Settings()