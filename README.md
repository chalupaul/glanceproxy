glanceproxy
===========

A multi-glance front end that supports inline image conversion and glance syncing.

Requirements
============


*  pyyaml
*  bottle
*  requests

Setup
=====

    $ cd /path/to/your/dev/dir
    $ git clone git@github.com:chalupaul/glanceproxy.git
    $ virtualenv glanceproxy
    $ cd glanceproxy
    $ source bin/activate
    $ pip install pyyaml requests bottle

Point apache2 to the www directory and go!

Use this for your apache config:


    WSGIDaemonProcess glanceproxy user=www-data group=www-data processes=1 threads=5
    WSGIScriptAlias / /var/www/glanceproxy/www/adapter.wsgi

    <Directory /var/www/glanceproxy>
        WSGIProcessGroup glanceproxy
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>