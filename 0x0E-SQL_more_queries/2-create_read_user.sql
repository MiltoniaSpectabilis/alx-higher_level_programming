-- Script to create read user

CREATE USER read_user WITH PASSWORD 'read_user';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO read_user;
