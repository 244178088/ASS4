#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()


G.add_node('Carol', pos = (2, 5))
G.add_node('Andre', pos = (1, 4))
G.add_node('Fernando', pos = (3, 4))
G.add_node('Diane', pos = (2, 3))
G.add_node('Beverly', pos = (1, 2))
G.add_node('Garth', pos = (3, 2))
G.add_node('Ed', pos = (2, 1))
G.add_node('Heather', pos = (4, 3))
G.add_node('Ike', pos = (5, 3))
G.add_node('Jane', pos = (6, 3))
G.add_edges_from([  ('Carol', 'Andre'), ('Carol', 'Fernando'), ('Carol', 'Ed'),
                    ('Andre', 'Fernando'), ('Andre', 'Diane'), ('Andre', 'Beverly'),
                    ('Beverly', 'Diane'), ('Beverly', 'Garth'), ('Beverly', 'Ed'),
                    ('Fernando', 'Diane'), ('Fernando', 'Heather'), ('Fernando', 'Garth'),
                    ('Garth', 'Diane'), ('Garth', 'Heather'), ('Garth', 'Ed'),
                    ('Ed', 'Diane'), ('Ike', 'Heather'), ('Ike', 'Jane')
                ])
pos = nx.get_node_attributes(G, 'pos')


nx.draw(G, pos, with_labels = True)
plt.show()







