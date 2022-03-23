# pylint: skip-file
from markdown import Extension
from markdown.treeprocessors import Treeprocessor
import xml.etree.ElementTree as etree

class ImagesTreeprocessor(Treeprocessor):
	def __init__(self, md):
		Treeprocessor.__init__(self, md)

	def run(self, root):
		parent_map = {child: parent for parent in root.iter() for child in parent}
		images = root.iter("img")
		for image in images:
			if image.attrib.get("class") == "figure":
				parent = parent_map[image]
				imageIndex = list(parent).index(image)

				figure = etree.Element('figure')
				figure.set("markdown", "")

				a = etree.Element('a')
				a.set("href", "#")
				a.set("data-featherlight", image.attrib["src"])
				a.append(image)

				figcaption = etree.Element('figcaption')
				figcaption.text = image.attrib["alt"]

				figure.append(a)
				figure.append(figcaption)

				parent.insert(imageIndex, figure)
				parent.remove(image)

class FigureExtension(Extension):
	def extendMarkdown(self, md, md_globals):
		md.treeprocessors.add("figure", ImagesTreeprocessor(md), "_end")


# pylint: disable-next=invalid-name
def makeExtension(*args, **kwargs):
	return FigureExtension(**kwargs)
