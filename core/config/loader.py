"""Configuration loader for clandestine project."""

from pathlib import Path
import yaml
from pydantic import BaseModel


class Config(BaseModel):
    """Application configuration schema."""

    shodan_api_key: str = ""
    twitter_bearer_token: str = ""
    tor_proxy: str = "socks5://localhost:9050"
    log_level: str = "INFO"


def load_config(env: str = "dev") -> Config:
    """
    Load YAML configuration file based on environment.

    Args:
        env (str): Environment name, e.g., 'dev', 'prod'.

    Returns:
        Config: Parsed configuration object.
    """
    config_path = Path(f"config/{env}.yaml")
    if not config_path.exists():
        raise FileNotFoundError(f"Config file {config_path} not found")
    return Config(**yaml.safe_load(config_path.read_text(encoding="utf-8")))
