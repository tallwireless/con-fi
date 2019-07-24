# con-fi
Light Weight WiFi Management Tool Set for Conferences inspired by Dragorn's ShmooCon System

# Hopes and Dreams
This is a project I'm throwing to together to provide a lightweight toolset
for wireless admins at conferences. The hope is to be able to provide the
following:

 * Self Registration for Conference Guests
 * Integrated RADIUS Server
 * MAC Address Blocking
 * User Management
 * Basic VLAN Assignment for Classes of Users
 * System packaged in Docker Containers or ablity to run it on bare metal

# Configuration
## FreeRADIUS
The `radius` directory is a fully working FreeRADIUS configuration which has
been tested on 3.0.19.

It will handle all authentication requests for EAP-PEAP/EAP-MSCHAPv2 on
127.0.0.1 port 1812.

The following files need to be added `radius/certs`:

    server.pem
      This is the private key for the cert without a passphrase on the key.

    server.crt
      This is the signed server certificate. It should include all INTERMEDIATAE
      CERTS for proper cert verification.

    ca.pem
      The root CA of the chain.

These files are required for being able to support EAP-PEAP.
