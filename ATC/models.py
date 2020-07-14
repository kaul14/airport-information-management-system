from django.db import models
from django.utils import timezone

# Create your models here.
class AircraftTypeModel(models.Model):
    Type_Indentifier=models.CharField(max_length=50)
    Long_Name=models.CharField(max_length=50)
    Short_Name=models.CharField(max_length=50)
    Seating_Capacity=models.IntegerField()
    Max_Weight=models.CharField(max_length=50)
    Wing_Span=models.CharField(max_length=50)
    Gear_Span=models.CharField(max_length=50)
    helicopter=models.BooleanField(default=False)
    supersonic=models.BooleanField(default=False)
    Remarks=models.TextField(max_length=150)
    #date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'id:{},name:{}'.format(self.id,self.Long_Name)

LT=(('National','National'),('International','International'),('Defense','Defense'))
D=(('Local','Local'),('State','State'))
RT=(('Plains','Plains'),("Hilly","Hilly"),('Island','Island'))
ST=(('Available','Available'),('Unavailable','Unavailable'))
s="Select One"
class NewLocationModel(models.Model):
    Location_Name=models.CharField(max_length=50)
    Location_Code=models.CharField(max_length=50)
    IATA_Code=models.CharField(max_length=50)
    Location_type=models.CharField(choices=LT,max_length=20,default=s)
    Airport_Type=models.CharField(choices=LT,max_length=20,default=s)
    Division=models.CharField(choices=D,max_length=20,default=s)
    Region=models.CharField(choices=RT,max_length=20,default=s)
    Status=models.CharField(choices=ST,max_length=20,default=s)
    TNLC_DISCOUNT=models.BooleanField(default=False)
    ILS=models.BooleanField(default=False)
    Uncontrolled=models.BooleanField(default=False)
    PCM_Seg=models.BooleanField(default=False)
    Address=models.TextField(max_length=150)
    #date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'ID:{},LOCATION NAME:{}'.format(self.id,self.Location_Name)

CAT=(('National','National'),('International','International'))
FF=(('YES','YES'),('NO','NO'))
Agc=(('1','1'),('2','2'),('3','3'))


class NewwOperatorModel(models.Model):
    Operator_Name=models.CharField(max_length=50)
    Operator_Code=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Email=models.EmailField()
    Category=models.CharField(choices=CAT,max_length=20,default=s)
    Free_Facility=models.CharField(choices=FF,max_length=20,default=s)
    Operator_Type=models.CharField(choices=CAT,max_length=20,default=s,primary_key=True)
    ROF=models.CharField(choices=FF,max_length=20,default=s)
    Security_Deposit=models.IntegerField()
    Credit_Facility=models.CharField(choices=FF,max_length=20,default=s)
    PAN_Number=models.CharField(max_length=50)
    TAN_Number=models.CharField(max_length=50)
    AGC=models.CharField(choices=Agc,max_length=20,default=s)
    Scheduled=models.CharField(choices=FF,max_length=20,default=s)
    Service_Tax_Reg_No=models.CharField(max_length=50)
    Counter_Category=models.CharField(choices=Agc,max_length=20,default=s)
    No_of_Counter_Alloted=models.IntegerField(default=0)
    No_of_Own_Counter=models.IntegerField(default=0)
    Monthly_CC_Category=models.CharField(choices=Agc,max_length=20,default=s)
    FAX_NO=models.CharField(max_length=50)
    Contact_Person=models.CharField(max_length=50)
    GSA_Details=models.CharField(max_length=50)
    Use_of_AAI_XRAY=models.BooleanField(default=False)
    Use_of_Common_Counter=models.BooleanField(default=False)
    Use_of_AAI_Housing=models.BooleanField(default=False)
    Use_of_AAI_Parking=models.BooleanField(default=False)
    Aero_Bridge=models.BooleanField(default=False)
    Include_PSF_in_charge_Bill=models.BooleanField(default=False)
    Common_Billing_For_SN=models.BooleanField(default=False)
    Common_Charges_for_All_Aircrafts=models.BooleanField(default=False)
    Applicable_for_PSF_Discount=models.BooleanField(default=False)
    Applicable_for_UDF_Discount=models.BooleanField(default=False)
    Use_Ambulift=models.BooleanField(default=False)
    Address=models.TextField(max_length=150)
    #date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'ID:{},OPERATOR NAME:{}'.format(self.Operator_Code,self.Operator_Name)


Air_type=(('Airbus A320','Airbus A320'),('Boeing 737-800','Boeing 737-800'),('Airbus A321','Airbus A321'),
('Boeing 777-300ER','Boeing 777-300ER'))
Reg_t=(('Local','Local'),('National','National'),('International','International'))

class NewAircraftModel(models.Model):
    Registration_Number=models.CharField(primary_key=True,max_length=50)
    Max_Weight=models.CharField(max_length=50)
    Aircraft_Type=models.CharField(choices=Air_type,max_length=20,default=s)
    Registration_Type=models.CharField(choices=Reg_t,max_length=20,default=s)
    Operator_Code=models.CharField(max_length=50)
    Seating_capacity=models.IntegerField()
    LCN=models.CharField(max_length=50)
    Height=models.DecimalField(max_digits=10,decimal_places=5)
    Owner_Name=models.CharField(max_length=50)
    Leased_From=models.CharField(max_length=50)
    Valid_From=models.DateField()
    Valid_Till=models.DateField()
    Reference_Number=models.CharField(max_length=50)
    Cargo=models.BooleanField(default=False)
    Supersonic=models.BooleanField(default=False)
    File_Upload=models.FileField()
    Remarks=models.TextField(max_length=150)
    #date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'REGISTRATION NUMBER:{},OPERATOR_CODE :{}'.format(self.Registration_Number,self.Operator_Code)

NOF=(('Buoyant flight','Buoyant flight'),('Aerodynamic flight','Aerodynamic flight'))
Sch_C=(('Passenger','Passenger'),('Cargo','Cargo'))
Sch_T=(('Long','Long'),('Short','Short'))

class NewDepartureModel(models.Model):
    Nature_Of_Flight=models.CharField(choices=NOF,max_length=20,default=s)
    Schedule_Category=models.CharField(choices=Sch_C,max_length=20,default=s)
    Schedule_Type=models.CharField(choices=Sch_T,max_length=20,default=s)
    Aircraft_Type=models.CharField(choices=Air_type,max_length=20,default=s)
    RCS_Flight=models.CharField(choices=FF,max_length=20,default=s)
    Valid_From=models.DateField()
    Valid_Till=models.DateField()
    Flight_Number=models.CharField(max_length=50,primary_key=True)
    Operator_Code=models.CharField(max_length=50)
    Arrival_Location=models.CharField(max_length=50)
    Flight_Status=models.CharField(max_length=50,null=True)
    Scheduled_Time=models.TimeField()
    Route=models.CharField(max_length=50)
    Mon=models.BooleanField(default=False)
    Tue=models.BooleanField(default=False)
    Wed=models.BooleanField(default=False)
    Thu=models.BooleanField(default=False)
    Fri=models.BooleanField(default=False)
    Sat=models.BooleanField(default=False)
    Sun=models.BooleanField(default=False)
    #date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'FLIGHT NUMBER :{},OPERATOR_CODE :{}'.format(self.Flight_Number,self.Operator_Code)

class NewArrivalModel(models.Model):
    Nature_Of_Flight=models.CharField(choices=NOF,max_length=20,default=s)
    Schedule_Category=models.CharField(choices=Sch_C,max_length=20,default=s)
    Schedule_Type=models.CharField(choices=Sch_T,max_length=20,default=s)
    Aircraft_Type=models.CharField(choices=Air_type,max_length=20,default=s)
    RCS_Flight=models.CharField(choices=FF,max_length=20,default=s)
    Valid_From=models.DateField()
    Valid_Till=models.DateField()
    Flight_Number=models.CharField(max_length=50,primary_key=True)
    Operator_Code=models.CharField(max_length=50)
    Departure_Location=models.CharField(max_length=50)
    Scheduled_Time=models.TimeField()
    Flight_Status=models.CharField(max_length=50,null=True)
    Route=models.CharField(max_length=50)
    Mon=models.BooleanField(default=False)
    Tue=models.BooleanField(default=False)
    Wed=models.BooleanField(default=False)
    Thu=models.BooleanField(default=False)
    Fri=models.BooleanField(default=False)
    Sat=models.BooleanField(default=False)
    Sun=models.BooleanField(default=False)

    #date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'FLIGHT NUMBER :{},OPERATOR_CODE :{}'.format(self.Flight_Number,self.Operator_Code)
