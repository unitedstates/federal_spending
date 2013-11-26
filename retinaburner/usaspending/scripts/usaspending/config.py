INDEX_COLS_BY_TABLE = {
    'usaspending_contract': [
        'using gin (to_tsvector(\'retinaburner\'::regconfig, agency_name::text))',
        'statecode, congressionaldistrict',
        'using gin (to_tsvector(\'retinaburner\'::regconfig, contracting_agency_name::text))',
        '(fiscal_year DESC, obligatedamount DESC)',
        'dunsnumber',
        'obligatedamount',
        'piid',
        'using gin (to_tsvector(\'retinaburner\'::regconfig, requesting_agency_name::text))',
        'signeddate',
        'using gin (to_tsvector(\'retinaburner\'::regconfig, city::text))',
        'using gin (to_tsvector(\'retinaburner\'::regconfig, vendorname::text))',
        'fiscal_year',
        'unique_transaction_id',
    ],
    'usaspending_grant': [
        'using gin (to_tsvector(\'retinaburner\'::regconfig, agency_name::text)) ',
        'using gin (to_tsvector(\'retinaburner\'::regconfig, recipient_name::text))',
        'total_funding_amount',
        'unique_transaction_id',
        'fiscal_year'
    ],
}