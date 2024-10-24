# apply the xslt stylesheet to all available xml files

import subprocess
import lxml.etree as ET
import os
import re
from pathlib import Path
import pdb
import sys

xsl_filename = "warnings.xsl"
basedir = sys.argv[1]


def to_snake(name):
    name = re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()
    return name


# handles acronyms better
def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1-\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1-\2", name).lower()


def transform_one_page(root, xml_filename, fileonly):
    if "toctree" in str(xml_filename):
        return
    try:
        dom = ET.parse(xml_filename)
    except Exception as e:
        print(f"Failed to parse {xml_filename}")
        print(e)
        return
    stringparams = {"filename": ET.XSLT.strparam(fileonly)}
    folder = root.split("/")[-1].strip()
    folder = camel_to_snake(folder)
    stringparams["folder"] = ET.XSLT.strparam(folder)

    xslt = ET.parse(xsl_filename)
    transform = ET.XSLT(xslt)
    try:
        newdom = transform(
            dom, **stringparams
        )  # can add an unparsed dictionary of stringparams
    except Exception as e:
        print(f"Failed to transform {xml_filename}")
        print(e)
        return

    # print(ET.tostring(newdom, pretty_print=True).decode("utf8"))

    # with open(xml_filename, "w") as ptfile:
    #     ptfile.write(ET.tostring(newdom, pretty_print=True).decode("utf8") + "\n")

    # newroot = root.replace("book/build/xml/", "")
    # ptx_filename = (
    #     str(xml_filename).replace(".xml", ".ptx").replace("book/build/xml/", "")
    # )
    # # maybe need to make folder
    # if ptx_filename.startswith("/"):
    #     ptx_filename = ptx_filename[1:]
    # fpath = Path(basedir) / "pretextNew" / Path(ptx_filename)
    # print("  ", fpath)
    # if "/" in ptx_filename:
    #     fpath.parent.mkdir(parents=True, exist_ok=True)

    # with open(fpath, "w") as ptfile:
    #     ptfile.write(ET.tostring(newdom, pretty_print=True).decode("utf8"))


xmldir = Path(basedir)
if not xmldir.exists():
    print(f"Directory {xmldir} does not exist")

# Recursively walk the tree
for root, dirs, files in os.walk(xmldir):
    for file in files:
        if ".ptx" in file and "toc" not in file:
            # print(root + "/" + file)
            transform_one_page(root, Path(os.path.join(root, file)), file)
