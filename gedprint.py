#!/usr/bin/env python
import sys
import gedcom

def nice_name(element):
    return " ".join(list(element.name()))

def get_individuals(tree):
    return [element for element in tree.element_list() if element.is_individual()]

def recursive_children(element):
    descendents = element.children()
    for d in descendents:
        r = recursive_children(d)
        for c in r:
            descendents.append(c)
    return descendents
    
def print_nice1(tree, filter = lambda v: v.is_individual()):
    for k, v in tree.element_dict().iteritems():
        if filter(v):
            print k, v.name()
            for c in recursive_children(v):
                print "   ", c

tree = gedcom.Gedcom("simple1.gedcom")

print_nice1(tree, lambda v: v.is_family())


sys.exit(0)

ppl = {}
for individual in get_individuals(tree):
    ppl[individual.value()] = individual

for id, individual in ppl.iteritems():
    print id, nice_name(individual)


