import ipaddress as ip
from src.generate_routes import generateRoutes
from src.generate_config import platforms
from os import path

def main():
    routes = []
    existingPrefixes = []
    desiredNumOfRoutes = 1000
    desiredPlatform = "container"

    counter = 0
    while counter < desiredNumOfRoutes:
        route = generateRoutes()
        if route.network not in existingPrefixes:
            routes.append(route)
            existingPrefixes.append(route.network)
            counter += 1

    config = platforms[desiredPlatform](path=path.join(path.dirname(__file__), "container"), routes=routes)

    print(config)

    #with open("output/config.txt", "w") as file:
    #    file.write(config)

if __name__ == "__main__":
    main()