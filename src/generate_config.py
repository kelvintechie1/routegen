from objects import Route, Neighbor
from jinja2 import Environment, FileSystemLoader
from ipaddress import IPv4Address
from hashlib import sha256

def writeConfig(path: str, config: str, fileName: str = "config.txt"):
    with open(f"{path}/{fileName}") as file:
        file.write(config)

def config_ios():
    pass # to be added later

def config_junos(routes: list[Route], path: str):
    config = []
    for route in routes:
        config.append(f"set routing-options static route {str(route.network)} as-path path \"{" ".join(route.aspath)}\"")
    
    writeConfig(path=path, config="\n".join(config))

def config_container(path: str, routes: list[Route], neighbors: list[Neighbor], rid: IPv4Address):
    birdTemplate = Environment(loader=FileSystemLoader(path)).get_template("bird.conf.j2")
    birdContent = birdTemplate.render(
        rid=str(rid),
        routes=routes,
        neighbors=neighbors
    )

    birdContentHash = str(sha256(birdContent.encode("utf-8")).hexdigest())
    dockerTemplate = Environment(loader=FileSystemLoader(path)).get_template("Dockerfile.j2")
    dockerContent = dockerTemplate.render(
        hash=birdContentHash
    )

    for item in [f"{path}/bird.conf", f"{path}/../output/{birdContentHash}.bird.conf"]:
        with open(item, "w") as file:
            file.write(birdContent)
    
    with open(f"{path}/Dockerfile", "w") as file:
        file.write(dockerContent)
    


platforms = {"ios": config_ios, "junos": config_junos, "container": config_container}