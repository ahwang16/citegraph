# nx-graph.py
import bibtexparser as bib
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

class Author:
	def __init__(self, display_name, nodeid):
		self.display_name = display_name
		self.names = set()
		self.cites_set = set()
		self.is_cited_by_set = set()
		self.nodeid = nodeid


	def change_display_name(self, new_name):
		self.display_name = new_name


	def cites(self, other_author):
		self.cites_set.add(other_author.nodeid)


	def is_cited_by(self, other_author):
		self.is_cited_by_set.add(other_author.nodeid)


	def __repr__(self):
		return "{} ({})".format(self.display_name, self.nodeid)


def return_authors(authors):
	first_available_nodeid = 0

	# index by name and integer --> change this to be more memory-efficient
	author_dict = {}
	author_index = {}

	for author in authors:
		node = Author(author, first_available_nodeid)
		author_dict[author] = node
		author_index[first_available_nodeid] = author
		first_available_nodeid += 1


	for author in authors:
		node = author_dict[author]

		for a in authors[author]:
			if a not in author_dict:
				author_dict[a] = Author(a, first_available_nodeid)
				author_index[first_available_nodeid] = a
				first_available_nodeid += 1
			
			node.cites(author_dict[a])
			author_dict[a].is_cited_by(node)


	for author in author_dict:
		print(author_dict[author].display_name)
		print("\tCITES")
		for c in author_dict[author].cites_set:
			print("\t\t",author_index[c])
		print("\tIS CITED BY")
		for c in author_dict[author].is_cited_by_set:
			print("\t\t", author_index[c])
		print('')

	return author_dict, first_available_nodeid


if __name__ == "__main__":
	G = nx.DiGraph()

	parser = bib.bparser.BibTexParser(common_strings=True)

	with open('bibtex.bib') as bibtex_file:
		bib_database = bib.load(bibtex_file, parser=parser)

	original_authors = ['alyssa']
	cited_authors = defaultdict(lambda: 1)
	for entry in bib_database.entries:
		for cited in entry['author'].split("and"):
			cited_authors[cited.strip()] += 1

	print(cited_authors)
	for author in original_authors:
		G.add_node(author)

	for author in cited_authors:
		G.add_node(author)

	for author in original_authors:
		for cited in cited_authors:
			G.add_edge(author, cited, weight=cited_authors[cited])

	edge_width = [G[u][v]['weight'] for u, v in G.edges()] 

	print(edge_width)


	# authors = {
	# 		"alyssa hwang" : ["spongebob squarepants", "patrick star"],
	# 		"sandy cheeks" : ["alyssa hwang", "eugene krabs"],
	# 		"spongebob squarepants" : ["alyssa hwang", "patrick star"]
	# }



	# author_dict, first_available_nodeid = return_authors(authors)

	# for author in authors:
	# 	G.add_node(author)

	# for author in authors:
	# 	for cited in authors[author]:
	# 		if cited not in G.nodes:
	# 			G.add_node(cited)
	# 		G.add_edge(author, cited)
			# G.add_edge(cited, author, label="is cited by")

	nx.draw(G, with_labels=True, directed=True, width=edge_width)
	plt.show()
	