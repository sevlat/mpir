# generate vcxproj file

from os.path import normpath, join, split, relpath

def vcx_proj_cfg(plat, outf):

  f1 = r'''  <ItemGroup Label="ProjectConfigurations">
'''
  f2 = r'''    <ProjectConfiguration Include="{1:s}|{0:s}">
    <Configuration>{1:s}</Configuration>
    <Platform>{0:s}</Platform>
    </ProjectConfiguration>
'''
  f3 = r'''  </ItemGroup>
'''
  outf.write(f1)
  for pl in plat:
    for conf in ('Release', 'Debug'):
      outf.write(f2.format(pl, conf))
  outf.write(f3)

def vcx_globals(name, guid, outf):

  f1 = r'''  <PropertyGroup Label="Globals">
    <RootNamespace>{0:s}</RootNamespace>
    <Keyword>Win32Proj</Keyword>
    <ProjectGuid>{1:s}</ProjectGuid>
    </PropertyGroup>
'''
  outf.write(f1.format(name, guid))

def vcx_default_cpp_props(outf):

  f1 = r'''  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.Default.props" />
'''
  outf.write(f1)

def vcx_library_type(plat, proj_type, app_str, tool_char_set_lines, outf):

  f1 = r'''  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='{arg_conf}|{arg_platf}'" Label="Configuration">
    <ConfigurationType>{arg_conftype}</ConfigurationType>{arg_tool_char_set_lines}
    <UseDebugLibraries>{arg_is_debug}</UseDebugLibraries>
    </PropertyGroup>
'''

  for pl in plat:
    for is_debug in (False, True):
      sPG=f1.format(arg_conf               =('Debug' if is_debug else 'Release'),
                    arg_platf              =pl,
                    arg_conftype           =app_str[proj_type],
                    arg_tool_char_set_lines=tool_char_set_lines,
                    arg_is_debug           =('true' if is_debug else 'false'))

      outf.write(sPG)

def vcx_cpp_props(outf):

  f1 = r'''  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.props" />
'''
  outf.write(f1)

def vcx_extensions(outf):

  f1 = r'''  <ImportGroup Label="ExtensionSettings">
    <Import Project="..\..\build.vc\vsyasm.props" />
    </ImportGroup>
'''
  outf.write(f1)

def vcx_user_props(plat, outf):

  f1 = r'''  <ImportGroup Condition="'$(Configuration)|$(Platform)'=='{1:s}|{0:s}'" Label="PropertySheets">
    <Import Project="$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props" Condition="exists('$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props')" />
    <Import Project="..\..\overall.props" />
  </ImportGroup>
'''
  for pl in plat:
    for conf in ('Release', 'Debug'):
      outf.write(f1.format(pl, conf))

def vcx_file_version(outf):

  f1 = r'''  <PropertyGroup>
    <_ProjectFileVersion>10.0.21006.1</_ProjectFileVersion>
  </PropertyGroup>
'''
  outf.write(f1)

def vcx_tool_options(plat, proj_type, is_cpp, af_list, outf):

  f1 = r'''  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='{1:s}|{0:s}'" />
'''
  for pl in plat:
    for is_debug in (False, True):
      outf.write(f1.format(pl, 'Debug' if is_debug else 'Release'))

def vcx_hdr_items(hdr_list, relp, outf):

  f1 = r'''  <ItemGroup>
'''
  f2 = r'''    <ClInclude Include="{}{}" />
'''
  f3 = r'''  </ItemGroup>
'''
  outf.write(f1)
  for i in hdr_list:
    outf.write(f2.format(relp, i))
  outf.write(f3)

def vcx_c_items(cf_list, plat, relp, outf):

  f1 = r'''  <ItemGroup>
'''
  f2 = r'''    <ClCompile Include="{0:s}{1[0]:s}{1[1]:s}" />
'''
  f3 = r'''    <ClCompile Include="{0:s}{1[2]:s}\{1[0]:s}{1[1]:s}" />
'''
  f6 = r'''  </ItemGroup>
'''
  outf.write(f1)
  for nxd in cf_list:
    if nxd[2] == '':
      outf.write(f2.format(relp, nxd))
    else:
      outf.write(f3.format(relp, nxd))

  outf.write(f6)

def vcx_a_items(af_list, relp, outf):

  f1 = r'''  <ItemGroup>
'''
  f2 = r'''    <YASM Include="{0:s}{1[2]:s}\{1[0]:s}{1[1]:s}" />
'''
  f3 = r'''  </ItemGroup>
'''
  outf.write(f1)
  for nxd in af_list:
    outf.write(f2.format(relp, nxd))
  outf.write(f3)

def gen_vcxproj(proj_name, file_name, mpir_dir, build_dir,
                guid, plat, proj_type,
                app_str, tool_char_set_lines, tools_ver,
                is_cpp, hf_list, cf_list, af_list):

  f1 = r'''<?xml version="1.0" encoding="utf-8"?>
<Project DefaultTargets="Build" ToolsVersion="{0}" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
'''.format(tools_ver)
  f2 = r'''  <PropertyGroup Label="UserMacros" />
'''
  f3 = r'''  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.targets" />
'''
  f4 = r'''  <ImportGroup Label="ExtensionTargets">
    <Import Project="..\..\build.vc\vsyasm.targets" />
    </ImportGroup>
'''

  f5 = r'''<ItemGroup>
    <None Include="..\..\gmp-h.in" />
    </ItemGroup>
</Project>
'''

  fn = normpath(join(build_dir, file_name))
  relp = split(relpath(mpir_dir, fn))[0] + '\\'
  with open(fn, 'w') as outf:
    outf.write(f1)
    vcx_proj_cfg(plat, outf)
    vcx_globals(proj_name, guid, outf)
    vcx_default_cpp_props(outf)
    vcx_library_type(plat, proj_type, app_str, tool_char_set_lines, outf)
    vcx_cpp_props(outf)
    if af_list:
      vcx_extensions(outf)
    vcx_user_props(plat, outf)
    outf.write(f2)
    vcx_file_version(outf)
    vcx_tool_options(plat, proj_type, is_cpp, af_list, outf)
    if hf_list:
      vcx_hdr_items(hf_list, relp, outf)
    vcx_c_items(cf_list, plat, relp, outf)
    vcx_a_items(af_list, relp, outf)
    outf.write(f3)
    if af_list:
      outf.write(f4)
    outf.write(f5)


def write_project_props(file_name, build_dir, usermacros):
  f1 = r'''<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ImportGroup Label="PropertySheets" />
  <PropertyGroup Label="UserMacros">
'''

  f2 = r'''    <{0}>{1}</{0}>
'''

  f3 = r'''  </PropertyGroup>
  <PropertyGroup />
  <ItemDefinitionGroup />
  <ItemGroup>
'''

  f4 = r'''    <BuildMacro Include="{0}">
      <Value>$({0})</Value>
    </BuildMacro>
'''

  f5 = r'''  </ItemGroup>
</Project>
'''

  fn = normpath(join(build_dir, file_name))
  if len(usermacros)==0:
    if exists(fn):
      unlink(fn)
    return

  with open(fn, 'w') as outf:
    outf.write(f1)
    for um in usermacros:
      outf.write(f2.format(um[0], um[1]))
    outf.write(f3)
    for um in usermacros:
      outf.write(f4.format(um[0]))
    outf.write(f5)


def gen_project_props(file_name, build_dir, config, add_prebuild,
                      is_cpp, af_list):
  usermacros=[]
  if is_cpp:
    usermacros.append(('MPIR_Is_Cpp', 'True'))

  if add_prebuild and not is_cpp:
    usermacros.append(('MPIR_Build', config))

  if af_list:
    usermacros.append(('MPIR_Has_Asm', 'True'))

  write_project_props(file_name, build_dir, usermacros)


