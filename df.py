# -*- coding: utf-8 -*-
 
import json
import string
import codecs
where = 'e:/pyTest/result.txt'

template = '<areas id=\"%d\" version=\"%s\" code=\"%s\" name=\"%s\" parent=\"%s\" level=\"%s\"/>\n'
template1 = '<areas id=\"%d\" version=\"%s\" code=\"%s\" name=\"%s\" />'

result = ""

fc = ""

id = 0

f = codecs.open('e:/pyTest/areas.json','r', 'utf8');

fc = f.read()

f.close()

js = json.loads(fc)

for key in js.keys():
    id = id + 1;
    for item in js[key]:
        name = item['name']
        if ((name == '市辖区') or (name == '县')) :
            print(item['code'])
        
        '''
        if (Compare(item['name'], '市辖区') or cmp(item['name'], '县')) and cmp(item['code'][4:6], '00'):
            continue
        else :
            result += template1 % (id , 1, item['code'] ,item['name'])
        '''
'''
for pro in js['province']:
    id = id+1
    result += template % (id, '1', pro['code'][0:2], pro['name'], '00', 0 )

for pro in js['city']:
    id = id+1
    result += template % (id, '1', pro['code'][0:4], pro['name'], pro['code'][0:2] , 1)

for pro in js['district']:
    id = id+1
    result += template % (id, '1', pro['code'][0:6], pro['name'], pro['code'][0:4] ,2)
'''
open(where, 'w').write(result_str.encode('utf8'))

