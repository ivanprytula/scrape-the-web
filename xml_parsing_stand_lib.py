import xml.etree.ElementTree as ET

"""
                Non-incremental	Incremental     Incremental
                                (Blocking)	    (Non-blocking)
ET.parse()	        ✔️
ET.fromstring()	    ✔️
ET.iterparse()		                ✔️
ET.XMLPullParser			                        ✔️


The XML data format is a mature and surprisingly powerful standard that is still in use today,
especially in the enterprise setting. Choosing the right XML parser is crucial in finding
the sweet spot between performance, security, compliance, and convenience.

- Choose the right XML parsing model
- Use the XML parsers in the standard library
- Use major XML parsing libraries
- Parse XML documents declaratively using data binding
- Use safe XML parsers to eliminate security vulnerabilities

"""

# Parse XML from a filename

# print(ET.parse("smiley.svg"))
# <xml.etree.ElementTree.ElementTree object at 0x7f0ae978fd00>


# Parse XML from a file object
with open("smiley.svg") as file:
    ET.parse(file)
    # print(ET.parse(file))
    # <xml.etree.ElementTree.ElementTree object at 0x7f9363753d00>

# Parse XML from a Python string
xml_piece = ET.fromstring(
    """\
     <svg viewBox="-105 -100 210 270">
       <!-- More content goes here... -->
     </svg>
     """
)
# print(xml_piece)  # <Element 'svg' at 0x7fe788cc92b0>

# ================================
# with a streaming pull parser, which yields a sequence of events and elements
for event, element in ET.iterparse("smiley.svg"):
    """uses blocking calls to read the next chunk of data,
    which might be unsuitable for asynchronous code running on a single thread of execution"""
    print(event, element.tag)


async def receive_data(url):
    """Download chunks of bytes from the URL asynchronously."""
    yield b"<svg "
    yield b'viewBox="-105 -100 210 270"'
    yield b"></svg>"


async def parse(url, events=None):
    parser = ET.XMLPullParser(events)
    async for chunk in receive_data(url):
        parser.feed(chunk)
        for event, element in parser.read_events():
            yield event, element

"""
What is XPath?
XPath is a major element in the XSLT standard.

XPath can be used to navigate through elements and attributes in an XML document.

- XPath stands for XML Path Language
- XPath uses "path like" syntax to identify and navigate nodes in an XML document
- XPath contains over 200 built-in functions
- XPath is a major element in the XSLT standard
- XPath is a W3C recommendation

XPath 1.0 became a W3C Recommendation on November 16, 1999.

XPath 2.0 became a W3C Recommendation on January 23, 2007.

XPath 3.0 became a W3C Recommendation on April 8, 2014.
"""
