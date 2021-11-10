# Election_Analysis

## Overview of Project

A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent congresstional election.

  1. Calculate the total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.
  6. The voter turnout for each county.
  7. The percentage of votes from each county out of the total count
  8. The county with the highest turnout

## Resources

* Data Source: election_results.csv

* Software: Python 3.7.6, Visual Studio Code, 1.62.0

## Election-Audit Results

The analysis of the election shows that:

* There were 369,711 votes cast in the election.
* The county information is as follows:
  * Jefferson County had 38,855 votes, representing 10.5% of total votes
  * Denver County had 306,055 votes, representing 82.8% of total votes
  * Arapahoe County had 24,801 votes, representing 6.7% of total votes
* Denver had the largest number of votes out of all of the counties
* The candidate's were:
  *  Charles Casper Stockham
  *  Diana DeGette
  *  Raymon Anthony Doane
* The candidate results were:
  * Charles Casper Stockham received 23.0% of the vote and 85,214 number of votes.
  * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  * Raymon Anthony Doane 3.1% of the vote and 11,606 number of votes.
* The winner of the election was:
  * Diana DeGette who received 73.8% of the vote and 272,892 total votes.


## Election-Audit Summary

This same audit program could be easily used for other elections in order to calculate the results. There would just need to be a few modifications in order to achieve this, they are as follows:

* In the input file there should be an additional variable to capture the name of the election, so the results can be tabulated for just that election
* Would have to create another loop in the data in order to go through all of the steps for each of the elections and then a specific output file can be created for each of the elections to keep it seperate
