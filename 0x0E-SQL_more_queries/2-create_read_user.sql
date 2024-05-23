-- Script to create read user

CREATE USER 'read'@'%' IDENTIFIED BY 'read';
GRANT SELECT ON *.* TO 'read'@'%';
FLUSH PRIVILEGES;
