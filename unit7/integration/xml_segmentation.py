__author__ = 'ronalddekker'

# imports
from xml.dom.pulldom import START_ELEMENT, parse
from xml.dom.minidom import NamedNodeMap


def segmentate_xml_file(xml_file):
    # parse the file, XML event after XML event
    # NOTE: the variable name 'doc' is not optimal (the variable is only a pointer to a stream of events)
    doc = parse(xml_file)
    print(str(doc)) # doc = DOMEventStream

    segment = 0

    for event, node in doc:
        if event == START_ELEMENT and node.localName == "div" and node.attributes["type"].value == "act":
            print(event, node.localName, node.attributes["type"].value, node.attributes.items())
            segment += 1
            yield(event, node, doc, segment)


# We define a function which tells the computer what to do when an act is encountered.
def segmentate_xml_file_and_write_segments_to_disc(xml_file,
                                                   filename="/Users/ronalddekker/Desktop/CollateX/Elisa Files/1823_act_"):
    for (event, node, doc, segment) in segmentate_xml_file(xml_file):
        doc.expandNode(node)
        # print("Act "+str(act)+" contains: "+str(node.toxml()))
        segment_xml_file = open(filename +str(segment)+".xml", mode="w")
        segment_xml_file.write(node.toxml())
        segment_xml_file.close()


