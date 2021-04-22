create table websites
(
	id bigserial not null
		constraint websites_pk
			primary key,
	url varchar(255) not null
);

create unique index websites_url_uindex
	on websites (url);

create table bodies
(
	body varchar(510),
	website_id bigint not null
);

create table titles
(
	title varchar(255),
	website_id bigint not null
);

create table images
(
	image_url varchar(255) not null,
	website_id bigint not null
);

