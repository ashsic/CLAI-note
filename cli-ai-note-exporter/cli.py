"""This module provides the CLI for the note taking app."""
# cli-ai-note-exporter/cli.py

from typing import Optional
import Typer
from cli-ai-note-exporter import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}, v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Display the application's version.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return