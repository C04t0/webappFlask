drop table if exists users;

create table users (
    id integer primary key autoincrement,
    created timestamp not null default current_timestamp,
    name text not null,
    age integer not null,
    image text not null
);