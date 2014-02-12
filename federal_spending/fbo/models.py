from django.db import models

SOLICITATION_CHOICES = (
    ('PRESOL', 'Presolicitation'),
    ('COMBINE', 'Combined Synopsis/Solicitation'),
    ('SRCSGT', 'Sources Sought'),
    ('SSALE', 'Sale of Surplus Property'),
    ('SNOTE', 'Special Notice'),
    ('FSTD', 'Foreign Government Standard')

)

NOTICE_CHOICES = (
    ('PRESOL', 'Presolicitation'),
    ('COMBINE', 'Combined Synopsis/Solicitation'),
    ('SRCSGT', 'Sources Sought'),
    ('SSALE', 'Sale of Surplus Property'),
    ('SNOTE', 'Special Notice'),
    ('FSTD', 'Foreign Government Standard'),
    ('AWARD', 'Award'),
    ('ITB', 'Intent to Bundle'),
    ('JA', 'Justification and Approval'),
    ('FO', 'Fair Opportunity Limited Sources Justification')

)

JUSTIFICATION_CHOICES = (
    (1, 'Urgency'),
    (2, 'Only One Source (Except Brand Name)'),
    (3, 'Follow-on Delivery Order Following Competitive Initial Order'),
    (4, 'Minimum Guarantee'),
    (5, 'Other Statutory Authority'),
)


class Notice(models.Model):

    notice_id = models.CharField(max_length=255, null=True, blank=True)
    sol_number = models.CharField(max_length=128, null=True, blank=True)
    notice_type = models.CharField(max_length=10, choices=NOTICE_CHOICES, null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    naics = models.IntegerField(max_length=6,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    class_code = models.CharField(max_length=20, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    zip_code = models.CharField(max_length=128, null=True, blank=True)
    setaside = models.CharField(max_length=128, null=True, blank=True)
    contact_name = models.TextField(null=True, blank=True)
    contact_description = models.TextField(null=True, blank=True)
    contact_email = models.TextField(null=True, blank=True)
    notice_title = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    office_address = models.CharField(null=True, blank=True, max_length=255)
    archive_date = models.DateField(null=True, blank=True)
    agency_name = models.TextField(null=True, blank=True)

    
    response_date = models.DateField(null=True, blank=True)
    pop_address = models.TextField(null=True, blank=True)
    pop_zip = models.CharField(max_length=128, null=True, blank=True)
    pop_country = models.CharField(max_length=125, null=True, blank=True)
    recovery_act = models.NullBooleanField(default=False, null=True, blank=True)
    solicitation_type = models.CharField(choices=SOLICITATION_CHOICES, max_length=20, null=True, blank=True)

    award_number = models.CharField(max_length=255, null=True, blank=True)
    award_amount = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    award_amount_text = models.TextField(null=True, blank=True)
    award_date = models.DateField( null=True, blank=True)
    line_number = models.CharField(max_length=255, null=True, blank=True)
    awardee = models.TextField( null=True, blank=True)

    statutory_authority = models.CharField(max_length=255, null=True, blank=True)
    modification_number = models.CharField(max_length=255, null=True, blank=True)

    #Fair Opportunity/Limited Sources Justification Authority
    foja = models.IntegerField(choices=JUSTIFICATION_CHOICES, null=True, blank=True)
    #Delivery/Task Order Number
    order_number = models.CharField(max_length=255, null=True, blank=True)
