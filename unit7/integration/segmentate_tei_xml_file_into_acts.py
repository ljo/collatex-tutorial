__author__ = 'ronalddekker'

# The goal of this file is to construct a witness from a single transcription stored in TEI format.

# imports

from integration.xml_segmentation import segmentate_xml_file_and_write_segments_to_disc

# open the source file
# Note file path containing ~ do not work for some reason
#tei_file_1823 = open("~/Desktop/CollateX/Elisa Files/JulianMelfiMS.xml")
#tei_file_1823 = open("/Users/ronalddekker/Desktop/CollateX/Elisa Files/JulianMelfiMS.xml")
tei_file = open("/Users/ronalddekker/Desktop/CollateX/Elisa Files/JulianMelfiPub1823.xml")
print(str(tei_file)) # tei_file = TextIoWrapper

# for every act we want to create a token stream in JSON format
# We first write an XML file for each act... just to save us from going over the whole file again and again


segmentate_xml_file_and_write_segments_to_disc(tei_file, filename = "/Users/ronalddekker/Desktop/CollateX/Elisa files/second_edition_act_")



