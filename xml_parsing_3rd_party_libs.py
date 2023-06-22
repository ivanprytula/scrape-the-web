"""
- import untangle
https://realpython.com/python-xml-parser/#explore-third-party-xml-parser-libraries


- import xmltodict

- lxml: Use ElementTree on Steroids
If you want the best performance, the broadest spectrum of functionality,
and the most familiar interface all wrapped in one package,
then install lxml and forget about the rest of the libraries.
It's a Python binding for the C libraries libxml2 and libxslt,
which support several standards, including XPath, XML Schema, and XSLT.

    import lxml.etree as ET

- https://pypi.org/project/defusedxml/
    At best they know about <!DOCTYPE> from experience with HTML
    but they are not aware that a document type definition (DTD)
    can generate an HTTP request or load a file from the file system.

>>> import defusedxml.ElementTree as ET
>>> ET.parse("bomb.xml")
Traceback (most recent call last):
  ...
    raise EntitiesForbidden(name, value, base, sysid, pubid, notation_name)
defusedxml.common.EntitiesForbidden:
 EntitiesForbidden(name='lol', system_id=None, public_id=None)

"""

import mmap

# import untangle


class XMLTagStream:
    def __init__(self, path, tag_name, encoding="utf-8"):
        self.file = open(path)
        self.stream = mmap.mmap(self.file.fileno(), 0, access=mmap.ACCESS_READ)
        self.tag_name = tag_name
        self.encoding = encoding
        self.start_tag = f"<{tag_name}>".encode(encoding)
        self.end_tag = f"</{tag_name}>".encode(encoding)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.stream.close()
        self.file.close()

    def __iter__(self):
        end = 0
        while (begin := self.stream.find(self.start_tag, end)) != -1:
            end = self.stream.find(self.end_tag, begin)
            yield self.parse(self.stream[begin : end + len(self.end_tag)])

    def parse(self, chunk):
        document = untangle.parse(chunk.decode(self.encoding))
        return getattr(document, self.tag_name)


# with XMLTagStream("abstract.xml", "doc") as stream:
#     for doc in stream:
#         print(doc.title.cdata.center(50, "="))
#         for sublink in doc.links.sublink:
#             print("-", sublink.anchor.cdata)
#         if "q" == input("Press [q] to exit or any key to continue..."):
#             break

# =========================
import lxml.etree as ET


xml_schema = ET.XMLSchema(
    ET.fromstring(
        """\
         <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
             <xsd:element name="parent"/>
             <xsd:complexType name="SomeType">
                 <xsd:sequence>
                     <xsd:element name="child" type="xsd:string"/>
                 </xsd:sequence>
             </xsd:complexType>
         </xsd:schema>"""
    )
)

valid = ET.fromstring("<parent><child></child></parent>")
invalid = ET.fromstring("<child><parent></parent></child>")

xml_schema.validate(valid)  # True

xml_schema.validate(invalid)  # False


"""
BeautifulSoup: Deal With Malformed XML
- pluggable architecture
- handle invalid content and it has a rich API for extracting information

Document Type	Parser Name	    Python Library	    Speed
HTML	        "html.parser"	    -	           Moderate
HTML	        "html5lib"	        html5lib	    Slow
HTML	        "lxml"	            lxml	        Fast
XML	        "lxml-xml" or "xml"	    lxml	        Fast
"""

from bs4 import BeautifulSoup

# Parse XML from a file object
with open("smiley.svg") as file:
    soup = BeautifulSoup(file, features="lxml-xml")

# Parse XML from a Python string
soup = BeautifulSoup(
    """\
<svg viewBox="-105 -100 210 270">
  <!-- More content goes here... -->
</svg>
""",
    features="lxml-xml",
)
print(soup.prettify())

soup_with_invalid_content = BeautifulSoup("""\
    <parent>
        <child>Forbidden < character </parent>
        </child>
    ignored
    """, features="lxml-xml")

print(soup_with_invalid_content.prettify())
