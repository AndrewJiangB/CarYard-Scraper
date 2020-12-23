drop table cars cascade;
drop table hashes cascade;

create table cars (
        id serial primary key,
        make varchar(50) NOT NULL,
        model varchar(50) NOT NULL,
        year varchar(4) NOT NULL,
        price int NOT NULL
);

create table specs (
    id primary key,
    odometer varchar(10),
    engine varchar(10),
    transmission varchar(10),
    drivetrain varchar(10),
    additional varchar(100)
);

create table hashes (
        id primary key,
        hashedData varchar(50),
);

INSERT INTO cars(make, model, year, price) values('Mazda', 'CX-5', '2017', 20000);
INSERT INTO cars(make, model, year, price) values('Honda', 'Civic', '2007', 3000);
INSERT INTO hashes(id, hashedData) values(1, 'abc');
INSERT INTO hashes(id, hashedData) values(2, 'bcd');
