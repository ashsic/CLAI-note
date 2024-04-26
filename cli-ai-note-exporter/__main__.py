"""Entry point script for cli-ai-note-exporter."""
# cli-ai-note-exporter/__main__.py"

from cli-ai-note-exporter import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()
