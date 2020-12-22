import csv
import pprint

relevantPages = ['captureEsn', 'deviceResults', 'captureConsumerId']

i1 = open('input1.csv')
i2 = open('input2.csv')
o = open('output.csv', 'w')

outputFile = csv.writer(o)
input1File = csv.reader(i1, delimiter=',')
input2File = csv.reader(i2, delimiter=',')

next(input1File)
next(input2File)

pageInfo = {}
totalErrors = 0

# Iterate on file 1 to get the count of errors per pageName
# row[0] error message
# row[1] pageName
# row[2] unique count of errors
for row in input1File:
    if row[1] not in relevantPages:
        continue

    totalErrors += int(row[2])

    if row[1] in pageInfo:
        pageInfo[row[1]]['errors'].append([row[0], row[2]])
        pageInfo[row[1]]['errorCount'] += int(row[2])
        continue

    pageInfo[row[1]] = {
        'errors': [[row[0], row[2]]],
        'errorCount': int(row[2]),
        'journeyCount': 0
    }

# Iterate through file 2 to get unique count of journeys per pageName
# row[0]: pageName
# row[1]: unique count of journeys
for row in input2File:
    if row[0] not in relevantPages:
        continue

    if row[0] in pageInfo:
        pageInfo[row[0]]['journeyCount'] = row[1]
        continue

    pageInfo[row[0]] = {
        'errors': [],
        'errorCount': 0,
        'journeyCount': row[1]
    }

outputFile.writerow(['pageName', 'journeyCount', 'errorCount'])

for key in pageInfo.keys():
    outputFile.writerow([key, pageInfo[key]['journeyCount'], pageInfo[key]['errorCount']])
