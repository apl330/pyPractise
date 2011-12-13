# -*- coding: utf-8 -*-
 
import json

import codecs
where = 'e:/pyTest/result.txt'

template = '<areas id=\"%d\" version=\"%s\" code=\"%s\" name=\"%s\" parent=\"%s\" level=\"%s\"/>\n'  

result_str = ""

fc = ""

id = 0

f = codecs.open('e:/pyTest/areas.json','r', 'utf8');

fc = f.read()

f.close()

js = json.loads(fc)

for pro in js['province']:
    id = id+1
    result_str += template % (id, '1', pro['code'][0:2], pro['name'], '00', 0 )

for pro in js['city']:
    id = id+1
    result_str += template % (id, '1', pro['code'][0:4], pro['name'], pro['code'][0:2] , 1)

for pro in js['district']:
    id = id+1
    result_str += template % (id, '1', pro['code'][0:6], pro['name'], pro['code'][0:4] ,2)

open(where, 'w').write(result_str.encode('utf8'))

