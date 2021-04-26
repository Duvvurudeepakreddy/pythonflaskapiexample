-- Table: tabledata.songsdata

-- DROP TABLE tabledata.songsdata;

CREATE TABLE tabledata.songsdata
(
    id numeric NOT NULL,
    title_of_the_song character varying COLLATE pg_catalog."default",
    duration bigint,
    uploaded_time character varying COLLATE pg_catalog."default",
    host character varying COLLATE pg_catalog."default",
    participants character varying COLLATE pg_catalog."default",
    narrator character varying COLLATE pg_catalog."default",
    author character varying COLLATE pg_catalog."default",
    type character varying COLLATE pg_catalog."default"
  
)

TABLESPACE pg_default;

ALTER TABLE tabledata.songsdata
    OWNER to postgres;