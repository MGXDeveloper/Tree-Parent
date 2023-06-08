import networkx as nx
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent, male, female, Father')

+ male('Ali')
+ male('Mohammad')
+ male('Ahmad')
+ male('Hussin')
+ male('Baker')
+ male('Taha')
+ male('Goad')

+ parent('Ali', 'Mohammad')
+ parent('Ali', 'Ahmad')

+ parent('Ahmad', 'Hussin')
+ parent('Ahmad', 'Baker')

+ parent('Mohammad', 'Taha')
+ parent('Mohammad', 'Goad')

Father(X, Y) <= parent(X, Y)&male(X)

edgs=[
    ('A1','R2-D2'),
    ('A2','R2-D2'),
    ('A3','R2-D2'),
    ('A4','R2-D2'),
    ('A1','A2'),
    ('A2','A3'),
    ('A3','A1'),
    ('A4','A1'),
]

G=nx.Graph()
#G.add_edge(tuple(parent(X, Y))[0])
G.add_edges_from(parent(X, Y))
MX=nx.adjacency_matrix(G)
nx.draw_networkx(G,with_labels = True)

print(Father(X, Y))
plt.show()