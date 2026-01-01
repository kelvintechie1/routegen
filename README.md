# Route Generator

**What does this package do?**

Exactly what it says on the tin - it's a route generator! Tired of creating six million loopbacks every time you need to pump a bunch of routes into a routing protocol for your lab environment? Be tired no more! This package generates an arbitrary number of random routes, alongside random route attributes (subject to any constraints defined in your configuration for this package), and allows you to export those routes using a variety of methods.

To be clear, if you need, like, two routes, don't bother with this package. Use this as the rule of thumb - if you need to create so many routes, your fingers will kill you tomorrow if you try to do so manually, look no further than this package!

Use Cases/Models:
There are a couple of ways you can use this package. Of course, these are all just suggestions and you are free to use it as you wish. 

* * Export all generated routes and associated path attributes as configuration commands. From there, you can add those configuration commands to any ol' router in your lab environment that you want to serve as the source of those routes.
* Export a Docker image containing an instance of the BIRD internet routing daemon that is preconfigured with all of the routes and neighbors that you need and import it onto your desired container host using the `docker load -i <file>` command (e.g., for Containerlab/native Docker use cases) or imported into a network emulation platform (e.g., Cisco Modeling Labs or EVE-NG). From there, you can start a new container using this image for any environment where you need a quick and dirty source of random/"internet" routes!

Supported Platforms:
* Cisco IOS/IOS-XE
* Juniper Junos
* BIRD container

Planned Platforms:
* Cisco IOS-XR

Supported Path Attributes:
* NEXT-HOP
* AS-PATH
* Communities

Planned Functionality:
* Import routes from BGPdump/MRT format
* Allow definition of basic policy inside of config.yml file (e.g., to selectively apply path attributes)

Some Important Notes:
* **Specifically for the container option:** by design, there is a constraint built into the configuration validation that requires all peerings between the bgpbox and the peer router to be eBGP. Put another way, the local ASN and any neighbor ASN(s) defined in the config file **MUST** be different. This restriction solely exists to make things easier, since it means that we don't have to consider any wonky iBGP behaviors, in terms of propagating the generated routes further into the lab network. Also, it means that we can just consider eBGP path attributes (i.e., no local preference).