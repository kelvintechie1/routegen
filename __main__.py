import ipaddress as ip
from src.generate_routes import generateRoutes
from src.generate_config import platforms
from os import path
from yaml import safe_load
import click as cli

@cli.command()
@cli.option("-c", "--configfile", help="Specify path (including file name) to the config YAML file. By default, routegen assumes a config.yml file in the current working directory", type=str, default="config.yml")
def main(configfile: str) -> None:
    routes = []
    existingPrefixes = []

    with open(configfile) as configFile:
        config = safe_load(configFile)

    counter = 0
    while counter < config["basic"]["desiredNumOfRoutes"]:
        route = generateRoutes()
        if route.network not in existingPrefixes:
            routes.append(route)
            existingPrefixes.append(route.network)
            counter += 1

    platforms[config["basic"]["platform"]](path=path.join(path.dirname(__file__), "output"), routes=routes)

if __name__ == "__main__":
    main()

