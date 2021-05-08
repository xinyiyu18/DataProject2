# DataProject2

## Process Description & Deployment Strategy
First, I created an MongoDB to store the data. 
Then, I used Chalice to create a project that run the Lambda function every minute for one hour. 
The Lambda function makes requests to the API and writes the response Json to MongoDB. 
The Lambda function will stop putting the data into MongoDB once the time is greater than "2021-05-08 03:05:01" utc time, which will be exactly 1 hour from the current running time;

## Code Explanation
Line 1- 6: The code first import packages into Python for later use.
 
Line 10-12: Then it connect to MongoDB. 

Line 14: Register as a Chalice project. 

Line 16-23: Create a Lambda function that runs periodically.
If the time is greater than 1 hour, it will stop puting the data into MongoDB;
Otherwise, it will update the data in MongoDB every minute. 


## Data Patterns & Explanation
The values of factor and PI seem to have positive relationship. 
Both values of factor and PI reach to the highest point around 30 minutes.
The value of factor reaches to the highest point earlier than that of PI. The values of factors to the 1/3 power are always an integer, which starting from 29 and increase by 1 every minute to 59.
The the integer start from 1 to 27.  
The values of PI changes more dramatically around 31 to 32 minutes (when factor equals to 1), but basically remain otherwise.
The values of factor increase gradually from time 0 to 32, and then decrease significantly afterward at the 32 minutes, and then increase gradually to 20000.   
One possible explanation is that once the values of factor and PI are correlated. 
Once the value of factor reaches at a value of 1, the value of PI increase to a value of 4.