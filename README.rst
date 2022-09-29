========
ns-samba
========

This is a vanilla build of Samba 4.
The package is distributed inside ``nethserver-dc`` rpm which
runs Samba 4 inside a container named ``nsdc``.

How to build
============

After installing `makerpms`, as described in [makerpms
README](https://github.com/NethServer/nethserver-makerpms/blob/master/README.rst),
run the following command to start the build:

    PODMAN_ARGS=--volume=$PWD/copr.repo:/etc/yum.repos.d/copr.repo YUM_ARGS=@development makerpms ns-samba.spec
