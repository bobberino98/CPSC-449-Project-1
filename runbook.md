# CPSC-449-Project-1

# Support Contacts

|        | Team           | Contact Info                   | Runbook Review                  |
|--------|----------------|--------------------------------|---------------------------------|
|Level 1 | Operations     | bobberino98@csu.fullerton.edu  | James Dobson - 3/16/2020        |
|Level 2 | SDET           | ywen1306@csu.fullerton.edu     | Yinglin Wen - 3/16/2020         |
|Level 3 | Dev            | almuhana@csu.fullerton.edu     | Abdulmalik Almuhana - 3/16/2020 |


# Requirements

User's system must have installed: Flask v1.1.1, Caddy v1.0.4, and Gunicorn v20.0.4.
If these requirements are not available, a shell script (setup.sh) is provided that will install them for the user.

# Starting the Services
To start the services, these commands must be run, in separate terminals, from the base directory:

ulimit -n 8192 && caddy

foreman start -m posts=3,accounts=3

There is a shell script (start_server.sh) that will run these commands automatically, opening terimnals for each server

# Shutting down the Services
To shut down the servers, simply kill the processes in the terminal by either closing the windows or pressing Ctrl+C.

# Network

| Service      | Port        | Protocol       |
|--------------|-------------|----------------|
| posts        | 5000        | TCP - http     |
| accounts     | 5100        | TCP - http     |

# Filesystem

| Service          | Data                                |
|------------------|-------------------------------------|
| posts            | /Dev/PostAPI                        |
| accounts         | /Dev/UserAccountAPI                 |
| Post Database    | /Dev/PostAPI/posts.db               |
| Account Database | /Dev/UserAccountAPI/user_account.db |



