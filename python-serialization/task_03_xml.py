#!/usr/bin/python3
"""
    Module for serialising a Python dictionary to XML format
    and
    deserialising XML back to a dictionary
"""


# import Python’s standard library for XML processing
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialise a Python dictionary into XML and
    save it to a file

    Args:
        dictionary (dict): The dictionary to serialise
        filename (str): The target XML file path

    Return:
        None
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialise_from_xml(filename):
    """
    Deserialise XML content from a file into a Python dictionary

    Args:
        filename (str): The XML file to read

    Return:
        dict: The deserialised dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    new_dict = {}
    for child in root:
        new_dict[child.tag] = child.text
    return new_dict



# #Test My Code:
# def main():
#     sample_dict = {
#         'name': 'John',
#         'age': '28',
#         'city': 'New York'
#     }

#     xml_file = "data.xml"
#     serialize_to_xml(sample_dict, xml_file)
#     print(f"Dictionary serialized to {xml_file}")

#     deserialized_data = deserialize_from_xml(xml_file)
#     print("\nDeserialized Data:")
#     print(deserialized_data)
