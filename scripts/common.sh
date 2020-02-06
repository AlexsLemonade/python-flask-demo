#!/bin/sh

get_docker_db_ip_address () {
    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' resources_portal_db 2> /dev/null
}
