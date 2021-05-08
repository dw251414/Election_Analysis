
# Election Analysis

## Overview of Election-Audit
---

Using the power of Python to automate the vote-counting process for a local election. A Colorado Board of Elections employee has assigned the project to generate a vote count report to certify this U.S. congressional race. Provided with a csv file containing election results; the data consisted of a number for the ballot ID and a name for the county and candidate, respectively. 
~Enter Python~
Beginning with pseudo-coding - to make the audit easier to present to nontechnical colleagues and stakeholders; we used our roadmap as a guide to programmatically calculate the total number of votes cast, get a complete list of candidates who received votes, calculate the total number of votes each candidate received, percentage of votes each candidate won, and determine the winner of the election based on popular vote. 

---

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.4, Visual Studio Code, 1.56.0

---

## Election-Audit Results
The analysis of the election show that: 
- There were 369,711 votes cast in the election.
- The candidates were: 
- - Charles Casper Stockham
- - Diana DeGette
- - Raymon Anthony Doane
- The candidate results, and winner of the election were:
<img width="314" alt="election_results" src="https://user-images.githubusercontent.com/82069038/117555667-28d60c00-b02f-11eb-9035-eb0404075ea2.png">

---

## Election-Audit Summary
Not only does this Python script perform adequately to meet the deliverables above, but also can be edited to see fit for any election. Both by being written to parse through the initial .csv file provided, but also to programmatically calculate and push output to .txt files for accessibility, and ease of presentation to nontechnical colleagues and stakeholders. The script is versatile, and can be modified for application in other election-types. One example - processing an outcome for bill proposals. Another, could be analyzing voter feedback post-election.
