# DataProject2

## Process Description & Deployment Strategy
All codes can be found in app.py. First, I created an MongoDB to store the data. 
Then, I used Chalice to create a project that run the Lambda function every minute for one hour. 
The Lambda function makes requests to the API and writes the response Json to MongoDB. 
The Lambda function will stop putting the data into MongoDB once the time is greater than "2021-05-08 03:05:01" utc time, which will be exactly 1 hour from the current running time;

## Code Explanation 

### app.py
Line 1-6: The code first import packages into Python for later use.
 
Line 10-12: Then it connect to MongoDB. 

Line 14: Register as a Chalice project. 

Line 16-23: Create a Lambda function that runs periodically.
If the time is greater than 1 hour, it will stop putting the data into MongoDB;
Otherwise, it will update the data in MongoDB every minute. 

### ana.py
Line 1- 4: The code first import packages into Python for later use.

Line 7-10: Then it connects to MongoDB. 

Line 12-19: Append new values of factor and PI for each minute to separate lists. 

Line 21-29: Create side by side time series plots for data analysis purpose.

## Data Patterns & Explanation
The values of factor and PI seem to have positive relationship. 
Both values of factor and PI reach to the highest point around 30 minutes.
The value of factor reaches to the highest point earlier than that of PI. The values of factors to the 1/3 power are always an integer, which starting from 29 and increase by 1 every minute to 59.
The the integer start from 1 to 27.  
The values of PI changes more dramatically around 31 to 32 minutes (when factor equals to 1), but basically remain otherwise.
The values of factor increase gradually from time 0 to 32, and then decrease significantly afterward at the 32 minutes, and then increase gradually to 20000.   
One possible explanation is that once the values of factor and PI are correlated. 
Once the value of factor reaches at a value of 1, the value of PI increase to a value of 4.

## Screenshot of the Database Table
![Mongodb Data Screenshot](https://github.com/xinyiyu18/DataProject2/blob/main/DataProject2.png?raw=true)

## Data Analysis Plot
![Mongodb Data Screenshot](https://github.com/xinyiyu18/DataProject2/blob/main/TimeSeriesPlot.png?raw=true)
