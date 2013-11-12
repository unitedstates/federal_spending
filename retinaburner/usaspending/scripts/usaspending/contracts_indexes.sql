drop index if exists usaspending_contract_unique_transaction_id;
create index usaspending_contract_unique_transaction_id on usaspending_contract (unique_transaction_id);

drop index if exists usaspending_contract_piid;
create index usaspending_contract_piid on usaspending_contract (piid);

drop index if exists usaspending_contract_district;
create index usaspending_contract_congressionaldistrict on usaspending_contract (statecode, congressionaldistrict);

create index usaspending_contract_dunsnumber on usaspending_contract (dunsnumber);
create index usaspending_contract_signeddate on usaspending_contract (signeddate);

drop index if exists usaspending_contract_fiscal_year;
create index usaspending_contract_fiscal_year on usaspending_contract (fiscal_year);

-- full-text
drop index if exists usaspending_contract_agency_name_ft;
drop index if exists usaspending_contract_contracting_agency_name_ft;
drop index if exists usaspending_contract_requesting_agency_name_ft;
drop index if exists usaspending_contract_vendor_city_ft;
drop index if exists usaspending_contract_vendor_name_ft;

create index usaspending_contract_agency_name_ft on usaspending_contract using gin(to_tsvector('retinaburner', agency_name));
create index usaspending_contract_contracting_agency_name_ft on usaspending_contract using gin(to_tsvector('retinaburner', contracting_agency_name));
create index usaspending_contract_requesting_agency_name_ft on usaspending_contract using gin(to_tsvector('retinaburner', requesting_agency_name));
create index usaspending_contract_vendor_city_ft on usaspending_contract using gin(to_tsvector('retinaburner', city));
create index usaspending_contract_vendor_name_ft on usaspending_contract using gin(to_tsvector('retinaburner', vendorname));

-- default sort order from API
drop index if exists usaspending_contract_defaultsort;
create index usaspending_contract_defaultsort on usaspending_contract (fiscal_year desc, obligatedamount desc);
commit;