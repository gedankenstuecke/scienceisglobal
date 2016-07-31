import re
from codecs import open
import sys
import unicodedata as uni
import regex
import networkx as nx
import matplotlib.pyplot as plt

myre = re.compile("["
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

out = open(sys.argv[2],"w",encoding="UTF-8")

G = nx.Graph()

def pairs(seq):
    for i in range(0, len(seq)-1):
        for j in range(i+1, len(seq)):
            yield (seq[i], seq[j])
for line in open(sys.argv[1], "r", encoding="UTF-8"):
    text = line.strip().split("\t")[3]
    rematch = re.search(myre,text)
    if rematch != None:
        out_array = []
        emoji_array = regex.findall(r'\X',rematch.group(0))
        for i in emoji_array:
            if i != "":
                j = "\\" + i
                out_array.append(j)
        for k in pairs(out_array):
           #print(k[0].replace("\\","") + ";" + k[1].replace("\\",""))
           out.write(k[0].replace("\\","") + ";" + k[1].replace("\\","")+"|\n")
           if G.has_edge(k[0].replace("\\",""),k[1].replace("\\","")):
               G[k[0].replace("\\","")][k[1].replace("\\","")]["weight"] += 1
               #print(G[k[0].replace("\\","")][k[1].replace("\\","")])
           else:
               G.add_edge(k[0].replace("\\",""),k[1].replace("\\",""),weight=1)


pos = nx.fruchterman_reingold_layout(G,scale=100000,iterations=5000)
nx.draw(G,pos=pos,with_labels = True)
plt.show()

nx.write_graphml(G,'scienceisglobal.graphml')
