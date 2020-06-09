# import bibtexparser as bib


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



if __name__ == "__main__":
	authors = {
		"alyssa hwang" : ["spongebob squarepants", "patrick star"],
		"sandy cheeks" : ["alyssa hwang", "eugene krabs"],
		"spongebob squarepants" : ["alyssa hwang", "patrick star"]
	}

	first_available_nodeid = 0
	author_nodes = []
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
