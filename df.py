# -*- coding: gbk -*-
 
import json
import string
import codecs
where = 'e:/pyTest/result.txt'
where2 = 'e:/pyTest/result2.txt'

template = '<areas id=\"%d\" version=\"%s\" code=\"%s\" name=\"%s\" parent=\"%s\" level=\"%s\"/>\n'
template1 = '<areas id=\"%d\" version=\"%s\" code=\"%s\" name=\"%s\" full_name=\"%s\"/>\n'
template2 = '<area_hierarchy id=\"%d\" version=\"%s\" parent_id=\"%s\" child_id=\"%s\" />\n'



result = ""
result2= ""
fc = ""

areas_id = 0
areas_hi_id = 0

f = codecs.open('e:/pyTest/areas.json','r', 'utf8');

fc = f.read()

f.close()

js = json.loads(fc)


for pro in js['province']:
    areas_id = areas_id + 1
    pro.update({"id":areas_id})
    result += template1 % (pro['id'], '1', pro['code'], pro['name'],pro['name'])
    
for pro1 in js['city']:
    areas_id = areas_id + 1
    pro1.update({"id":areas_id})
    for pro in js['province'] :
        if pro['code'][0:2] == pro1['code'][0:2]:
            name = pro['name'] + pro1['name']
            result += template1 % (pro1['id'], '1', pro1['code'],pro1['name'], name)
   
    
for pro2 in js['district']:
    areas_id = areas_id + 1
    pro2.update({"id":areas_id})
    for pro in js['province'] :
        for pro1 in js['city']:
            if pro['code'][0:2] == pro1['code'][0:2] and pro1['code'][2:4] == pro2['code'][2:4] and pro2['code'][0:2] == pro['code'][0:2]:
                name = pro['name'] + pro1['name'] + pro2['name']
                result += template1 % (pro2['id'], '1', pro2['code'],pro2['name'], name )
    


#    全国的

for pro in js['province']:
    areas_hi_id = areas_hi_id + 1
    name = pro['name']
    proId = pro['id']
    result2 += template2 % (areas_hi_id, '1', "" , proId)
    proCode = pro['code'][0:2]
    for ci in js['city']:
        if  ci['code'][0:2] == proCode:
            if  ci['name'] != '市辖区' and  ci['name'] != '县':
                areas_hi_id = areas_hi_id + 1
                result2 += template2 % (areas_hi_id, '1', proId , ci['id'])
                for di in js['district']:
                    if ci['code'][2:4] == di['code'][2:4] and di['code'][0:2] == proCode:
                        areas_hi_id = areas_hi_id + 1
                        result2 += template2 % (areas_hi_id, '1', ci['id'] , di['id'])
            else:
                for di in js['district']:
                    if di['code'][0:2] == proCode:
                        areas_hi_id = areas_hi_id + 1
                        result2 += template2 % (areas_hi_id, '1', proId , di['id'])
'''
#广东的

for pro in js['province']:
    name = pro['name']
    proId = pro['id']
    if name == '广东省' :
        areas_hi_id = areas_hi_id + 1
        result2 += template2 % (areas_hi_id, '1', "" , proId)
        proCode = pro['code'][0:2]
        for ci in js['city']:
            if  ci['code'][0:2] == proCode:
                if  ci['name'] != '市辖区' and  ci['name'] != '县':
                    areas_hi_id = areas_hi_id + 1
                    result2 += template2 % (areas_hi_id, '1', proId , ci['id'])
                    for di in js['district']:
                        if ci['code'][2:4] == di['code'][2:4] and di['code'][0:2] == proCode:
                            areas_hi_id = areas_hi_id + 1
                            result2 += template2 % (areas_hi_id, '1', ci['id'] , di['id'])
                else:
                    for di in js['district']:
                        if di['code'][0:2] == proCode:
                            areas_hi_id = areas_hi_id + 1
                            result2 += template2 % (areas_hi_id, '1', proId , di['id'])
    if name == '广西壮族自治区' :
        areas_hi_id = areas_hi_id + 1
        result2 += template2 % (areas_hi_id, '1', "" , proId)
        proCode = pro['code'][0:2]
        for ci in js['city']:
            if  ci['code'][0:2] == proCode:
                if  ci['name'] != '市辖区' and  ci['name'] != '县':
                    areas_hi_id = areas_hi_id + 1
                    result2 += template2 % (areas_hi_id, '1', proId , ci['id'])
                    for di in js['district']:
                        if ci['code'][2:4] == di['code'][2:4] and di['code'][0:2] == proCode:
                            areas_hi_id = areas_hi_id + 1
                            result2 += template2 % (areas_hi_id, '1', ci['id'] , di['id'])
                else:
                    for di in js['district']:
                        if di['code'][0:2] == proCode:
                            areas_hi_id = areas_hi_id + 1
                            result2 += template2 % (areas_hi_id, '1', proId , di['id'])
'''





codecs.open(where, 'w', 'gbk').write(result + result2)

      



