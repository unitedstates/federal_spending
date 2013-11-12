
-- full-text
drop index if exists usaspending_grant_agency_name_ft;
drop index if exists usaspending_grant_recipient_name_ft;

create index usaspending_grant_agency_name_ft on usaspending_grant using gin(to_tsvector('retinaburner', agency_name));
create index usaspending_grant_recipient_name_ft on usaspending_grant using gin(to_tsvector('retinaburner', recipient_name));

create index usaspending_grant_total_funding_amount on usaspending_grant (total_funding_amount);
commit;