CREATE OR REPLACE FUNCTION usaspending_contract_update_child()
RETURNS TRIGGER AS $$
DECLARE tablename TEXT;
DECLARE statement TEXT;
DECLARE fy TEXT;

BEGIN
    RAISE NOTICE 'in func';
    fy := trim(to_char(NEW.fiscal_year, '9999'));
    tablename := 'usaspending_contract_' || fy;
    statement := 'UPDATE ' || tablename || ' AS OLD SET ' || 

  '"unique_transaction_id" = ' || coalesce(quote_literal(NEW.unique_transaction_id), 'NULL') || ',   "transaction_status" = ' || coalesce(quote_literal(NEW.transaction_status), 'NULL') || ',   "obligatedamount" = ' || coalesce(quote_literal(NEW.obligatedamount), 'NULL') || ',   "baseandexercisedoptionsvalue" = ' || coalesce(quote_literal(NEW.baseandexercisedoptionsvalue), 'NULL') || ',   "baseandalloptionsvalue" = ' || coalesce(quote_literal(NEW.baseandalloptionsvalue), 'NULL') || ',   "maj_agency_cat" = ' || coalesce(quote_literal(NEW.maj_agency_cat), 'NULL') || ',   "mod_agency" = ' || coalesce(quote_literal(NEW.mod_agency), 'NULL') || ',   "maj_fund_agency_cat" = ' || coalesce(quote_literal(NEW.maj_fund_agency_cat), 'NULL') || ',   "contractingofficeagencyid" = ' || coalesce(quote_literal(NEW.contractingofficeagencyid), 'NULL') || ',   "contractingofficeid" = ' || coalesce(quote_literal(NEW.contractingofficeid), 'NULL') || ',   "fundingrequestingagencyid" = ' || coalesce(quote_literal(NEW.fundingrequestingagencyid), 'NULL') || ',   "fundingrequestingofficeid" = ' || coalesce(quote_literal(NEW.fundingrequestingofficeid), 'NULL') || ',   "fundedbyforeignentity" = ' || coalesce(quote_literal(NEW.fundedbyforeignentity), 'NULL') || ',   "signeddate" = ' || coalesce(quote_literal(NEW.signeddate), 'NULL') || ',   "effectivedate" = ' || coalesce(quote_literal(NEW.effectivedate), 'NULL') || ',   "currentcompletiondate" = ' || coalesce(quote_literal(NEW.currentcompletiondate), 'NULL') || ',   "ultimatecompletiondate" = ' || coalesce(quote_literal(NEW.ultimatecompletiondate), 'NULL') || ',   "lastdatetoorder" = ' || coalesce(quote_literal(NEW.lastdatetoorder), 'NULL') || ',   "contractactiontype" = ' || coalesce(quote_literal(NEW.contractactiontype), 'NULL') || ',   "reasonformodification" = ' || coalesce(quote_literal(NEW.reasonformodification), 'NULL') || ',   "typeofcontractpricing" = ' || coalesce(quote_literal(NEW.typeofcontractpricing), 'NULL') || ',   "priceevaluationpercentdifference" = ' || coalesce(quote_literal(NEW.priceevaluationpercentdifference), 'NULL') || ',   "subcontractplan" = ' || coalesce(quote_literal(NEW.subcontractplan), 'NULL') || ',   "lettercontract" = ' || coalesce(quote_literal(NEW.lettercontract), 'NULL') || ',   "multiyearcontract" = ' || coalesce(quote_literal(NEW.multiyearcontract), 'NULL') || ',   "performancebasedservicecontract" = ' || coalesce(quote_literal(NEW.performancebasedservicecontract), 'NULL') || ',   "majorprogramcode" = ' || coalesce(quote_literal(NEW.majorprogramcode), 'NULL') || ',   "contingencyhumanitarianpeacekeepingoperation" = ' || coalesce(quote_literal(NEW.contingencyhumanitarianpeacekeepingoperation), 'NULL') || ',   "contractfinancing" = ' || coalesce(quote_literal(NEW.contractfinancing), 'NULL') || ',   "costorpricingdata" = ' 

|| coalesce(quote_literal(NEW.costorpricingdata), 'NULL') || ',   "costaccountingstandardsclause" = ' || coalesce(quote_literal(NEW.costaccountingstandardsclause), 'NULL') || ',   "descriptionofcontractrequirement" = ' || coalesce(quote_literal(NEW.descriptionofcontractrequirement), 'NULL') || ',   "purchasecardaspaymentmethod" = ' || coalesce(quote_literal(NEW.purchasecardaspaymentmethod), 'NULL') || ',   "numberofactions" = ' || coalesce(quote_literal(NEW.numberofactions), 'NULL') || ',   "nationalinterestactioncode" = ' || coalesce(quote_literal(NEW.nationalinterestactioncode), 'NULL') || ',   "progsourceagency" = ' || coalesce(quote_literal(NEW.progsourceagency), 'NULL') || ',   "progsourceaccount" = ' || coalesce(quote_literal(NEW.progsourceaccount), 'NULL') || ',   "progsourcesubacct" = ' || coalesce(quote_literal(NEW.progsourcesubacct), 'NULL') || ',   "account_title" = ' || coalesce(quote_literal(NEW.account_title), 'NULL') || ',   "rec_flag" = ' || coalesce(quote_literal(NEW.rec_flag), 'NULL') || ',   "typeofidc" = ' || coalesce(quote_literal(NEW.typeofidc), 'NULL') || ',   "multipleorsingleawardidc" = ' || coalesce(quote_literal(NEW.multipleorsingleawardidc), 'NULL') || ',   "programacronym" = ' || coalesce(quote_literal(NEW.programacronym), 'NULL') || ',   "vendorname" = ' || coalesce(quote_literal(NEW.vendorname), 'NULL') || ',   "vendoralternatename" = ' || coalesce(quote_literal(NEW.vendoralternatename), 'NULL') || ',   "vendorlegalorganizationname" = ' || coalesce(quote_literal(NEW.vendorlegalorganizationname), 'NULL') || ',   "vendordoingasbusinessname" = ' || coalesce(quote_literal(NEW.vendordoingasbusinessname), 'NULL') || ',   "divisionname" = ' || coalesce(quote_literal(NEW.divisionname), 'NULL') || ',   "divisionnumberorofficecode" = ' || coalesce(quote_literal(NEW.divisionnumberorofficecode), 'NULL') || ',   "vendorenabled" = ' || coalesce(quote_literal(NEW.vendorenabled), 'NULL') || ',   "vendorlocationdisableflag" = ' || coalesce(quote_literal(NEW.vendorlocationdisableflag), 'NULL') || ',   "ccrexception" = ' || coalesce(quote_literal(NEW.ccrexception), 'NULL') || ',   "streetaddress" = ' || coalesce(quote_literal(NEW.streetaddress), 'NULL') || ',   "streetaddress2" = ' || coalesce(quote_literal(NEW.streetaddress2), 'NULL') || ',   "streetaddress3" = ' || coalesce(quote_literal(NEW.streetaddress3), 'NULL') || ',   "city" = ' || coalesce(quote_literal(NEW.city), 'NULL') || ',   "state" = ' || coalesce(quote_literal(NEW.state), 'NULL') || ',   "zipcode" = ' || coalesce(quote_literal(NEW.zipcode), 'NULL') || ',   "vendorcountrycode" = ' || coalesce(quote_literal(NEW.vendorcountrycode), 'NULL') || ',   "vendor_state_code" = ' || coalesce(quote_literal(NEW.vendor_state_code), 'NULL') || ',   "vendor_cd" = ' || coalesce(quote_literal(NEW.vendor_cd), 'NULL') 

|| ',   "congressionaldistrict" = ' || coalesce(quote_literal(NEW.congressionaldistrict), 'NULL') || ',   "vendorsitecode" = ' || coalesce(quote_literal(NEW.vendorsitecode), 'NULL') || ',   "vendoralternatesitecode" = ' || coalesce(quote_literal(NEW.vendoralternatesitecode), 'NULL') || ',   "dunsnumber" = ' || coalesce(quote_literal(NEW.dunsnumber), 'NULL') || ',   "parentdunsnumber" = ' || coalesce(quote_literal(NEW.parentdunsnumber), 'NULL') || ',   "phoneno" = ' || coalesce(quote_literal(NEW.phoneno), 'NULL') || ',   "faxno" = ' || coalesce(quote_literal(NEW.faxno), 'NULL') || ',   "registrationdate" = ' || coalesce(quote_literal(NEW.registrationdate), 'NULL') || ',   "renewaldate" = ' || coalesce(quote_literal(NEW.renewaldate), 'NULL') || ',   "mod_parent" = ' || coalesce(quote_literal(NEW.mod_parent), 'NULL') || ',   "locationcode" = ' || coalesce(quote_literal(NEW.locationcode), 'NULL') || ',   "statecode" = ' || coalesce(quote_literal(NEW.statecode), 'NULL') || ',   "pop_state_code" = ' || coalesce(quote_literal(NEW.pop_state_code), 'NULL') || ',   "placeofperformancecountrycode" = ' || coalesce(quote_literal(NEW.placeofperformancecountrycode), 'NULL') || ',   "placeofperformancezipcode" = ' || coalesce(quote_literal(NEW.placeofperformancezipcode), 'NULL') || ',   "pop_cd" = ' || coalesce(quote_literal(NEW.pop_cd), 'NULL') || ',   "placeofperformancecongressionaldistrict" = ' || coalesce(quote_literal(NEW.placeofperformancecongressionaldistrict), 'NULL') || ',   "psc_cat" = ' || coalesce(quote_literal(NEW.psc_cat), 'NULL') || ',   "productorservicecode" = ' || coalesce(quote_literal(NEW.productorservicecode), 'NULL') || ',   "systemequipmentcode" = ' || coalesce(quote_literal(NEW.systemequipmentcode), 'NULL') || ',   "claimantprogramcode" = ' || coalesce(quote_literal(NEW.claimantprogramcode), 'NULL') || ',   "principalnaicscode" = ' || coalesce(quote_literal(NEW.principalnaicscode), 'NULL') || ',   "informationtechnologycommercialitemcategory" = ' || coalesce(quote_literal(NEW.informationtechnologycommercialitemcategory), 'NULL') || ',   "gfe_gfp" = ' || coalesce(quote_literal(NEW.gfe_gfp), 'NULL') || ',   "useofepadesignatedproducts" = ' || coalesce(quote_literal(NEW.useofepadesignatedproducts), 'NULL') || ',   "recoveredmaterialclauses" = ' || coalesce(quote_literal(NEW.recoveredmaterialclauses), 'NULL') || ',   "seatransportation" = ' || coalesce(quote_literal(NEW.seatransportation), 'NULL') || ',   "contractbundling" = ' || coalesce(quote_literal(NEW.contractbundling), 'NULL') || ',   "consolidatedcontract" = ' || coalesce(quote_literal(NEW.consolidatedcontract), 'NULL') || ',   "countryoforigin" = ' || coalesce(quote_literal(NEW.countryoforigin), 'NULL') || ',   "placeofmanufacture" = ' || coalesce(quote_literal(NEW.placeofmanufacture), 'NULL') || ',   "manufacturingorganizationtype" = ' 

|| coalesce(quote_literal(NEW.manufacturingorganizationtype), 'NULL') || ',   "agencyid" = ' || coalesce(quote_literal(NEW.agencyid), 'NULL') || ',   "piid" = ' || coalesce(quote_literal(NEW.piid), 'NULL') || ',   "modnumber" = ' || coalesce(quote_literal(NEW.modnumber), 'NULL') || ',   "transactionnumber" = ' || coalesce(quote_literal(NEW.transactionnumber), 'NULL') || ',   "fiscal_year" = ' || coalesce(quote_literal(NEW.fiscal_year), 'NULL') || ',   "idvagencyid" = ' || coalesce(quote_literal(NEW.idvagencyid), 'NULL') || ',   "idvpiid" = ' || coalesce(quote_literal(NEW.idvpiid), 'NULL') || ',   "idvmodificationnumber" = ' || coalesce(quote_literal(NEW.idvmodificationnumber), 'NULL') || ',   "solicitationid" = ' || coalesce(quote_literal(NEW.solicitationid), 'NULL') || ',   "extentcompeted" = ' || coalesce(quote_literal(NEW.extentcompeted), 'NULL') || ',   "reasonnotcompeted" = ' || coalesce(quote_literal(NEW.reasonnotcompeted), 'NULL') || ',   "numberofoffersreceived" = ' || coalesce(quote_literal(NEW.numberofoffersreceived), 'NULL') || ',   "commercialitemacquisitionprocedures" = ' || coalesce(quote_literal(NEW.commercialitemacquisitionprocedures), 'NULL') || ',   "commercialitemtestprogram" = ' || coalesce(quote_literal(NEW.commercialitemtestprogram), 'NULL') || ',   "smallbusinesscompetitivenessdemonstrationprogram" = ' || coalesce(quote_literal(NEW.smallbusinesscompetitivenessdemonstrationprogram), 'NULL') || ',   "a76action" = ' || coalesce(quote_literal(NEW.a76action), 'NULL') || ',   "competitiveprocedures" = ' || coalesce(quote_literal(NEW.competitiveprocedures), 'NULL') || ',   "solicitationprocedures" = ' || coalesce(quote_literal(NEW.solicitationprocedures), 'NULL') || ',   "typeofsetaside" = ' || coalesce(quote_literal(NEW.typeofsetaside), 'NULL') || ',   "localareasetaside" = ' || coalesce(quote_literal(NEW.localareasetaside), 'NULL') || ',   "evaluatedpreference" = ' || coalesce(quote_literal(NEW.evaluatedpreference), 'NULL') || ',   "fedbizopps" = ' || coalesce(quote_literal(NEW.fedbizopps), 'NULL') || ',   "research" = ' || coalesce(quote_literal(NEW.research), 'NULL') || ',   "statutoryexceptiontofairopportunity" = ' || coalesce(quote_literal(NEW.statutoryexceptiontofairopportunity), 'NULL') || ',   "organizationaltype" = ' || coalesce(quote_literal(NEW.organizationaltype), 'NULL') || ',   "numberofemployees" = ' || coalesce(quote_literal(NEW.numberofemployees), 'NULL') || ',   "annualrevenue" = ' || coalesce(quote_literal(NEW.annualrevenue), 'NULL') || ',   "firm8aflag" = ' || coalesce(quote_literal(NEW.firm8aflag), 'NULL') || ',   "hubzoneflag" = ' || coalesce(quote_literal(NEW.hubzoneflag), 'NULL') 

|| ',   "sdbflag" = ' || coalesce(quote_literal(NEW.sdbflag), 'NULL') || ',   "shelteredworkshopflag" = ' || coalesce(quote_literal(NEW.shelteredworkshopflag), 'NULL') || ',   "hbcuflag" = ' || coalesce(quote_literal(NEW.hbcuflag), 'NULL') || ',   "educationalinstitutionflag" = ' || coalesce(quote_literal(NEW.educationalinstitutionflag), 'NULL') || ',   "womenownedflag" = ' || coalesce(quote_literal(NEW.womenownedflag), 'NULL') || ',   "veteranownedflag" = ' || coalesce(quote_literal(NEW.veteranownedflag), 'NULL') || ',   "srdvobflag" = ' || coalesce(quote_literal(NEW.srdvobflag), 'NULL') || ',   "localgovernmentflag" = ' || coalesce(quote_literal(NEW.localgovernmentflag), 'NULL') || ',   "minorityinstitutionflag" = ' || coalesce(quote_literal(NEW.minorityinstitutionflag), 'NULL') || ',   "aiobflag" = ' || coalesce(quote_literal(NEW.aiobflag), 'NULL') || ',   "stategovernmentflag" = ' || coalesce(quote_literal(NEW.stategovernmentflag), 'NULL') || ',   "federalgovernmentflag" = ' || coalesce(quote_literal(NEW.federalgovernmentflag), 'NULL') || ',   "minorityownedbusinessflag" = ' || coalesce(quote_literal(NEW.minorityownedbusinessflag), 'NULL') || ',   "apaobflag" = ' || coalesce(quote_literal(NEW.apaobflag), 'NULL') || ',   "tribalgovernmentflag" = ' || coalesce(quote_literal(NEW.tribalgovernmentflag), 'NULL') || ',   "baobflag" = ' || coalesce(quote_literal(NEW.baobflag), 'NULL') || ',   "naobflag" = ' || coalesce(quote_literal(NEW.naobflag), 'NULL') || ',   "saaobflag" = ' || coalesce(quote_literal(NEW.saaobflag), 'NULL') || ',   "nonprofitorganizationflag" = ' || coalesce(quote_literal(NEW.nonprofitorganizationflag), 'NULL') || ',   "haobflag" = ' || coalesce(quote_literal(NEW.haobflag), 'NULL') || ',   "emergingsmallbusinessflag" = ' || coalesce(quote_literal(NEW.emergingsmallbusinessflag), 'NULL') || ',   "hospitalflag" = ' || coalesce(quote_literal(NEW.hospitalflag), 'NULL') || ',   "contractingofficerbusinesssizedetermination" = ' || coalesce(quote_literal(NEW.contractingofficerbusinesssizedetermination), 'NULL') || ',   "receivescontracts" = ' || coalesce(quote_literal(NEW.receivescontracts), 'NULL') || ',   "receivesgrants" = ' || coalesce(quote_literal(NEW.receivesgrants), 'NULL') || ',   "receivescontractsandgrants" = ' || coalesce(quote_literal(NEW.receivescontractsandgrants), 'NULL') || ',   "walshhealyact" = ' || coalesce(quote_literal(NEW.walshhealyact), 'NULL') || ',   "servicecontractact" = ' || coalesce(quote_literal(NEW.servicecontractact), 'NULL') || ',   "davisbaconact" = ' || coalesce(quote_literal(NEW.davisbaconact), 'NULL') || ',   "clingercohenact" = ' || coalesce(quote_literal(NEW.clingercohenact), 'NULL') || ',   "otherstatutoryauthority" = ' || coalesce(quote_literal(NEW.otherstatutoryauthority), 'NULL') || ',   "interagencycontractingauthority" = ' || coalesce(quote_literal(NEW.interagencycontractingauthority), 'NULL') || ',   "isserviceprovider" = ' || coalesce(quote_literal(NEW.isserviceprovider), 'NULL') ||

    ' WHERE id=' || OLD.id || ' and fiscal_year=' || fy || ';';
    

    EXECUTE statement USING NEW;
    RETURN NEW;
END
$$ LANGUAGE plpgsql;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract_2000'
    AND trigger_name = 'before_update_usaspending_contract_trigger'
) THEN
        CREATE TRIGGER before_update_usaspending_contract_trigger
            BEFORE UPDATE ON usaspending_contract_2000
            FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_update_child();
END IF;
END $$;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract_2001'
    AND trigger_name = 'before_update_usaspending_contract_trigger'
) THEN
        CREATE TRIGGER before_update_usaspending_contract_trigger
            BEFORE UPDATE ON usaspending_contract_2001
            FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_update_child();
END IF;
END $$;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract_2002'
    AND trigger_name = 'before_update_usaspending_contract_trigger'
) THEN
        CREATE TRIGGER before_update_usaspending_contract_trigger
            BEFORE UPDATE ON usaspending_contract_2002
            FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_update_child();
END IF;
END $$;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract_2003'
    AND trigger_name = 'before_update_usaspending_contract_trigger'
) THEN
        CREATE TRIGGER before_update_usaspending_contract_trigger
            BEFORE UPDATE ON usaspending_contract_2003
            FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_update_child();
END IF;
END $$;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract_2004'
    AND trigger_name = 'before_update_usaspending_contract_trigger'
) THEN
        CREATE TRIGGER before_update_usaspending_contract_trigger
            BEFORE UPDATE ON usaspending_contract_2004
            FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_update_child();
END IF;
END $$;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract_2005'
    AND trigger_name = 'before_update_usaspending_contract_trigger'
) THEN
        CREATE TRIGGER before_update_usaspending_contract_trigger
            BEFORE UPDATE ON usaspending_contract_2005
            FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_update_child();
END IF;
END $$;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract_2006'
    AND trigger_name = 'before_update_usaspending_contract_trigger'
) THEN
        CREATE TRIGGER before_update_usaspending_contract_trigger
            BEFORE UPDATE ON usaspending_contract_2006
            FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_update_child();
END IF;
END $$;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract_2007'
    AND trigger_name = 'before_update_usaspending_contract_trigger'
) THEN
        CREATE TRIGGER before_update_usaspending_contract_trigger
            BEFORE UPDATE ON usaspending_contract_2007
            FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_update_child();
END IF;
END $$;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract_2008'
    AND trigger_name = 'before_update_usaspending_contract_trigger'
) THEN
        CREATE TRIGGER before_update_usaspending_contract_trigger
            BEFORE UPDATE ON usaspending_contract_2008
            FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_update_child();
END IF;
END $$;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract_2009'
    AND trigger_name = 'before_update_usaspending_contract_trigger'
) THEN
        CREATE TRIGGER before_update_usaspending_contract_trigger
            BEFORE UPDATE ON usaspending_contract_2009
            FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_update_child();
END IF;
END $$;

