from modules.PuzzlesAPI import PuzzleInput

url = 'https://adventofcode.com/2020/day/7/input'

input_conn = PuzzleInput(url)
soup = input_conn.get_puzzle_input()
# print(len(soup))

rules = []

from string import digits
remove_digits = str.maketrans('', '', digits)

# for rule in soup comprehention
rules = [{rule.split(" contain ")[0]:[bag[1:] for bag in rule.split(" contain ")[1][:-1].translate(remove_digits).split(", ")]} for rule in soup]

edges = []
for rule in rules:
  for keys, values in rule.items():
    a = [(value, keys) for value in values]
    edges += a

    import networkx as nx
import matplotlib
from matplotlib import pyplot as plt

G=nx.DiGraph()
pos = nx.circular_layout(G)

for edge in edges:
  G.add_edge(*edge)

bag_tags = [bag_tag[1] for bag_tag in list(nx.edge_dfs(G, "shiny gold bag"))]
print(f"number of possible colours = {len(set(bag_tags))}")

# list(nx.edge_dfs(G, "shiny gold bag"))
# plt.figure(3,figsize=(12,12)) 
# nx.draw(G, node_size=60,font_size=8, with_labels=True)
# plt.show() # display
