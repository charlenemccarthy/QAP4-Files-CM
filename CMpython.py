# Description: To enter and calculate new insurance policy information.
# Author: Charlene McCarthy
# Date(s): March 14th 2024 - March 24th 2024

# Imports

import datetime

# Constants

CLAIM_DATE = datetime.datetime.now()
PREM_RATE = 869.00
ADD_CAR_DISC_RATE = 0.25
EXT_LIB_RATE = 130.00
GLASS_COV_RATE = 86.00
LOAN_CAR_RATE = 58.00
HST_RATE = 0.15
PRO_FEE_RATE = 39.99

Ctr = 1
ClaimInfoLst = []

AddCarDisc = 0


# Functions


def calculate_TotalInsPremium(NumCars, ExtraLib, GlassCov, LoanerCar):

    ExtraLibValue = 0
    GlassCovValue = 0
    LoanerCarValue = 0
    AddCarDisc = 0
    CarTotal = NumCars * PREM_RATE

    if NumCars > 1:
        AddCarDisc = ((NumCars - 1) * PREM_RATE) * ADD_CAR_DISC_RATE

    if ExtraLib == "Y":
        ExtraLibValue = NumCars * EXT_LIB_RATE

    if GlassCov == "Y":
        GlassCovValue = NumCars * GLASS_COV_RATE

    if LoanerCar == "Y":
        LoanerCarValue = NumCars * LOAN_CAR_RATE

    return NumCars, ExtraLibValue, GlassCovValue, LoanerCarValue, AddCarDisc, CarTotal


def calculate_HST(NumCars, ExtraLib, GlassCov, LoanerCar, TotalInsPrem, HST_RATE):

    NumCars, ExtraLibValue, GlassCovValue, LoanerCarValue, AddCarDisc, CarTotal = calculate_TotalInsPremium(NumCars, ExtraLib, GlassCov, LoanerCar)
    

    HST =  TotalInsPrem * HST_RATE
    TotalCharges = TotalInsPrem + HST

    return HST, TotalCharges



def calculate_Payments(NumCars, ExtraLib, GlassCov, LoanerCar, AddCarDisc, TotalInsPrem):

    HST, TotalCharges = calculate_HST(NumCars, ExtraLib, GlassCov, LoanerCar, TotalInsPrem, HST_RATE)
    
    DownPayAmt = 0
    MonthlyPay = 0
    TodayPayment = 0

    if PayMethod == "F":
        TodayPayment = TotalCharges
    
    elif PayMethod == "M":
        MonthlyPay = (TotalCharges + PRO_FEE_RATE) / 8

    elif PayMethod == "D":
        DownPayAmt = float(input("Enter down-payment amount: "))
        MonthlyPay = (TotalCharges + PRO_FEE_RATE - DownPayAmt) / 8
        TodayPayment = DownPayAmt

    return DownPayAmt, MonthlyPay, TodayPayment


# Main Program

    # Inputs

while True:

    Ctr += 1
    ClaimNum = Ctr
    ClaimDate = CLAIM_DATE

    PolicyNum = "1944"
    CustFName = input("Enter the customer's first name or enter END to exit: ").title()
    if CustFName == "END":
        break
    CustLName = input("Enter customer's last name: ").title()
    StAdd = input("Enter customer's street address: ").title()
    City = input("Enter customer's city: ").title()
    ProvLst = ["NL", "NS", "PE", "NB", "QB", "ON", "SK", "MB", "AB", "BC", "NU", "NT", "YT"]
    while True:    
        Prov = input("Enter customer's province: ").upper()
        if Prov == "":
            print("Error, province cannot not be blank.")
        elif Prov not in ProvLst:
            print("Error, province must be a valid province.")
        else:
            break
    PostCode = input("Enter customer's postal code: ").upper()
    PhoNum = input("Enter customer's phone number: ")
    NumCars = int(input("Enter the number of cars being insured: "))
    ExtraLib = input("Does the customer require extra liability, Y/N?: ").upper()
    GlassCov = input("Does the customer require glass coverage, Y/N?: ").upper()
    LoanerCar = input("Does the customer require a loaner car, Y/N?: ").upper()    
    PayMethodLst = ["F", "M", "D"]
    PayMethod = None
    while PayMethod is None:
        PayMethod = input("Is the customer paying in full, monthly, or down-paying (F/M/D)?: ").upper()
        if PayMethod == "":
            print("Error, payment method cannot not be blank.")
            PayMethod = None
        elif PayMethod not in PayMethodLst:
            print("Error, payment method must be F, M or D.")
            PayMethod = None
        else:
            break

    
    # Calculations
    
    NumCars, ExtraLibValue, GlassCovValue, LoanerCarValue, AddCarDisc, CarTotal = calculate_TotalInsPremium(NumCars, ExtraLib, GlassCov, LoanerCar)
    TotalInsPrem = CarTotal - AddCarDisc + ExtraLibValue + GlassCovValue + ExtraLibValue
    HST, TotalCharges = calculate_HST(NumCars, ExtraLib, GlassCov, LoanerCar, TotalInsPrem, HST_RATE)
    DownPayAmt, MonthlyPay, TodayPayment = calculate_Payments(NumCars, ExtraLib, GlassCov, LoanerCar, AddCarDisc, TotalInsPrem)

    # Displays

    CustName = CustFName + " " + CustLName
    Add = City + " " + Prov + " " + PostCode
    ClaimDateDsp = ClaimDate.strftime("%Y/%m/%d")
    ExtraLibDsp = "${:,.2f}".format(ExtraLibValue)
    GlassCovDsp = "${:,.2f}".format(GlassCovValue)
    LoanerCarDsp = "${:,.2f}".format(LoanerCarValue)
    AddCarDiscDsp = "${:,.2f}".format(AddCarDisc)
    HSTDsp = "${:,.2f}".format(HST)
    TotalChargesDsp = "${:,.2f}".format(TotalCharges)
    DownPayDsp = "${:,.2f}".format(DownPayAmt)
    TodayPaymentDsp = "${:,.2f}".format(TodayPayment)
    MonthlyPayDsp = "${:,.2f}".format(MonthlyPay)

    if PayMethod == "F":
        PayMethodDsp = "Full"
    elif PayMethod == "M":
        PayMethodDsp = "Monthly"
    elif PayMethod == "D":
        PayMethodDsp = "Down-payment"

        # Outputs
    print()
    print()
    print("                                One Stop Insurance Company")
    print("                               Insurance Policy Information")
    print("----------------------------------------------------------------------------------------------")
    print(f"                                                             Claim Date: {ClaimDateDsp:>10s}")
    print("----------------------------------------------------------------------------------------------")
    print("      Customer Information:")
    print("----------------------------------------------------------------------------------------------")
    print(f"   Policy Number:                             {PolicyNum:<4s}")
    print(f"   Name:                                      {CustName:<15s}")
    print(f"   Address:                                   {StAdd:<20s}")
    print(f"                                              {Add:<20s}")
    print(f"   Phone Number:                              {PhoNum:<10s}")
    print("----------------------------------------------------------------------------------------------")
    print("      Charges:")
    print("----------------------------------------------------------------------------------------------")
    print(f"   Number of Cars: {NumCars:>2d}")
    print()
    print(f"   Extra Liability:                           {ExtraLibDsp:>9s}")
    print(f"   Glass Coverage:                            {GlassCovDsp:>9s}")
    print(f"   Loaner Cars:                               {LoanerCarDsp:>9s}")
    print(f"   Additional Car Discount:                   {AddCarDiscDsp:>9s}")
    print(f"   HST:                                       {HSTDsp:>9s}")
    print(f"   Total Charges:                             {TotalChargesDsp:>9s}")
    print("----------------------------------------------------------------------------------------------")
    print("      Payment Information:")
    print("----------------------------------------------------------------------------------------------")

    print(f"   Payment Method:                            {PayMethodDsp:>12s}")
    print(f"   Down-Payment:                              {DownPayDsp:>9s}")
    print(f"   Today's Payment:                           {TodayPaymentDsp:>9s}")
    print(f"   Monthly Payment:                           {MonthlyPayDsp:>9s}")
    print("----------------------------------------------------------------------------------------------")
    print()
    if PayMethod == "D" or PayMethod == "M":
        print("                                      Payment Chart")
        print()
        print(f"          Date:                      Monthly Payment:                      Remaining:")
        print("----------------------------------------------------------------------------------------------")
        Remaining = TotalCharges
        for Month in range(1,9):
            PaymentYear = (CLAIM_DATE.year) + ((CLAIM_DATE.month + Month) // 12)
            PaymentMonth = (CLAIM_DATE.month + Month) % 12 + 1
            PaymentDate = CLAIM_DATE.replace(year=PaymentYear, month=PaymentMonth, day=1)
            PaymentDateDsp = PaymentDate.strftime("%Y/%m/%d")
            Remaining -= MonthlyPay
            RemainingDsp = max(Remaining, 0)
            RemainingDsp = "${:,.2f}".format(Remaining)
            print(f"           {PaymentDateDsp}                    {MonthlyPayDsp:>9s}                         {RemainingDsp:>9s}")
        print("----------------------------------------------------------------------------------------------")
    ClaimInfo = (ClaimNum, ClaimDate, TotalCharges)
    ClaimInfoLst.append(ClaimInfo)      
    print("          Claim #:                      Claim Date:                      Claim Amount:")
    print("----------------------------------------------------------------------------------------------")  
    for ClaimNum, ClaimDate, TotalCharges in ClaimInfoLst:
        print(f"           {ClaimNum:>04d}                         {ClaimDateDsp:>10s}                         {TotalChargesDsp:>9s}")
    print()
    print("                            Thank you and have a great day!")
    
# Housekeeping
