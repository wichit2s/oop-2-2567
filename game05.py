import json


def open_json(fname='Tiny_Swords.json'):
    f = open(fname, 'r')
    #for line in f.readlines():
    #    print(line.strip())
    tileset = json.load(f)
    f.close()
    return tileset

tileset = open_json()
#print(type(tileset))
for k in tileset:
    print(k)
