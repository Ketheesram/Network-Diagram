import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import openpyxl as oxl
from pylab import rcParams

#Read the data from excel file
data=pd.read_excel('Arranged.Xlsx')
df=pd.DataFrame(data,columns=['X','Y','Type'])
Label=pd.DataFrame(data,columns=['Name of Devices'])
Ncolor=pd.DataFrame(data,columns=['Node type'])

#By the data making edge list
G=nx.from_pandas_edgelist(df,source='X',target='Y',edge_attr='Type')
pos=nx.spring_layout(G)

#Deleteting null values from dictationary
nan_value=float("NaN")
Label.replace("",nan_value,inplace=True)
Label.dropna(subset=["Name of Devices"],inplace=True)

nan_value=float("NaN")
Ncolor.replace("",nan_value,inplace=True)
Ncolor.dropna(subset=["Node type"],inplace=True)

#making label dictatinary
Labeldict=Label.to_dict()['Name of Devices']
Nodecolor=Ncolor.to_dict()['Node type']

#Ploting Diagram with Size
fig = plt.figure(1, figsize=(200, 80), dpi=120)
colorlegend = {'Mobile Devices': 2,'Remote Devices': 3,'Other ': 1}

#coloring the nodes
low,*_,high=sorted(Nodecolor.values())
norm=mpl.colors.Normalize(vmin=low,vmax=high,clip=True)
mapper=mpl.cm.ScalarMappable(norm=norm,cmap=mpl.cm.brg)

#Color Legends
f=plt.figure(1)
ax=f.add_subplot(1,1,1)
for label in colorlegend:
   ax.plot([0],[0],color=mapper.to_rgba(colorlegend[label]),label=label)

#Ploting the diagram
nx.draw(G,
        labels=Labeldict,
        with_labels=True,
        node_color=[mapper.to_rgba(i) for i in Nodecolor.values()],
        font_weight='normal',
        edge_cmap=plt.cm.Blues,
        node_size=20,
        edge_color='black',
        pos=pos,
        font_size=6)

#Edge formatting
edge_labels=nx.get_edge_attributes(G,'Type')
formatted_edge_labels={(elem[0],elem[1]):edge_labels[elem] for elem in edge_labels}
nx.draw_networkx_edge_labels(G,
                             pos,
                             edge_labels=formatted_edge_labels,
                             label_pos=0.5,
                             font_size=4)

#diagram Title and legends
plt.title('DNS Network Diagram')
plt.legend()
plt.show()




