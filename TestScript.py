# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 09:00:57 2025

@author: Georg
"""

import json
import JsonToXML
import xmltojson


hiddenMod = {'@field': 'hidden',
             '@type': 'set',
             '@value': 'true'}

path = "T'au Empire.cat"
with open(path, 'r') as f:
    my_xml = f.read()
dorf = xmltojson.parse(my_xml)
dorf = json.loads(dorf)


"""
units = getRules(967)
parsed = CacheBSData.getFaction("TAU")
unitList = parsed['sharedSelectionEntries']['selectionEntry']
for unit in unitList:
    if unit['@id'] not in units:
        if 'modifiers' in unit:
            modifers = unit['modifiers']['modifier']
            if type(modifers) != list:
                modifers = [modifers]
            noHidden = True
            for modifier in modifers:
                if modifier['@field'] == 'hidden':
                    modifier['@value'] = 'true'
                    noHidden = False
                    break
            if noHidden:
                modID = 0
                while modID in modifers:
                    modID += 1
                modifers[modID] = hiddenMod
        else:
            unit['modifiers'] = {'modifier': {0: hiddenMod}}

parsedString = json.dumps(parsed)           
root = JsonToXML.fromTexttoFile(parsedString, "Tau.cat") # convert the string to XML and return the root node
"""
