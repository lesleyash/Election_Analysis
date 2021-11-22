# Election_Analysis

## Overview of Election Audit
 The Elecion Audit is to analyze the election results by candidate and by country. With the help of the analysis, we can find out the country with largest turnout and the winner of the election.

## Election-Audit Results
- Total Votes cast in this congressional election is 369,711

  ![image](https://user-images.githubusercontent.com/92648619/142820513-95bedd40-2645-4cb2-8544-0ec2b0661dab.png)

- There are three counties in the precinct, Jefferson, Denver and Arapahoe. The number of votes and percentage of each county are shown below:

  ![image](https://user-images.githubusercontent.com/92648619/142820619-1dbe9967-93ac-4847-8890-9f64ef3cbe36.png)
  
- The county with the largest number of votes is Denver. 
  
  ![image](https://user-images.githubusercontent.com/92648619/142820908-ef29998c-c5c0-4e31-b6e7-c836f88db3e9.png)

- Total of three candidates in this election: Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane. Their total votes and percentage of total votes received are shown below:

  ![image](https://user-images.githubusercontent.com/92648619/142820984-16002528-e5b6-4f51-bb57-5bab6d5d1c46.png)

- The winner of the election is Diana DeGette with 72,892 votes or 73.8% percentage of total votes..

  ![image](https://user-images.githubusercontent.com/92648619/142821201-11d26bc1-71af-46b6-8d3f-8203bb00bff0.png)

## Election-Audit Summary: 
### The application of the scripts
The scripts to run the election analysis can be applied to other elections by some modifications.
- The index used in the script to retrive the candidate or country information might need to be updated based on the structure of the file of election data results. The Index is 2 here for candidate name as the name info are in the third column of the data file. 

  ![image](https://user-images.githubusercontent.com/92648619/142822000-b57ffb52-5175-4bfc-8a06-4169e00a4e03.png)

- The path of the original election data need to be updated in order for the script to connect to the correct file
  ![image](https://user-images.githubusercontent.com/92648619/142822591-6df1288b-c38d-4bd0-8639-f8e1594e0f22.png)

- The next() script might be deleted if the data file does not have column headers.
  ![image](https://user-images.githubusercontent.com/92648619/142822533-10624cb8-addf-4413-9774-e39a0ab81aa2.png)


