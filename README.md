# con-fi
Light Weight WiFi Management Tool Set for Conferences inspired by Dragorn's ShmooCon System

# Hopes and Dreams
This is a project I'm throwing to together to provide a lightweight toolset
for wireless admins at conferences. The hope is to be able to provide the
following:

 * Self Registration for Conference Guests (Completed)
 * Integrated RADIUS Server (Completed)
 * MAC Address Blocking
 * User Management
 * Basic VLAN Assignment for Classes of Users (Partially Completed)
 * System packaged in Docker Containers or ablity to run it on bare metal (Partially Completed)

# Before Running
Before running ConFi, please ensure the SSL certs are setup correctly as
described in the README file in the SSL directory.

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

# Adding RADIUS clients
Sadly at this point in the development of this project, RADIUS clients have to
be added manually to the database. This can be accomplished with the following
postgres query:

    INSERT INTO nas (nasname, shortname, secret)
    VALUES ('192.5.44.10', '192.5.44.10', 'thisshouldbechanged')

After adding, changing, or removing devices from the NAS table, the FreeRADIUS
service will have to be restarted:

    docker-compose restart radius

# Configuration
Most of the application is controlled via environment variables. See the
`settings.env` file for configuration varibles and discriptions.
