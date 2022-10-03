import csv

data = csv.DictReader(open('Resources/election_results.csv'))
myReport = open('analysis/election_analysis.txt', 'w')

total = 0
counties = {}
candidates = {}
countiesReport = ''
candidatesReport = ''
LCT = [0,'']
winner = [0,""]

for row in data:
    total += 1
    county = row['County']
    candidate = row['Candidate']

    if county not in counties.keys():
        counties[county] = 0

    counties[county] += 1

    if candidate not in candidates.keys():
        candidates[candidate] = 0
    
    candidates[candidate] += 1

for county in counties:
    votes = counties[county]
    countiesReport += f'{county}: {votes/total*100:.1f}% ({votes:,}) \n'

    if votes > LCT[0]:
        LCT[0] = votes
        LCT[1] = county

for can in candidates.keys():
    candidatesReport += f'{can}: {candidates[can]/total*100:.1f}% ({candidates[can]:,})\n'

    if winner[0] < candidates[can]:
        winner[0] = candidates[can]
        winner[1] = can

output = f'''
Election Results
-------------------------
Total Votes: {total:,}
-------------------------
County Votes:
{countiesReport}
-------------------------
Largest County Turnout: {LCT[1]}
-------------------------

{candidatesReport}
-------------------------
Winner: {winner[1]}
Winning Vote Count: {winner[0]} 
Winning Percentage: {winner[0]/total*100:.1f}%
-------------------------
'''
print(output)
myReport.write(output)