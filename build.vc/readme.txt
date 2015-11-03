This is an attempt to simplify a MSVC build system, using Property sheets
(*.props files)

Vcxproj files now doesn't contain any project settings: they all are in 
property sheets.

Every vcxproj imports only one property sheet: overall.props. This is a hub,
that imports all others required property sheets, depending on platform,
configuration, and so on.

overall.props also imports a property sheet _project.props, that imports
before other properties sheets and contains 1-2 properties, that describes
this project

As a result, vcxproj files became shorter and simplier. If you need to change
some project setting, you shuld change it in only one place.

Also user may define properties MPIR_Props_PreExternal and MPIR_Props_External
(for example, in MSBUILD command line) to pass a name of his own property sheets,
that will be imported before and after all others property sheets.
This is a way to customize project building, without editing downloaded files.


Notice, that this all is an experimental job. It was not seriously tested !!!
You may try it on you own risk!!!

--------------------------------------------------------------------------------
mpir_config.py

Generate OLD-styled projects for any MSVC version (passed as command line
parameter).

For example (for Msvc12): 
  python mpir_config.py 12

Projects and solutions will put to build.vcNN directory (as it was previously)

--------------------------------------------------------------------------------
mpir_config_p.py

Generate NEW-styled projects and props for any MSVC version (passed as command
line parameter). 

For example (for Msvc12): 
  python mpir_config_p.py 12

Projects and solutions will put to build.vcNN.p directory.

---------------------
There also a build.vc12.p.handmade directory. It contains projects and props, 
that I made by hand, when investigated vcxproj structure. Now it serves as 
ethalon for debugging mpir_config_p.py.
This directory will be removed later.

--------------------------------------------------------------------------------
remove_empty_props_files.py

Scans directory tree, looks for empty property sheets and generate a bat file
(delete_empty_props_files.bat).

--------------------------------------------------------------------------------
vsyasm.* files

Required for project files. They ware the same in all build.vcNN, so it would be
better to have them only in this directory.

--------------------------------------------------------------------------------
mpir_configs

Temporary working directory. To be deleted later.
Contain four mpir_config.NN.py, copied from build.vcNN directories.
I used them for investigation and comparing mpir_config.py files.

--------------------------------------------------------------------------------
props_common

Contains common property sheets - common for all MSVC versions

--------------------------------------------------------------------------------
props_sys

Contains system (nonpublic) property sheets, that declares special properties for
other properti sheets and projects. These files should not be edited using MSVS 
PropertyManager, so I made them invisible in a PropertyManager.

--------------------------------------------------------------------------------
props_templates

My service directory, probably will be removed.
Contain property sheet templates (empty). I used this files to populate project
directories with properties.


=========
Best regards,
Taymanov Sergey, Moscow