"""Main entry point for clandestine CLI."""

import typer
from modules.osint.cli import app as osint_app

app = typer.Typer()
app.add_typer(osint_app, name="osint")


if __name__ == "__main__":
    app()
