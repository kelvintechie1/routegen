from ipaddress import IPv4Network

class Route:
    def __init__(self, network: IPv4Network, aspath: list):
        self.network = network
        self.aspath = aspath

class Neighbor:
    def __init__(self, address: str, asn: int):
        self.address = address
        self.asn = asn