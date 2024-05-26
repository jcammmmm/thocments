Container Terminology
==================================================
> Container technology involves many parts and concepts. In this guide I will provide the most common names and how they get involved in this technology. In addition, serveral hands on examples are provided with Podman.

Container Manager
--------------------
They are called _runtimes_ in kubernetes [docs](https://kubernetes.io/docs/setup/production-environment/container-runtimes)
- `containerd`
- `CRI-O`: Interface Implementation (Kubernetes CRI) to run any compatible container runtime (OCI)
- `Docker Engine`
- `Mirantis Container Runtime`

Container Runtime
--------------------
- `runc`
- `crun`: _A fast and low-memory footprint OCI Container Runtime fully written in C._[1]
- `Kata containers`
- `runv`: _runV is a hypervisor-based runtime for OCI._ [2]. This runtime is currently obsolete.

Podman
--------------------
* Podman: does not use a daemon to manage containers. It relies on `systemd`. 
    - `systemd`: from manpage: _is a system and service manager for Linux operating systems. When run as first process on boot (as PID 1), it acts as init system that brings up and maintains userspace services. Separate instances are started for logged-in users to start their services._
		* `runc`: [docs](https://github.com/opencontainers/runc) from github readme: _is a CLI tool for spawning and running containers on Linux according to the OCI specification._
		
It is useful to look at this output when you try to install with `sudo apt install podman`:
```log
The following additional packages will be installed:
  aardvark-dns buildah catatonit conmon containernetworking-plugins crun fuse-overlayfs golang-github-containers-common
  golang-github-containers-image iptables libip6tc2 libslirp0 libsubid4 netavark slirp4netns uidmap
Suggested packages:
  containers-storage firewalld docker-compose
```		
### Podman Initial configs
In order to download images from _DockerHub_ you must add at the end of the config file `/etc/containers/registries.conf`, the following configuration:
```conf
[registries.search]
registries = ['container-registry.oracle.com', 'quay.io', 'docker.io']
```

### Rootless vs rootless containers
As any other software, Podman can be executed as an _root_ or _admin_ user. When you run Podman without `sudo` is said that you are running Podman _rootless_. When you run prefix every command with `sudo` is said that you are running Podman _rootfull_. When you run something _rootless_ will not be available in _rootfull_ environment and viceversa, for example an image pulled in an _rootfull_ mode will not be available in _rootless_ environment.

The ideal scenario when your are running software is to execute it without admin/root permissions. Podman can be ran without root permissions (i.e. without the `sudo` command), however that comes with some drawbacks. The main drawback is that since the user that is being executing the containers does not have full access to the system, you must throw additional commands in order to have networking between your pods or containers. The tecnical [4] difference is the following:
- rootfull : `containernetworking`
- rootless : `slirp4netns`	

### One Container Basic Setup
1. Launch a container `podman run -dt --name webserver --net podman1 -p 8081:80 quay.io/libpod/banner`

### Two Container Basic Setup (no pod) [3]
Please note that every command is thrown with `sudo`, in order to ease the newtworking process. This example shows how to intercommunicate two _containers_. 
1. Create network `sudo podman network create innernetwork`
2. Launch a database `sudo podman run --name highspeed-database -e POSTGRES_PASSWORD=mysecretpassword -d registry.hub.docker.com/library/postgres`
3. Launch a database web client `sudo podman run --name highspeed-webclient -p 8080:8080 -d registry.hub.docker.com/library/adminer`
4. Connect both containers to the network 
	- `sudo podman network connect innernetwork highspeed-database`
	- `sudo podman network connect innernetwork highspeed-webclient`
5. Obtain the database ip address: `sudo podman inspect highspeed-database |  grep IPA`
6. Go to `http://localhost:8080/` and put the following database login details:
	- System: PostgresSQL
	- Server: database.ip.address
	- Username: postgres
	- Password: mysecretpassword
	- Database: postgress
	
### Two Container Basic Setup (with pod) [3]
This interconnection setup for containers relies in the _pod_ concept. A _pod_ is a collection of containers that share the same networking space. Since they are under the same network space, you can refer to each other as _localhost_.
Moreover, it seems that it is no possible to move and already created container to a pod. In order to add a container to a pod, it must be specefied at the moment you create the container.
1. `sudo podman pod create --name reldatapod -p 8089:8080`
2. `sudo podman run --pod reldatapod --name highspeed-poddatabase -e POSTGRES_PASSWORD=mysecretpassword -d registry.hub.docker.com/library/postgres`
3. `sudo podman run --pod reldatapod --name highspeed-podwebclient -d registry.hub.docker.com/library/adminer`
4. Go to `http://localhost:8089/` and put the following database login details:
	- System: PostgresSQL
	- Server: localhost
	- Username: postgres
	- Password: mysecretpassword
	- Database: postgress

Container Shim
--------------------
Glue software.


Podman Cheat Sheet
==================================================
* run and `--rm` remove when exit and `-d` run in background (detached) and `-t` allocate a pseudo-tty terminal.
```sh
sudo podman run --rm -dt containername
```

```sh
sudo podman container list
sudo podman ps
sudo podman logs -f b76e2ddc91c3
sudo podman top b76e2ddc91c3
sudo podman port -l 
sudo podman inspect -f "{{.NetworkSettings.IPAddress}}" containername
sudo podman inspect containername | grep IPA
sudo podman pod stats podname
sudo podman pod ps
sudo podman build -t zookeeper:3.9.1 .
sudo podman image list
```


Aliases
--------------------
They have the following form `p` + `3-first-letters` + `2-letter-action`
```sh
alias pcon='podman container -h'
alias pconls='podman container list'
alias pconrm='podman container rm'
alias pconstop='podman container stop'
alias pps='podman ps'
alias pimals='podman images'
alias plog='podman logs -f'
alias ptop='podman top'
```





References
==================================================
* [1](https://github.com/containers/crun)
* [2](https://github.com/hyperhq/runv)
* [3](https://github.com/containers/podman/blob/main/docs/tutorials/basic_networking.md)
* [4](https://www.redhat.com/sysadmin/container-networking-podman)
