# gcf

Prototypo/POC for accessing GCF from Raspberry Pi 3.

DO NOT INSTALL 
* python-cryptography 
* python-pyjwt
using apt

Relies on correct installs of 
* python3
* pip3py
* requests
* libffi-dev
* libssl-dev

Then from pip3
* install cffi --upgrade
* install cryptography --upgrade
* install pyjwt --upgrade

NOTE: pyjwt installed with pip/python2 still installs in /usr/local/lib/python3
