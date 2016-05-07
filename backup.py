import codecs

new = []
with codecs.open('company.json', mode='r', encoding='utf-8') as f:
    for line in f:
        new.append(line)

with codecs.open('company.json.backup', mode='a', encoding='utf-8') as f:
    for i in new:
        f.write(i)
