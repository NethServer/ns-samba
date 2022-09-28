========
ns-samba
========

This is a vanilla build of Samba 4.
The package is distributed inside ``nethserver-dc`` rpm which
runs Samba 4 inside a container named ``nsdc``.

How to build
============

1. Download all sources ::

  spectool -g ns-samba.spec

2. Create needed tarballs ::

    export sambaver=`grep Version ns-samba.spec | cut -d ':' -f 2 | tr -d ' '`
    git archive --format=tar --prefix=ns-samba-$sambaver/ HEAD | tar xf -
    tar -c -z --exclude-vcs --exclude='.gitignore' -f  ns-samba-$sambaver.tar.gz ns-samba-$sambaver
    rm -rf ns-samba-$sambaver

   Where ``$sambaver`` is the samba version saved inside the spec file.

3. Create the source RPM ::

    mock --resultdir=. -r nethserver-7-x86_64 -D 'dist .ns7' --buildsrpm --spec ns-samba.spec --sources .

4. Create the binary RPM ::

    mock --resultdir=. -r nethserver-7-x86_64 -D 'dist .ns7' ns-samba-$sambaver-1.ns7.src.rpm
