from localflavor.us.models import USStateField
from django.db import models
import federal_spending.usaspending
from django.db import connection

class ContractManager(models.Manager):
    def get_table_for(self, fiscal_year):
        table = 'usaspending_contract_{0}'.format(fiscal_year)
        return table

    def in_fiscal_year(self, fiscal_year):
        self.fiscal_year = fiscal_year
        self.model._meta.db_table = self.get_table_for(fiscal_year)
        return self

class Contract(models.Model):

    objects = ContractManager()

    unique_transaction_id = models.CharField(max_length=32)
    transaction_status = models.CharField(max_length=32, blank=True)
    obligatedamount = models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=True, null=True)
    baseandexercisedoptionsvalue = models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=True, null=True)
    baseandalloptionsvalue = models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=True, null=True)
    maj_agency_cat = models.CharField(max_length=2, blank=True)
    mod_agency = models.CharField(max_length=4, blank=True)
    maj_fund_agency_cat = models.CharField(max_length=2, blank=True)
    contractingofficeagencyid = models.CharField(max_length=4, blank=True)
    contractingofficeid = models.CharField(max_length=6, blank=True)
    fundingrequestingagencyid = models.CharField(max_length=4, blank=True)
    fundingrequestingofficeid = models.CharField(max_length=6, blank=True)
    fundedbyforeignentity = models.CharField(max_length=21, blank=True)
    signeddate = models.DateField(blank=True, null=True)
    effectivedate = models.DateField(blank=True, null=True)
    currentcompletiondate = models.DateField(blank=True, null=True)
    ultimatecompletiondate = models.DateField(blank=True, null=True)
    lastdatetoorder = models.CharField(max_length=32, blank=True)
    contractactiontype = models.CharField(max_length=4, blank=True)
    reasonformodification = models.CharField(max_length=1, blank=True)
    typeofcontractpricing = models.CharField(max_length=2, blank=True)
    priceevaluationpercentdifference = models.CharField(max_length=100, blank=True)
    subcontractplan = models.CharField(max_length=1, blank=True)
    lettercontract = models.CharField(max_length=1, blank=True)
    multiyearcontract = models.NullBooleanField()
    performancebasedservicecontract = models.CharField(max_length=1, blank=True)
    majorprogramcode = models.CharField(max_length=100, blank=True)
    contingencyhumanitarianpeacekeepingoperation = models.CharField(max_length=1, blank=True)
    contractfinancing = models.CharField(max_length=1, blank=True)
    costorpricingdata = models.CharField(max_length=1, blank=True)
    costaccountingstandardsclause = models.CharField(max_length=1, blank=True)
    descriptionofcontractrequirement = models.TextField(blank=True, null=True)
    purchasecardaspaymentmethod = models.NullBooleanField()
    numberofactions = models.IntegerField(null=True)
    nationalinterestactioncode = models.CharField(max_length=64, blank=True)
    progsourceagency = models.CharField(max_length=2, blank=True)
    progsourceaccount = models.CharField(max_length=4, blank=True)
    progsourcesubacct = models.CharField(max_length=3, blank=True)
    account_title = models.CharField(max_length=255, blank=True)
    rec_flag = models.NullBooleanField()
    typeofidc = models.CharField(max_length=41, blank=True)
    multipleorsingleawardidc = models.CharField(max_length=1, blank=True)
    programacronym = models.CharField(max_length=32, blank=True)
    vendorname = models.CharField(max_length=400, blank=True)
    vendoralternatename = models.CharField(max_length=400, blank=True)
    vendorlegalorganizationname = models.CharField(max_length=400, blank=True)
    vendordoingasbusinessname = models.CharField(max_length=400, blank=True)
    divisionname = models.CharField(max_length=400, blank=True)
    divisionnumberorofficecode = models.CharField(max_length=10, blank=True)
    vendorenabled = models.CharField(max_length=10, blank=True)
    vendorlocationdisableflag = models.NullBooleanField()
    ccrexception = models.CharField(max_length=255, blank=True)
    streetaddress = models.CharField(max_length=400, blank=True)
    streetaddress2 = models.CharField(max_length=400, blank=True)
    streetaddress3 = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=35, blank=True)
    state = models.CharField(max_length=35, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    vendorcountrycode = models.CharField(max_length=100, blank=True)
    vendor_state_code = models.CharField(max_length=32, blank=True)
    vendor_cd = models.CharField(max_length=37, blank=True)
    congressionaldistrict = models.CharField(max_length=37, blank=True)
    vendorsitecode = models.CharField(max_length=16, blank=True)
    vendoralternatesitecode = models.CharField(max_length=20, blank=True)
    dunsnumber = models.CharField(max_length=13, blank=True)
    parentdunsnumber = models.CharField(max_length=13, blank=True)
    phoneno = models.CharField(max_length=20, blank=True)
    faxno = models.CharField(max_length=20, blank=True)
    registrationdate = models.DateField(blank=True, null=True)
    renewaldate = models.DateField(blank=True, null=True)
    mod_parent = models.CharField(max_length=100, blank=True)
    locationcode = models.CharField(max_length=5, blank=True)
    statecode = USStateField(blank=True)
    pop_state_code = USStateField(blank=True)
    placeofperformancecountrycode = models.CharField(max_length=3, blank=True)
    placeofperformancezipcode = models.CharField(max_length=10, blank=True)
    pop_cd = models.CharField(max_length=4, blank=True)
    placeofperformancecongressionaldistrict = models.CharField(max_length=6, blank=True)
    psc_cat = models.CharField(max_length=2, blank=True)
    productorservicecode = models.CharField(max_length=4, blank=True)
    systemequipmentcode = models.CharField(max_length=4, blank=True)
    claimantprogramcode = models.CharField(max_length=3, blank=True)
    principalnaicscode = models.CharField(max_length=6, blank=True)
    informationtechnologycommercialitemcategory = models.CharField(max_length=1, blank=True)
    gfe_gfp = models.NullBooleanField()
    useofepadesignatedproducts = models.CharField(max_length=1, blank=True)
    recoveredmaterialclauses = models.CharField(max_length=1, blank=True)
    seatransportation = models.CharField(max_length=1, blank=True)
    contractbundling = models.CharField(max_length=1, blank=True)
    consolidatedcontract = models.NullBooleanField()
    countryoforigin = models.CharField(max_length=3, blank=True)
    placeofmanufacture = models.CharField(max_length=1, blank=True)
    manufacturingorganizationtype = models.CharField(max_length=4, blank=True)
    agencyid = models.CharField(max_length=4, blank=True)
    piid = models.CharField(max_length=50, blank=True)
    modnumber = models.CharField(max_length=25, blank=True)
    transactionnumber = models.CharField(max_length=6, blank=True)
    fiscal_year = models.IntegerField(null=True)
    idvagencyid = models.CharField(max_length=4, blank=True)
    idvpiid = models.CharField(max_length=50, blank=True)
    idvmodificationnumber  = models.CharField(max_length=25, blank=True)
    solicitationid = models.CharField(max_length=25, blank=True)
    extentcompeted = models.CharField(max_length=3, blank=True)
    reasonnotcompeted = models.CharField(max_length=3, blank=True)
    numberofoffersreceived = models.IntegerField(null=True)
    commercialitemacquisitionprocedures = models.CharField(max_length=1, blank=True)
    commercialitemtestprogram = models.NullBooleanField()
    smallbusinesscompetitivenessdemonstrationprogram = models.NullBooleanField()
    a76action = models.NullBooleanField()
    competitiveprocedures = models.CharField(max_length=3, blank=True)
    solicitationprocedures = models.CharField(max_length=5, blank=True)
    typeofsetaside = models.CharField(max_length=10, blank=True)
    localareasetaside = models.CharField(max_length=32, blank=True)
    evaluatedpreference = models.CharField(max_length=6, blank=True)
    fedbizopps = models.CharField(max_length=32, blank=True)
    research = models.CharField(max_length=3, blank=True)
    statutoryexceptiontofairopportunity = models.CharField(max_length=4, blank=True)
    organizationaltype = models.CharField(max_length=64, blank=True)
    numberofemployees = models.IntegerField(null=True)
    annualrevenue = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    firm8aflag = models.NullBooleanField()
    hubzoneflag = models.NullBooleanField()
    sdbflag = models.NullBooleanField()
    shelteredworkshopflag = models.NullBooleanField()
    hbcuflag = models.NullBooleanField()
    educationalinstitutionflag = models.NullBooleanField()
    womenownedflag = models.NullBooleanField()
    veteranownedflag = models.NullBooleanField()
    srdvobflag = models.NullBooleanField()
    localgovernmentflag = models.NullBooleanField()
    minorityinstitutionflag = models.NullBooleanField()
    aiobflag = models.CharField(max_length=1, blank=True)
    stategovernmentflag = models.NullBooleanField()
    federalgovernmentflag = models.NullBooleanField()
    minorityownedbusinessflag = models.NullBooleanField()
    apaobflag = models.NullBooleanField()
    tribalgovernmentflag = models.NullBooleanField()
    baobflag = models.NullBooleanField()
    naobflag = models.NullBooleanField()
    saaobflag = models.NullBooleanField()
    nonprofitorganizationflag = models.NullBooleanField()
    haobflag = models.NullBooleanField()
    emergingsmallbusinessflag = models.NullBooleanField()
    hospitalflag = models.NullBooleanField()
    contractingofficerbusinesssizedetermination = models.CharField(max_length=1, blank=True)
    receivescontracts = models.CharField(max_length=1, blank=True)
    receivesgrants = models.CharField(max_length=1, blank=True)
    receivescontractsandgrants = models.CharField(max_length=1, blank=True)
    walshhealyact = models.NullBooleanField()
    servicecontractact = models.NullBooleanField()
    davisbaconact = models.NullBooleanField()
    clingercohenact = models.NullBooleanField()
    otherstatutoryauthority = models.TextField(blank=True, null=True)
    interagencycontractingauthority = models.CharField(max_length=1, blank=True)
    isserviceprovider = models.NullBooleanField()
    
    agency_name = models.CharField(max_length=255, blank=True)
    contracting_agency_name = models.CharField(max_length=255, blank=True)
    requesting_agency_name = models.CharField(max_length=255, blank=True)
    imported_on = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        Contract.objects.in_fiscal_year(self.fiscal_year)
        super(Contract, self).save()

    def delete(self, *args, **kwargs):
        Contract.objects.in_fiscal_year(self.fiscal_year)
        super(Contract, self).delete()

RECORD_TYPES = (
    ('1', "County aggregate reporting"),
    ('2', "Action-by-action reporting"),
)

ACTION_TYPES = (
    ('A', 'New assistance action'),
    ('B', 'Continuation'),
    ('C', 'Revision'),
    ('D', 'Funding adjustment to completed project'),
)

RECIPIENT_TYPES = (
    ('00', 'State government'),
    ('01', 'County government'),
    ('02', 'City or township government'),
    ('03', '03'),
    ('04', 'Special district government'),
    ('05', 'Independent school district'),
    ('06', 'State controlled institution of higher education'),
    ('07', '07'),
    ('11', 'Indian tribe'),
    ('12', 'Other nonprofit'),
    ('20', 'Private higher education'),
    ('21', 'individual'),
    ('22', 'Profit organization'),
    ('23', 'Small business'),
    ('25', 'Other'),
    ('88', '88'),
    ('90', '90'),
)

RECIPIENT_CATEGORIES = (
    ('f', 'For Profit'),
    ('g', 'Government'),
    ('h', 'Higher Education'),
    ('i', 'Individual'),
    ('n', 'Nonprofit'),
    ('o', 'Other'),
)

ASSISTANCE_TYPES = (
    ('00', '00'),
    ('02', 'Block grant (A)'),
    ('03', 'Formula grant (A)'),
    ('04', 'Project grant (B)'),
    ('05', 'Cooperative agreement (B)'),
    ('06', 'Direct payment for specified use, as a subsidy or other non-reimbursable direct financial aid (C)'),
    ('07', 'Direct loan (D)'),
    ('08', 'Guaranteed/insured loan (F)'),
    ('09', 'Insurance (G)'),
    ('0E', '0E'),
    ('10', 'Direct payment with unrestricted use (D)'),
    ('11', 'Other reimbursable, contingent, intangible or indirect financial assistance'),
    ('25', '25'),
    ('99', '99'),
)

ASSISTANCE_CATEGORIES = (
    ('d', 'Direct Payments'),
    ('g', 'Grants and Cooperative Agreements'),
    ('i', 'Insurance'),
    ('l', 'Loans'),
    ('o', 'Other'),
)

CORRECTIONS = (
    ('0', ''),
    ('2', ''),
    ('5', ''),
    ('6', ''),
    ('B', ''),
    ('C', ''),
    ('F', ''),
    ('L', ''),
    ('_', ''),
)

BFIS = (
    ('000', ''),
    ('0NO', ''),
    ('NON', ''),
    ('REC', ''),
)

AGENCY_CATEGORIES = (
    ('12', ''),
    ('13', ''),
    ('14', ''),
    ('15', ''),
    ('16', ''),
    ('19', ''),
    ('20', ''),
    ('24', ''),
    ('28', ''),
    ('31', ''),
    ('36', ''),
    ('49', ''),
    ('68', ''),
    ('69', ''),
    ('70', ''),
    ('72', ''),
    ('73', ''),
    ('75', ''),
    ('80', ''),
    ('86', ''),
    ('89', ''),
    ('91', ''),
    ('97', ''),
    ('ot', ''),
)

class GrantManager(models.Manager):
    def get_table_for(self, fiscal_year):
        table = 'usaspending_grant_{0}'.format(fiscal_year)
        return table

    def in_fiscal_year(self, fiscal_year):
        self.fiscal_year = fiscal_year
        self.model._meta.db_table = self.get_table_for(fiscal_year)
        return self


class Grant(models.Model):

    objects = GrantManager()

    imported_on = models.DateField(auto_now_add=True)
    fiscal_year = models.IntegerField()
    record_type = models.CharField(max_length=1, blank=True, choices=RECORD_TYPES)
    rec_flag = models.NullBooleanField(blank=True)
    cfda_program_num = models.CharField(max_length=8, blank=True)
    cfda_program_title = models.CharField(max_length=255, blank=True)
    sai_number = models.CharField(max_length=20, blank=True)
    account_title = models.CharField(max_length=100, blank=True)
    recipient_name = models.CharField(max_length=100, blank=True)
    recipient_city_name = models.CharField(max_length=21, blank=True)
    recipient_city_code = models.CharField(max_length=5, blank=True)
    recipient_county_name = models.CharField(max_length=21, blank=True)
    recipient_county_code = models.CharField(max_length=3, blank=True)
    recipient_state_code = USStateField(blank=True)
    recipient_zip = models.CharField(max_length=9, blank=True)
    recipient_country_code = models.CharField(max_length=3, blank=True)
    recipient_cd = models.CharField(max_length=4, blank=True)
    recipient_type = models.CharField(max_length=2, blank=True, choices=RECIPIENT_TYPES)
    recip_cat_type = models.CharField(max_length=1, blank=True, choices=RECIPIENT_CATEGORIES)
    receip_addr1 = models.CharField(max_length=100, blank=True)
    receip_addr2 = models.CharField(max_length=100, blank=True)
    receip_addr3 = models.CharField(max_length=100, blank=True)
    duns_no = models.CharField(max_length=13, blank=True)
    obligation_action_date = models.DateField(blank=True, null=True)
    action_type = models.CharField(max_length=1, blank=True, choices=ACTION_TYPES)
    agency_name = models.CharField(max_length=72, blank=True)
    agency_code = models.CharField(max_length=4, blank=True)
    maj_agency_cat = models.CharField(max_length=2, blank=True)
    federal_award_id = models.CharField(max_length=16, blank=True)
    federal_award_mod = models.CharField(max_length=4, blank=True)
    fed_funding_amount = models.BigIntegerField(blank=True, default=0)
    non_fed_funding_amount = models.BigIntegerField(blank=True, default=0)
    total_funding_amount = models.BigIntegerField(blank=True, default=0)
    face_loan_guran = models.BigIntegerField(blank=True, default=0)
    orig_sub_guran = models.BigIntegerField(blank=True, default=0)
    assistance_type = models.CharField(max_length=2, blank=True, choices=ASSISTANCE_TYPES)
    asst_cat_type = models.CharField(max_length=1, blank=True, choices=ASSISTANCE_CATEGORIES)
    correction_late_ind = models.CharField(max_length=1, blank=True, choices=CORRECTIONS)
    principal_place_code = models.CharField(max_length=7, blank=True)
    principal_place_state = models.CharField(max_length=64, blank=True)
    principal_place_state_code = USStateField(blank=True)
    principal_place_cc = models.CharField(max_length=25, blank=True)
    principal_place_zip = models.CharField(max_length=9, blank=True)
    principal_place_cd = models.CharField(max_length=4, blank=True)
    project_description = models.CharField(max_length=255, blank=True)
    progsrc_agen_code = models.CharField(max_length=2, blank=True)
    progsrc_acnt_code = models.CharField(max_length=4, blank=True)
    progsrc_subacnt_code = models.CharField(max_length=3, blank=True)
    uri = models.CharField(max_length=70, blank=True)
    duns_conf_code = models.CharField(max_length=2, blank=True)
    ending_date = models.DateField(blank=True, null=True)
    fyq = models.CharField(max_length=10, blank=True)
    fyq_correction = models.CharField(max_length=5, blank=True)
    starting_date = models.DateField(blank=True, null=True)
    transaction_status = models.CharField(max_length=32, blank=True)
    unique_transaction_id = models.CharField(max_length=32)
    
    
    def save(self, *args, **kwargs):
        Grant.objects.in_fiscal_year(self.fiscal_year)
        super(Grant, self).save()

    def delete(self, *args, **kwargs):
        Grant.objects.in_fiscal_year(self.fiscal_year)
        super(Grant, self).delete()

    class Meta:
        ordering = ('fiscal_year','id')
    
    def __unicode__(self):
        return u"%s %s" % (self.fiscal_year, self.project_description)
