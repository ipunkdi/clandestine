"""CLI module for OSINT commands."""

import typer
from .social_media import scrape_twitter

app = typer.Typer()


@app.command()
def twitter(keyword: str) -> None:
    """
    Scrape Twitter for a given keyword.

    Args:
        keyword (str): Keyword to search for.
    """
    results = scrape_twitter(keyword)
    typer.echo("\n".join(results))
