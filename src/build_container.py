from docker import from_env

def buildContainer(dockerfilePath: str, tarballPath: str, birdConfHash: str):

    client = from_env()
    image = client.images.build(
        path=dockerfilePath,
        tag=f"bgpbox:{birdConfHash}",
        forcerm=True,
        nocache=True
    )[0]

    with open(f"{tarballPath}", "wb") as file:
        for chunk in image.save(named=True):
            file.write(chunk)

    client.images.remove(image.id)