rt4repobuilder - rt4 RPM and SRPM building toolki8t

License:  GPLv3
	  (Except where noted in subpackages)
Maintainer:   Nico Kadel-Garcia
Maintainer Email: nkadel@gmail.com

Note:
    This system builds RT version 4 and all its dependencies for RHEL
    7 based on the current release in Fedora. It also builds some
    added RT perl modules for enduser use. It's suitable for replacing
    the older "rt3" package in EPEL, but is not laid out identically,
    so it is not a drop-in replacement.

Usage:
    make install - build, and install for local access, the
    full build requirements for RT4. This is the normal bootstrap
    operation.

    make build - try and build all the components in the local
    environment, without using "mock"

    make all - build all comopnents using "mock" and the local
    RT4 repository, called "rt4repo"

    make epel - build only the compoenents that can be built
    from EPEL, without additional comopnents from this toolkit.

    make rt4 - buld the compnents that require the local EPEL
    compatible and RT4 component dependent packages.


Requirements: This toolkit requires the following tools:

     * The "mock" software for building RPM's, available from EPEL for
       RHEL based cystems.

     * Spare diskspace at /var/lib/mock and /var/cache/mock for the
       builky builds of mock chroot environments.

     * Reliable access to yum repositories for CentOS, RHEL, or
       Scietific Linux repositories, for the standard "mock"
       configuration.

     * Membership in the "mock" group for permissions to exucute the
       mock software.

     * PATH setting or an alias that accfess "/usr/bin/mock", not
       "/usr/sbin/mock".
