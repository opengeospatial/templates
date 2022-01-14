# Engineering Report template

OGC uses [Metanorma](https://www.metanorma.org) software for creating Engineering Report documents.

## Pre-requisite

Confirm that you have docker installed on your operating system. If you do not have docker installed, follow the steps at the [Get Docker page](https://docs.docker.com/get-docker/) to install it.

## Creating a copy of the template

The template for Engineering Report documents is organized as a folder of asciidoc files, with nested folders for sections, and other resources.

To create a copy of the template, follow these steps.

**Step 1**. Pull the latest version of the Metanorma image on to your local docker installation.

`docker pull metanorma/mn:latest`

**Step 2**.  Generate a copy of the template for OGC Engineering Report documents by running the following command from a terminal (i.e. from the command prompt).

`docker run -v "$(pwd)":/metanorma metanorma/mn  metanorma new -d engineering-report -t ogc  -l https://github.com/metanorma/mn-templates-ogc folder_for_engineering_report`

NOTE: The `-d engineering-report -t ogc` flags instruct metanorma that the template is for OGC Engineering Report documents.

NOTE: The `folder_for_engineering_report` value can be replaced with whatever you would like to be the name of the folder that contains the copy of the template.

## Editing a Draft OGC Engineering Report document for compilation with Metanorma

Now that you have generated a copy of the template, you can edit the document. The following steps assume that you have read the **authoring guidelines** are at https://www.metanorma.org/author/ogc/authoring/

**Step 3**. Next, edit the asciidoc file `document.adoc` by filling the document properties: `status`, `abbrev`, `edition` (i.e. version of the document), `docnumber` (OGC Document Number), `keywords`, `fullname` (of the editors).

**Step 4**. Ensure that the `doctype` property is set to `engineering-report`.

Refer to the authoring guidelines for the complete list of document properties.

NOTE: If there are multiple editors, the names of the editors are listed in the sequence `fullname`, `fullname_2`, `fullname_3`,...

## Compiling a Draft OGC Engineering Report document with a docker-containerized Metanorma instance

To convert the draft OGC Engineering Report from asciidoc format to HTML and PDF formats, we use the metanorma software to **compile** the document.

**Step 5**. From the folder containing the `document.adoc` file, run the following command.

`docker run -v "$(pwd)":/metanorma -v ${HOME}/.fontist/fonts/:/config/fonts  metanorma/mn  metanorma compile --agree-to-terms -t ogc -x xml,html,doc document.adoc`

NOTE: You need to add this option to retrieve licensed fonts  `--agree-to-terms`
