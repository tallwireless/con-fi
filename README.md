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

# Running
This project is meant to be running via `docker-compose`. The easy way to run
it is as such:

    git clone https://github.com/tallwireless/con-fi.git
    cd con-fi
    docker-compose up

On up, the database, application server, proxy, and RADIUS server will all
come up.

The registration page can be found at `http://localhost:8080`.
The RADIUS server can be accessed via `localhost:1812`.

## Adding RADIUS clients
Sadly at this point in the development of this project, RADIUS clients have to
be added manually to the database. This can be accomplished with the following
postgres query:

    INSERT INTO nas (nasname, shortname, secret)
    VALUES ('192.5.44.10', '192.5.44.10', 'thisshouldbechanged')

After adding, changing, or removing devices from the NAS table, the FreeRADIUS
service will have to be restarted:

    docker-compose restart radius

# Configuration
##
The application itself is configured via enviroment variables passed into the
Docker image. These can be set in the settings.env file.

    DB_DEBUG
        Default: False
        Description: This is the verbose setting for SQLAlchemy and will
        result in all SQL queries being sent to the logs.

    POSTGRES_USER
        Default: dev
        Description: Username for connecting to the database

    POSTGRES_PASSWORD
        Default: dev
        Description: Password for connecting to the database

    POSTGRES_DB
        Default: confi
        Description: What database to connect to

    POSTGRES_HOST
        Default: db
        Description: Host where the database is located. Do not set if using
        docker-compose.

    POSTGRES_PORT
        Default: 5432
        Description: Port to connect over. Do not set if using docker-compose.

    APP_KEY
        Default: 11111111111111111
        Description: This is a key used for encryption session related data
        within the app.
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
