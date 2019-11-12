docker cp /Users/admin/Documents/docker_new/falcon-intern/tests/test_03/SQL/CreateDatabase.sql hungphat_falcon_intern_postgres:/
docker cp /Users/admin/Documents/docker_new/falcon-intern/tests/test_03/SQL/CreateCustomer.sql hungphat_falcon_intern_postgres:/
docker cp /Users/admin/Documents/docker_new/falcon-intern/tests/test_03/SQL/InsertList.sql hungphat_falcon_intern_postgres:/

psql -Upostgres -f /CreateDatabase.sql
psql -Upostgres -dpsql -Upostgres -d cutomserdata -f /CreateCustomer.sql
psql -Upostgres -dpsql -Upostgres -d cutomserdata -f /InsertList.sql
psql -Upostgres -d cutomserdata  -c 'select * from Customer'

