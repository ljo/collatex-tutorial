from collatex.core_classes import WordPunctuationTokenizer

__author__ = 'ronalddekker'

# The goal of this file is to construct a token stream from a single act from a single witness

# imports
from collatex import *

from collatex.suffix_based_scorer import Scorer
from integration.xml_tokenization import tokenize_xml_file
from integration.xml_tokenization import tokenize_plain_text_file

# main routine



# open the source file
tei_file_1823_act1 = open("/Users/ronalddekker/Desktop/CollateX/Elisa Files/1823_act_1.xml")

# parse the file, XML event after XML event
token_stream_witness_1 = []
for token_string in tokenize_xml_file(tei_file_1823_act1):
    # print(">" + str(token_string) + "< ")
    token_data = {}
    token_data["t"]=token_string
    # token_data["n"]=token_string.lower()
    token_stream_witness_1.append(token_data)



print(token_stream_witness_1)

# open the source file
tei_file_second_edition_act1 = open("/Users/ronalddekker/Desktop/CollateX/Elisa Files/second_edition_act_1.xml")

# parse the file, XML event after XML event
token_stream_witness_2 = []
for token_string in tokenize_xml_file(tei_file_second_edition_act1):
    # print(">" + str(token_string) + "< ")
    token_data = {}
    token_data["t"]=token_string
    # token_data["n"]=lowercase(token_string)
    token_stream_witness_2.append(token_data)

print(token_stream_witness_2)

# open the third file
plain_text_third_witness = open("/Users/ronalddekker/Desktop/CollateX/Elisa Files/Act1_version3.txt")

token_stream_witness_3 = []
for token_string in tokenize_plain_text_file(plain_text_third_witness):
    # print(">" + str(token_string) + "< ")
    token_data = {}
    token_data["t"]=token_string
    # token_data["n"]=lowercase(token_string)
    token_stream_witness_3.append(token_data)

print(token_stream_witness_3)





# create JSON block

witness_data_1 = {}
witness_data_2 = {}
witness_data_3 = {}

witness_data_1["id"]='1'
witness_data_2["id"]="2"
witness_data_3["id"]="3"

witness_data_1["tokens"] = token_stream_witness_1[0:500]
witness_data_2["tokens"] = token_stream_witness_2[0:500]
witness_data_3["tokens"] = token_stream_witness_3[0:500]

pretokenized_json = {}
pretokenized_json["witnesses"] = [witness_data_1, witness_data_2, witness_data_3]

print(len(token_stream_witness_1))
print(len(token_stream_witness_2))
print(len(token_stream_witness_3))

print(len(witness_data_1["tokens"]))
print(len(witness_data_2["tokens"]))
print(len(witness_data_3["tokens"]))


# # debug
# collation = Collation()
# for witness in pretokenized_json["witnesses"]:
#     collation.add_witness(witness)


# algorithm = Scorer(collation)
# block_witness1 = algorithm._get_block_witness(collation.witnesses[0])
# block_witness2 = algorithm._get_block_witness(collation.witnesses[1])
# block_witness3 = algorithm._get_block_witness(collation.witnesses[2])

# print(block_witness1.debug())
# print(block_witness2.debug())
# print(block_witness3.debug())


alignment_table = collate_pretokenized_json(pretokenized_json)

print(alignment_table)


