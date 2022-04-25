# Bibliography Management

The OGC uses the LNCS (Lecture Notes in Computer Science) citation style for bibliographies in OGC documents.

To assist editors in creating and managing bibliographies when authoring documents in metanorma-asciidoc, a python script is provided in this folder.

**Note that this utility is for advanced users.**

First prepare the environment by installing the citeproc-py library. This is a one-time requirement.

`pip3 install citeproc-py`

Now each time you want to be generate the bibliography, simply run the following commands to generate the metanorma xml document.

 
`cd "./templates/bibliography_management/test/template1"`
`docker run -v "$(pwd)":/metanorma -v ${HOME}/.fontist/fonts/:/config/fonts  metanorma/mn  metanorma compile --agree-to-terms -t ogc -x xml document.adoc`

Then adapt and run the following commands to generate a file called  annex-bibliography.adoc that contains the generated bibliography. Note that the file annex-bibliography.adoc will be overwritten. Ensure that you have a copy if you need to retain any existing information in the file.

`cd ./templates/bibliography_management`
`python3 -m ogcbibtex "./test/bibtex.bib" "./test/lncs.csl" "./test/template1/document.xml" "./test/template1/sections/annex-bibliography.adoc"` 

Then compile the document, with the newly generated bibliography.

`cd "./templates/bibliography_management/test/template1"`
`docker run -v "$(pwd)":/metanorma -v ${HOME}/.fontist/fonts/:/config/fonts  metanorma/mn  metanorma compile --agree-to-terms -t ogc -x xml,html,pdf document.adoc`
