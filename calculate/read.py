file_content = ""

with open("../web/data.js", "r") as f:
    for lines in f:
        file_content += lines.strip() + " \n"
        
        
file_content = file_content.replace(" ", "")
file_content = "".join(file_content.split("\n")[1:])


import json

table  = json.loads(file_content)

for item in table:

    if len(item) == 4:
        item.append(False)
        
    

next_number = 1

rename = []
reverse_lookup = {}

for (i, _, _, neighbors, _) in table:
    if(len(neighbors) == 0):
        continue
    rename.append(i)
    reverse_lookup[i] = next_number
    next_number += 1

graph = []

for (i, x, y, neighbors, _) in table:
    if(len(neighbors) == 0):
        continue
    graph.append([
        reverse_lookup[i],x,y, [reverse_lookup[e] for e in neighbors], False]
    )
    

with open("graph.txt", "w") as f:
    f.write("{}\n".format(len(graph)))
    for (i, x, y, neighbors, _) in graph:
        f.write("{} {} {} {} ".format(
            i,x,y, len(neighbors)
        ))
        for item in sorted(neighbors):
            f.write("{} ".format(item))
            
        f.write("\n")
        
with open("new_graph.js", "w") as f:
    f.write("let points = \n")
    f.write(graph.__repr__())
        
