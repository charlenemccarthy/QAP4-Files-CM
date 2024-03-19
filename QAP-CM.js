// Description: Sleep-Tite Motel Customer Information
// Author: Charlene McCarthy
// Date: March 14th - 24th 2024

const Customer = {
    Name: "Charlene McCarthy",
    BirthDate: "1993/02/18",
    Gender: "Female",
    RoomPref: ["Early Check-Out", "Extra Bed", "Extra Key", "Late Check-Out"],
    PaymentMethod: "Cash",
    CreditCardNum: "1234123412341234",
    PhoneNum: "7096821392",
    MailingAdd: {
        StreetAdd: "104A Upper Evenings Path",
        City: "Torbay",
        Prov: "NL",
        PostalCode: "A1K1K3",
    },
    StayParameters: {
        CheckInDate: "2024/03/14",
        CheckOutDate: "2024/03/14",
    },
    calculateAge: function() {
        const Today = new Date();
        const BirthDate = new Date(this.BirthDate);
        let Age = Today.getFullYear() - BirthDate.getFullYear();
        const Month = Today.getMonth() - BirthDate.getMonth();
        if (Month < 0 || (Month === 0 && Today.getDate() < BirthDate.getDate())){
            Age--;
        }
        return Age
    },
    calculateStay: function() {
        const CheckIn = new Date(this.StayParameters.CheckInDate);
        const CheckOut = new Date(this.StayParameters.CheckOutDate);
        const DayLength = 1000 * 60 * 60 *24;
        const Duration = Math.abs(CheckOut - CheckIn);
        return Math.ceil(Duration / DayLength)
    },
    describeCustomer: function() {
        const Age = this.AgeCalculations();
        const StayDuration = this.StayCalculations();
        return `
        <ul>
            <li>Customer ${this.Name}</li>
            <li>Age: ${Age}</li>
            <li>Gender: ${this.Gender}</li>
            <li>Address: ${this.MailingAdd.StreetAdd}, ${this.MailingAdd.City}, ${this.MailingAdd.Prov}, ${this.MailingAdd.PostalCode}</li>
            <li>Credit Card Number: ${this.CreditCardNum}</li>
            <li>Check-In: ${this.StayParameters.CheckInDate}</li>
            <li>Check-Out: ${this.StayParameters.CheckOutDate}</li>
            <li>Stay Duration: ${StayDuration} total days</li>
            <li>Room Preferences: ${this.RoomPref.join(", ")}</li>
        </ul>
        `
    }
};

console.log(Customer.CustomerDescription());
