#!/usr/bin/env python


# =================================================================================================
from dataclasses import fields
import sys
import xml.etree.ElementTree as ET

from citeproc.source.bibtex import BibTeX
from citeproc import CitationStylesStyle, CitationStylesBibliography
from citeproc import formatter
from citeproc import Citation, CitationItem


def exitWithErrorMessage(msg):
    print(msg)
    sys.exit(1)


bibtext_db = ''
style = ''
input_document = ''
generated_bibliography = ''

if len(sys.argv) == 5:
    bibtext_db = sys.argv[1]
    style = sys.argv[2]
    input_document = sys.argv[3]
    generated_bibliography = sys.argv[4]

    if bibtext_db.endswith('.bib') ==False:
        exitWithErrorMessage('1st argument must be a filename with a .bib extension')

    if style.endswith('.csl') ==False:
        exitWithErrorMessage('2nd argument must be a filename with a .csl extension')

    if input_document.endswith('.xml') ==False:
        exitWithErrorMessage('3rd argument must be a filename with a .xml extension')

    if generated_bibliography.endswith('.adoc') ==False:
        exitWithErrorMessage('4th argument must be a filename with a .adoc extension')

else:
    print('Problem with the command line arguments '+str(len(sys.argv)))
    sys.exit(1)


# Parse the bibtex file

bib_source = BibTeX(sys.argv[1]) # e.g. "./test/bibtex.bib"


print(str(bib_source.fields))

# load a style from the csl file

bib_style = CitationStylesStyle(sys.argv[2], validate=False) # e.g.  "./test/lncs.csl"


# Create a citeproc-py bibliography and configure it with the style, bib file, and formatter

bibliography = CitationStylesBibliography(bib_style, bib_source,
                                          formatter.plain)


# Processing citations in a document needs to be done in two passes as for some
# CSL styles, a citation can depend on the order of citations in the
# bibliography and thus on citations following the current one.
# For this reason, we first need to register all citations with the
# CitationStylesBibliography.


tree = ET.parse(sys.argv[3]) # e.g. './test/template1/document.xml'
root = tree.getroot()

citelist = []

for target in root.iter("{https://www.metanorma.org/ns/ogc}xref"):
    citelist.append(str(target.get('target')))
    citation1 = Citation([CitationItem(str(target.get('target')))])
    bibliography.register(citation1)


# In the second pass, CitationStylesBibliography can generate citations.
# CitationStylesBibliography.cite() requires a callback function to be passed
# along to be called in case a CitationItem's key is not present in the
# bibliography.

def warn(citation_item):
    print("WARNING: Reference with key '{}' not found in the bibliography."
          .format(citation_item.key))



# Then the bibliography can be rendered.

fout = open(sys.argv[4],'w')

print('[bibliography]')
print('[[Bibliography]]')
print('== Bibliography')

fout.write('[bibliography]\n')
fout.write('[[Bibliography]]\n')
fout.write('== Bibliography\n\n')

itemCount = 0
bibliographyList = bibliography.bibliography()

while itemCount < len(bibliographyList):

    bibliographyItem = str(bibliographyList[itemCount])[1+str(bibliographyList[itemCount]).index('.'):]
    print("* [[["+str(bibliography.keys[itemCount])+","+str(itemCount+1)+"]]], "+bibliographyItem+" "+"\n")
    fout.write("* [[["+str(bibliography.keys[itemCount])+","+str(itemCount+1)+"]]], "+bibliographyItem+'\n')

    itemCount = itemCount + 1

fout.close()
