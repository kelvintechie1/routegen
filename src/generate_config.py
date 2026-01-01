from src.objects import Route, Neighbor
from jinja2 import Environment, FileSystemLoader
from ipaddress import IPv4Address
from hashlib import sha256

def writeConfig(path: str, config: str):
    with open(f"{path}/config.txt") as file:
        file.write(config)

def config_ios():
    pass # to be added later

def config_junos(routes: list[Route], path: str):
    config = []
    for route in routes:
        config.append(f"set routing-options static route {str(route.network)} as-path path \"{" ".join(route.aspath)}\"")
    
    writeConfig(path=path, config="\n".join(config))

def config_container(path: str, routes: list[Route], neighbors: list[Neighbor] = [Neighbor("10.101.11.221", "100")], rid: IPv4Address = IPv4Address("100.100.100.100")):
    birdTemplate = Environment(loader=FileSystemLoader(path)).get_template("bird.conf.j2")
    birdContent = birdTemplate.render(
        rid=str(rid),
        routes=routes,
        neighbors=neighbors
    )

    dockerTemplate = Environment(loader=FileSystemLoader(path)).get_template("Dockerfile.j2")
    dockerContent = dockerTemplate.render(
        hash=str(sha256(birdContent.encode("utf-8")).hexdigest())
    )

    with open(f"{path}/bird.conf", "w") as file:
        file.write(birdContent)
    
    with open(f"{path}/Dockerfile", "w") as file:
        file.write(dockerContent)
    


platforms = {"ios": config_ios, "junos": config_junos, "container": config_container}