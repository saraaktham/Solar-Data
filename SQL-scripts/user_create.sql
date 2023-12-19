-- create user
create user sara with password 'nrel';
-- grant connection
grant connect on database "sara-nsrdb-dni" to sara;
-- grant table permission
grant select, insert, update, delete on all tables in schema public to sara;