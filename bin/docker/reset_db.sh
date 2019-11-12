#!/usr/bin/env bash
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"  # get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
APP_HOME="$SCRIPT_HOME/../.."

c=hungphat_falcon_intern_postgres  # c aka container

docker cp "$APP_HOME/tests/test_03/SQL/CreateDatabase.sql" $c:/
docker cp "$APP_HOME/tests/test_03/SQL/CreateCustomer.sql" $c:/
docker cp "$APP_HOME/tests/test_03/SQL/InsertList.sql"     $c:/

docker exec $c bash -c "psql -Upostgres                 -f /CreateDatabase.sql"
docker exec $c bash -c "psql -Upostgres -d customerdata -f /CreateCustomer.sql"
docker exec $c bash -c "psql -Upostgres -d customerdata -f /InsertList.sql"
docker exec $c bash -c "psql -Upostgres -d customerdata -c 'select * from customers'"
