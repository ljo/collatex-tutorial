__author__ = 'ronalddekker'

# imports
from xml.dom.pulldom import START_ELEMENT, parse
from xml.dom.pulldom import CHARACTERS
from xml.dom.minidom import NamedNodeMap
from xml.dom.minidom import Text

from collatex.core_classes import WordPunctuationTokenizer


# define functions

# written as a generator (or is this an array?, no this is a list comprehension)
def generate_nodes(tei_file):
    # NOTE: the variable name 'doc' is not optimal (the variable is only a pointer to a stream of events)
    doc = parse(tei_file)
    return [node for event, node in doc if event == START_ELEMENT]


def generate_text_nodes(tei_file):
    doc = parse(tei_file)
    for event, node in doc:
        if event == CHARACTERS:
            yield node

def tokenize_text_node(text_node):
    # split on whitespace, punctuation and numerical values
    tokenizer = WordPunctuationTokenizer()
    return tokenizer.tokenize(text_node.data)

def tokenize_xml_file(tei_file):
    for node in generate_text_nodes(tei_file):
        content = node.wholeText.strip()
        if not content:
            continue
        for token in tokenize_text_node(node):
            yield token

def tokenize_plain_text_file(plain_text_file):
    tokenizer = WordPunctuationTokenizer()

    with plain_text_file as f:
        for line in f:
            for token in tokenizer.tokenize(line):
                yield token
