drop table if exists tcsi_element;
create table tcsi_element(
    id serial primary key,
    element_no varchar(255),
    page_title varchar(255),
    description varchar(5000),
    code_category varchar(255),
    element_type varchar(255),
    width varchar(255),
    version_revision_date varchar(255),
    version varchar(255),
    years_version_active varchar(255),
    sub_header varchar(255),
    value varchar(255),
    meaning varchar(5000),
    derivation varchar(255),
    spec_flag varchar(255),
    retired varchar(255),
    page_access_timestamp timestamp,
    page_url varchar(255),
    page_harvestor varchar(255)
);