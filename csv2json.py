# www.philwillis.pw
import csv
import json

# http://geojsonlint.com/ test to see if it's geoJSON validated
inputFileName = 'sample.csv'
outputFileName = 'sample.json'




with open(inputFileName,'r') as f:
    # get the header values
    first_line = f.readline()[::1].split('\r\n')[0]
    print(first_line)

    headers = first_line.split(',')
    # print(headers)
    headersStr = ', '.join('"{0}"'.format(w) for w in headers)
    # print(headersStr)


    # make the json file
    lines = f.readlines()[1:]
    # print(lines)


    reader = csv.DictReader( lines, fieldnames = ( headers) )
    out = json.dumps( [ row for row in reader ] , sort_keys=True)
    print out



    ## write the data to a json file
    with open(outputFileName, 'w') as text_file:
        text_file.write(out)













