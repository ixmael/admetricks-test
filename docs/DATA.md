# Data 

The RestAPI has only two endopoints:
* Provide a *json* data with:
    * Day: The day of the 
    * Difference: this is a number that represents the difference between the 
    * Difference between the value of USD in Chilean Pesos in a day and the value of USD in Chilean Pesos in the previous day.

* Provide a CSV file with the data:
    * Day
    * Value of the USD in Chilean Pesos
    * Difference between the value of a day and previous day

All the data are filtered by *from* and *to* dates.

The backend application is in **packages/backend** directory. The detailed instructions to run the API are in the **packages/backend/README.md** file.