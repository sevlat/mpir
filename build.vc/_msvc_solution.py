# add a project file to the solution

from os.path import join, exists
from re import compile

folder_guid = "{2150E333-8FDC-42A3-9474-1A3956D46DE8}"
vcxproject_guid = "{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}"

s_guid = r'\s*(\{\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\})\s*'
s_name = r'\s*\"([a-zA-Z][-.\\_a-zA-Z0-9]*\s*)\"\s*'
re_guid = compile(r'\s*\"\s*' + s_guid + r'\"\s*')
re_proj = compile(r'Project\s*\(\s*\"' + s_guid + r'\"\)\s*=\s*'
                  + s_name + r'\s*,\s*' + s_name + r'\s*,\s*\"' + s_guid + r'\"')
re_fmap = compile(r'\s*' + s_guid + r'\s*=\s*' + s_guid)

def read_solution_file(soln_name, solution_dir):
  fd, pd, p2f = {}, {}, {}
  solution_path = join(solution_dir, soln_name)
  if exists(solution_path):
    lines = open(solution_path).readlines()
    for i, ln in enumerate(lines):
      m = re_proj.search(ln)
      if m:
        if m.group(1) == folder_guid and m.group(2) == m.group(3):
          fd[m.group(2)] = m.group(4)
        elif m.group(3).endswith('.vcxproj') or m.group(3).endswith('.pyproj'):
          pd[m.group(2)] = (m.group(1), m.group(3), m.group(4))
      m = re_fmap.search(ln)
      if m:
        p2f[m.group(1)] = m.group(2)
  return fd, pd, p2f

sol_1 = '''Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio {0}
VisualStudioVersion = {1}
MinimumVisualStudioVersion = 10.0.40219.1
'''

sol_2 = '''Project("{}") = "{}", "{}", "{}"
EndProject
'''

sol_3 = '''Global
    GlobalSection(SolutionConfigurationPlatforms) = preSolution
        Debug|Win32 = Debug|Win32
        Debug|x64 = Debug|x64
        Release|Win32 = Release|Win32
        Release|x64 = Release|x64
    EndGlobalSection
    GlobalSection(SolutionProperties) = preSolution
        HideSolutionNode = FALSE
    EndGlobalSection
    GlobalSection(NestedProjects) = preSolution
'''

sol_4 = '''     {} = {}
'''

sol_5 = r'''    EndGlobalSection
EndGlobal
'''

def write_solution_file(file_name, solution_dir, fd, pd, p2f, ver_short, ver_long):
  with open(join(solution_dir, file_name), 'w') as outf:
    outf.write(sol_1.format(ver_short, ver_long))
    for f, g in fd.items():
      outf.write(sol_2.format(folder_guid, f, f, g))
    for f, (g1, pn, g2) in pd.items():
      outf.write(sol_2.format(g1, f, pn, g2))
    outf.write(sol_3)
    for f, g in p2f.items():
      outf.write(sol_4.format(f, g))
    outf.write(sol_5)

def add_proj_to_sln(soln_name, solution_dir, soln_folder, proj_name, file_name, guid,
                    ver_short, ver_long):
  fd, pd, p2f = read_solution_file(soln_name, solution_dir)
  if soln_folder:
    if soln_folder in fd:
      f_guid = fd[soln_folder]
    else:
      f_guid = '{' + str(uuid4()).upper() + '}'
      fd[soln_folder] = f_guid
  pd[proj_name] = (vcxproject_guid, file_name, guid)
  if soln_folder:
    p2f[guid] = f_guid

  write_solution_file(soln_name, solution_dir, fd, pd, p2f, ver_short, ver_long)
