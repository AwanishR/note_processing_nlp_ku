CREATE USER 'nlp'@'localhost' IDENTIFIED BY  'nlp';GRANT ALL PRIVILEGES ON *.* TO 'nlp'@'localhost' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

drop table if exists ner;
Create table ner (
id int AUTO_INCREMENT PRIMARY KEY,
note_id varchar(50),
detected_element varchar (100),
element_type varchar(50),
set_id varchar(20),
sent_id varchar(50),
updated_date date);

