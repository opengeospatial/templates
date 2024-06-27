# Charter template

You can compile Charters using either a local installation of *asciidoctor** or optionally a docker-containerized instance of *asciidoctor*.

## Using asciidoctor from a local installation

### Pre-requisite

Confirm that you have asciidoctor installed locally on your operating system. If you do not have asciidoctor installed, follow the steps at the [asciidoctor website](https://docs.asciidoctor.org/asciidoctor/latest/install/) to install it.

### Getting the Templates

**Step 1**. Obtain the template for a Draft Charter from the `template` sub-folder.

### Editing a Draft Charter for compilation with asciidoctor

Now that you have obtained a copy of the template, you can edit the document. 

**Step 2**. Next, edit the asciidoc file `swg_charter.adoc` or `dwg_charter.adoc`.

### Compiling a Draft Charter with a local asciidoctor instance

To convert the draft document from asciidoc format to HTML and PDF formats, we use the asciidoctor software to **compile** the document.

**Step 3**. From the folder containing the `swg_charter.adoc` or `dwg_charter.adoc` file, run the following command.

`asciidoctor swg_charter.adoc` if compiling a SWG Charter.

`asciidoctor dwg_charter.adoc` if compiling a DWG Charter.

## Using asciidoctor from with a docker-containerized asciidoctor instance

### Pre-requisite

Confirm that you have docker installed on your operating system. If you do not have docker installed, follow the steps at the [Get Docker page](https://docs.docker.com/get-docker/) to install it.

### Getting the Templates

**Step 1**. Obtain the template for a Draft Charter from the `template` sub-folder.

### Editing a Draft Charter for compilation with asciidoctor

Now that you have obtained a copy of the template, you can edit the document. 

**Step 2**. Next, edit the asciidoc file `swg_charter.adoc` or `dwg_charter.adoc`.

### Compiling a Draft Charter with docker

To convert the draft document from asciidoc format to HTML and PDF formats, we use the asciidoctor software to **compile** the document.

**Step 3**. From the folder containing the `swg_charter.adoc` or `dwg_charter.adoc` file, run the following command. The commands assume a Linux or MacOS terminal.

`docker run -it -u $(id -u):$(id -g) -v $(pwd):/documents/ asciidoctor/docker-asciidoctor asciidoctor swg_charter.adoc` if compiling a SWG Charter.

`docker run -it -u $(id -u):$(id -g) -v $(pwd):/documents/ asciidoctor/docker-asciidoctor asciidoctor dwg_charter.adoc` if compiling a DWG Charter.
