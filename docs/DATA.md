# Data
The data is the *Chilean Pesos* amount of a *United States Dollar* by day from 2020-01-01 to 2023-09-04. I got the historical data from [USD-Chilean Pesos historical data](https://mx.investing.com/currencies/usd-clp-historical-data) and stored in the file **/packages/backend/data/source.csv**.

When the *RestAPI* stars, it reads the file **/packages/backend/data/source.csv** and load data to a variable that is used to filter the data by date.

The *RestAPI* has only two endopoints:
* Provide a *json* data with:
    * Day: The date of the measure.
    * Close: The *CLP* value of a *USD*.
    * Difference: The difference between the *CLP* value of a *USD* in a day and the value of the previous day.

* Provide a CSV file with the data:
    * Day: The date of the measure.
    * Close: The *CLP* value of a *USD*.
    * Difference: The difference between the *CLP* value of a *USD* in a day and the value of the previous day.

The data are filtered by *from* and *to* dates. If you don't provide the filters, this return all data stored in the **/packages/backend/data/source.csv** file.
