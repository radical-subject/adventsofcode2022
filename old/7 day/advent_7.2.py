from modules.PuzzlesAPI import PuzzleInput

url = 'https://adventofcode.com/2020/day/7/input'

input_conn = PuzzleInput(url)
soup = input_conn.get_puzzle_input()
# print(len(soup))

import networkx as nx
import matplotlib
from matplotlib import pyplot as plt

#func for removing digits from string 
from string import digits
remove_digits = str.maketrans('', '', digits)

#parsing soup to list of rules (1 rule = 1 dict in list), rstrip() deletes all " " from the left of string
rules = [{rule.split(" contain ")[0]:[bag.lstrip() for bag in rule.split(" contain ")[1][:-1].translate(remove_digits).split(", ")], "numbers":[int(i) for i in rule.split() if i.isdigit()]} for rule in soup]

#preparation of edges [("a", "b"), ...] and weights [(number : \d), ..] for directed weighted graph
edges = []
weights = []
#iterate by rules (rule = {"starting bag tag": ['contains this bag tag', 'and this bag tag', ...], "numbers": [1, 2, 3, ...]})
for rule in rules:
  for keys, values in rule.items():
    #unpack list of bags that are contained in key starting bag to list of edges
    a = [(keys, value) for value in values]
    #this will add to list of edges all edges related to 1 row of input rules
    if keys != 'numbers':
      edge = a
      edges += edge
    # if contains no bags then "numbers" = [], change this to 0 weight
    elif a == []:
      weight_tuple = [('numbers', 0)]
      weights += weight_tuple
    #this just regularly adds (appends elements) list of tuples [("number, 2"), ("number", 3), ..] to weights list
    else: 
      weight_tuple = a
      weights += weight_tuple


weighted_edges = []
for i in range(len(edges)):
  try:
    # convert edges ("a", "b") to list to append an element
    a = list(edges[i])
    # appends element (I could have done it without convertation just by ()+(), silly me)
    a.append(weights[i][1])
    # convert back
    b = tuple(a)
    #appent the list with new tuples ("a", "b", 1)
    weighted_edges.append(b)
  except IndexError as e:
    print(e)

#now create a directed graph
G=nx.DiGraph()
#add directed edges from list with tuples of weighted edges
G.add_weighted_edges_from(weighted_edges)
#apply depth first search algorithm from networkx library - it gives me the list of edges of paths, where i can come starting from "shiny gold bag"
calculate_edges = list(nx.edge_dfs(G, "shiny gold bag"))
#now add weights to this list of edges
paths_with_weighted_edges = []
wt_sum = 0
for (u, v) in calculate_edges:
  #accessing weighted edges from original graph
  for (x, y, wt) in G.edges.data('weight'):
    if (u, v) == (x, y):
        # z.append((f"({u}, {v}, {wt})"))
        paths_with_weighted_edges.append((u, v, wt))
        wt_sum += wt

# create a new graph consisting only from possible paths from "shiny gold bag" node
G_DFS=nx.DiGraph()
pos = nx.circular_layout(G_DFS)

G_DFS.add_weighted_edges_from(paths_with_weighted_edges)

#here i have nx.all_simple_paths(G_DFS, source="shiny gold bag", target='no other bag') that gives all possible paths from "shiny gold bag" to 'no other bag'
paths = {n : [(path[i], path[i+1]) for i in range(len(path)-1)] for n, path in enumerate(nx.all_simple_paths(G_DFS, source="shiny gold bag", target='no other bag'))}
# this is dictionary to ask conveniently for weights of related edges
paths_with_weighted_edges_dict = {(path[0], path[1]):path[2] for path in paths_with_weighted_edges}

def main():
  """
  here goes some very fucked up code to go down edge by edge, 
  then checking WHERE the next route in graph branches from the previous branch
  ("j_start_summing_index" index)
  """
  x = [path for path in paths.values()]
  path_weight_sum = 0
  for i in range(len(x)):
    path_weight = 0
    edge_increment = 1
    for j in range(len(x[i])):
      if i != 0:
        if x[i][j] != x[i-1][j]:
          j_start_summing_index = j
          break
        else:
          j_start_summing_index = 0
      else:
        j_start_summing_index = 0

    for j in range(len(x[i])):
      edge_increment *= paths_with_weighted_edges_dict[x[i][j]]
      if j >= j_start_summing_index:
        path_weight += edge_increment
    path_weight_sum += path_weight

  print(f"num of bags in my shiny gold bag - {path_weight_sum}")
  return path_weight_sum


if __name__ == '__main__':
  main()