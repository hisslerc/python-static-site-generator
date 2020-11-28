import typer
import ssg.parsers
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest, "parsers": [ssg.parsers.ResourceParser()]}
    site = Site(**config).build()


if __name__ == '__main__':
    typer.run(main)


