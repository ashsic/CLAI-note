# cliNote/cli.py

from typing import Optional
import typer
from __init__ import __app_name__, __version__

app = typer.Typer()

@app.command()
def new(title: str = None, body: str = None):
    if not title:
        title = input("Enter the title for the note: ")
    if not body:
        body = input("Enter the body for the note: ")
    print(f'Note: {title}:\n {body}')

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
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