#! /bin/sh

# Create DB and user.
docker run -it -e PGPASSWORD=mysecretpassword --rm --link resources_portal_db:postgres postgres:9.6.6 psql -c "create database resources_portal" -h postgres -U postgres
docker run -it -e PGPASSWORD=mysecretpassword --rm --link resources_portal_db:postgres postgres:9.6.6 psql -c "CREATE ROLE resources_portal_user WITH LOGIN PASSWORD 'resources_portal_password';" -h postgres -U postgres
docker run -it -e PGPASSWORD=mysecretpassword --rm --link resources_portal_db:postgres postgres:9.6.6 psql -c 'GRANT ALL PRIVILEGES ON DATABASE resources_portal TO resources_portal_user;' -h postgres -U postgres

# Set up test DB.
docker run -it -e PGPASSWORD=mysecretpassword --rm --link resources_portal_db:postgres postgres:9.6.6 psql -c "create database test_resources_portal" -h postgres -U postgres
docker run -it -e PGPASSWORD=mysecretpassword --rm --link resources_portal_db:postgres postgres:9.6.6 psql -c 'GRANT ALL PRIVILEGES ON DATABASE test_resources_portal TO resources_portal_user;' -h postgres -U postgres

docker run -it -e PGPASSWORD=mysecretpassword --rm --link resources_portal_db:postgres postgres:9.6.6 psql -c 'ALTER USER resources_portal_user CREATEDB;' -h postgres -U postgres
docker run -it -e PGPASSWORD=mysecretpassword --rm --link resources_portal_db:postgres postgres:9.6.6 psql -c 'ALTER ROLE resources_portal_user superuser;' -h postgres -U postgres
