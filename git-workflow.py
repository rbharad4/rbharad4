#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

import networkx as nx


# Integrate Python data visualization libraries

# In[2]:


G = nx.DiGraph()


# Create a directed graph using networkx library

# In[3]:


G.add_node ("Git Init")
G.add_node ("Git Add")
G.add_node ("Git Commit")
G.add_node ("Git Push")


# Add nodes to graph (each representing a Git command)

# In[4]:


G.add_edge ("Git Init", "Git Add")
G.add_edge ("Git Add", "Git Commit")
G.add_edge ("Git Commit", "Git Push")


# Add edges depicting relationships between each node in Git workflow

# In[16]:


pos = nx.circular_layout(G)


# Define the position of nodes for a more readable layout

# In[17]:


fig, ax = plt.subplots(figsize=(8, 6), dpi=200)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, 
        font_weight="bold", arrows=True, ax=ax)
plt.title("Basic Git Workflow")
plt.show()


# In[ ]:




