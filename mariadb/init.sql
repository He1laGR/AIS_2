CREATE DATABASE delivery_service;

--create delivery table
CREATE TABLE delivery_service.delivery (
	delivery_id varchar(100) NOT NULL DEFAULT UUID(),
    author_id varchar(100) NOT NULL,
	weigth integer NOT NULL,
    category varchar(100) NOT NULL,
	delivery_from varchar(100) NOT NULL,
    delivery_to varchar(100) NOT NULL,
	pay_method varchar(100) NOT NULL,
    delivery_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

ALTER TABLE delivery_service.delivery ADD CONSTRAINT delivery_PK PRIMARY KEY (delivery_id);
ALTER TABLE delivery_service.delivery ADD CONSTRAINT user_id_author_id FOREIGN KEY(author_id) REFERENCES user(user_id);


--create user table
CREATE TABLE delivery_service.user (
	user_id varchar(100) NOT NULL DEFAULT UUID(),
	login varchar(100) NOT NULL,
	password varchar(100) NOT NULL,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	email varchar(100) NOT NULL,
    phone_number varchar(100) NOT NULL
);

ALTER TABLE delivery_service.user ADD CONSTRAINT user_PK PRIMARY KEY (user_id);


--create delivery_monitoring table
CREATE TABLE delivery_service.delivery_monitoring (
    delivery_id varchar(100) NOT NULL,
	delivery_status varchar(100) NOT NULL,
    sender_id varchar(100) NOT NULL,
    delivery_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

ALTER TABLE delivery_service.package ADD CONSTRAINT delivery_id_package_id FOREIGN KEY(delivery_id) REFERENCES delivery(delivery_id);


--insert in user table
INSERT INTO delivery_service.user (user_id, login, password, first_name, last_name, email, phone_number)
VALUES('63e46b49-d61a-4f8b-866e-247cf490272d', 'perviy', 'odin', 'Ivan', 'Pavlov', 'ivan_pavlov@google.com', '89003002040');

INSERT INTO delivery_service.user (user_id, login, password, first_name, last_name, email, phone_number)
VALUES('46d0467b-6549-4e23-932d-e8255ec9314e', 'vtoroy', 'dva', 'Sergey', 'Yuriev',  'sYuriev@yandex.ru', '89004004020');

INSERT INTO delivery_service.user (user_id, login, password, first_name, last_name, email, phone_number)
VALUES('f1b03ee7-5e4c-443f-a4f2-72f1351435c8', 'tretiy', 'tri', 'Fedor', 'Fedorov', 'fedorfed@yahoo.com', '88005553535');


-- insert in delivery table
INSERT INTO delivery_service.delivery (delivery_id, author_id, weigth, category, delivery_from, delivery_to, pay_method, delivery_date)
VALUES('c01749c7-c1a8-4720-a72d-d4e2db718915', '46d0467b-6549-4e23-932d-e8255ec9314e', 35, 'medium', 'Saint-P', 'Moscow', 'cash', current_timestamp());

INSERT INTO delivery_service.delivery (delivery_id, author_id, weigth, category, delivery_from, delivery_to, pay_method, delivery_date)
VALUES('3ad6f59d-9813-4c31-8226-c9645d0fab85', 'f1b03ee7-5e4c-443f-a4f2-72f1351435c8', 5, 'small', 'Moscow', 'Bryansk', current_timestamp());

INSERT INTO delivery_service.delivery (delivery_id, author_id, weigth, category, delivery_from, delivery_to, pay_method, delivery_date)
VALUES('0ecebf26-0b2a-413c-a53a-e9b7d1e9da10', '63e46b49-d61a-4f8b-866e-247cf490272d', 89, 'big', 'Murmansk', 'Petrozavodsk' current_timestamp());


-- insert in delivery_monitoring table
INSERT INTO delivery_service.delivery_monitoring (delivery_id, sender_id, delivery_status, delivery_date)
VALUES('c01749c7-c1a8-4720-a72d-d4e2db718915', '46d0467b-6549-4e23-932d-e8255ec9314e', 'in progress', current_timestamp());

INSERT INTO delivery_service.delivery_monitoring (delivery_id, sender_id, delivery_status, delivery_date)
VALUES('3ad6f59d-9813-4c31-8226-c9645d0fab85', 'f1b03ee7-5e4c-443f-a4f2-72f1351435c8', 'applied', current_timestamp());

INSERT INTO delivery_service.delivery_monitoring (delivery_id, sender_id, delivery_status, delivery_date)
VALUES('0ecebf26-0b2a-413c-a53a-e9b7d1e9da10', '63e46b49-d61a-4f8b-866e-247cf490272d', 'arrived', current_timestamp());
