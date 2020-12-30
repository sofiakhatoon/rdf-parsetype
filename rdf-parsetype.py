import rdflib
from rdflib.graph import ConjunctiveGraph
from rdflib import Graph, Literal, RDF, URIRef, BNode, RDFS
from rdflib.namespace import Namespace
from rdflib.namespace import FOAF , XSD
# https://www.w3.org/TR/owl-xmlsyntax/


lit2006 = Literal('2006-01-01',datatype=XSD.date)
litxml = Literal(u'<a><b/></a>',datatype=RDF.XMLLiteral)
# create a Graph for obj1
gObj1 = ConjunctiveGraph()
owl = Namespace('http://www.w3.org/2002/07/owl#')

footype = URIRef("http://www.recshop.fake/cd#")
u = URIRef(u'http://example.com/foo')

bb=Literal("bobIdeas", datatype=footype)
obj1=BNode()

gObj1.add((BNode('freq'), RDF.value, litxml))
print(gObj1.serialize(format="pretty-xml").decode("utf-8"))
