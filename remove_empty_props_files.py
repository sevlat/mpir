# Utility for cleaning source tree from unused *.props files
# It scans directory tree and remove empty *.props files from project directories
# It doesn't remove empty *.props from props_templates directory

import sys
import os

g_EmptyPropsFileContent=[
    r"""<?xml version="1.0" encoding="utf-8"?>""",
    r"""<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">""",
    r"""  <ImportGroup Label="PropertySheets" />""",
    r"""  <PropertyGroup Label="UserMacros" />""",
    r"""  <PropertyGroup />""",
    r"""  <ItemDefinitionGroup />""",
    r"""  <ItemGroup />""",
    r"""</Project>"""
]

def CompressString(s):
    sRes=""
    for ch in s:
        i=ord(ch)
        if ord(ch)<=0x20:
            continue
        if ord(ch)==0xFEFF:
            continue
        if ord(ch)==0xFFFE:
            continue
        sRes+=ch.lower()
    return sRes

def CompressText(t):
    sRes=""
    for s in t:
        sRes+=CompressString(s)
    return sRes;

def RoughlyCompareStringAndTest(s, t):
    return CompressString(s)==CompressText(t)


def IsProjectFile(sFile):
    (_,sExt)=os.path.splitext(sFile)
    if (sExt.lower()!=".vcxproj"):
        return False
    return True;

def IsPropsFile(sFile):
    (_,sExt)=os.path.splitext(sFile)
    if (sExt.lower()!=".props"):
        return False
    return True;

# Not a good implementation !!!
def IsEmptyPropsFile(sFile):
    statinfo = os.stat(sFile)
    if not statinfo:
        return False
    if statinfo.st_size<290:
        return False
    if statinfo.st_size>292:
        return False
    with open(sFile, encoding='utf-8', mode='r') as f:
        sText="  "
        sText=f.read(300)
        if (RoughlyCompareStringAndTest(sText, g_EmptyPropsFileContent)):
            return True

    with open(sFile, encoding='utf-16', mode='r') as f:
        sText=""
        sText=f.read(300)
        if (RoughlyCompareStringAndTest(sText, g_EmptyPropsFileContent)):
            return True

    return False;

sRootDir=os.path.dirname(os.getcwd())

FilesToDelete=[]
for root, dirs, files in os.walk(sRootDir):
    if root.lower().find('templates')>=0:
        continue
#    print ("Directory: ", root)
    bProjectDir=False;
    for sFile in files:
        sFullFile=os.path.join(root, sFile)
        if IsProjectFile(sFullFile):
            bProjectDir=True

        if IsPropsFile(sFullFile):
#            print ("Property file: ", sFullFile)

            if IsEmptyPropsFile(sFullFile):
                FilesToDelete.append(sFullFile)

with open("delete_empty_props_files.bat", mode='w') as f:
    for sFile in FilesToDelete:
        print ("del ", sFile, file=f)
