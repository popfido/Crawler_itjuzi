import codecs
import json

writer = codecs.open('url_loaded.csv', mode='w', encoding='utf-8')

with codecs.open('company.json.backup', encoding='utf-8', mode='r') as f:
    counter = 0
    for line in f:
        counter += 1
        try:
            writer.write(json.loads(line.strip())['url'] + '\n')
        except Exception as e:
            print e
            print line.strip()
            print counter