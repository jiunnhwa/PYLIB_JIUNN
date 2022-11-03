
text = """
<?xml version="1.0" encoding="utf-8"?>
<Project xmlns="http://schemas.microsoft.com/developer/msbuild/2003" DefaultTargets="Build" ToolsVersion="4.0">
  <PropertyGroup>
    <OutputType>WinExe</OutputType>
    <RootNamespace>Eternal</RootNamespace>
    <AssemblyName>Eternal</AssemblyName>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">
    <DefineConstants>,CONST_A,CONST_B,CONST_C</DefineConstants>
  </PropertyGroup>
  <ItemGroup>
    <Compile Include="MyScr\Source1.vb" />
  </ItemGroup>
  <ItemGroup>
    <None Include="Sample.ini" />
  </ItemGroup>
</Project>
"""

def parse_vbproj_props(filename):
    """
    parse a vbproj file to return a dictionary of useful properties.
    """

    # invalid filename
    if not exists(filename):
        return None

    # get the main dir of the campaign
    topdir = dirname(abspath(filename))

    namespace = r"{http://schemas.microsoft.com/developer/msbuild/2003}"
    root = ET.parse(filename).getroot()

    # get assembly name(campaign_name)
    assembly = root.find(".//" + namespace + "AssemblyName").text

    # get pre-compilation such as NUNIT3
    define_constants = root.find(".//" + namespace + "DefineConstants").text
    define_constants = [x for x in define_constants.split(",") if len(x)]

    # get ini name
    nodes = [elem for elem in root.findall(".//" + namespace + "None")]
    ini = [node.attrib.get("Include") for node in nodes if node.attrib.get("Include").upper().endswith("INI")][0]

    # get full path of ini file
    ini_fullpath = path_join(topdir, ini)

    # get all scr files
    nodes = [elem for elem in root.findall(".//" + namespace + "Compile")]
    scrfiles = [node.attrib.get("Include") for node in nodes if node.attrib.get("Include").upper().startswith("MYSCR")]

    return {
        "assembly": assembly,
        "define_constants": define_constants,
        "topdir": topdir,
        "ini": ini,
        "ini_fullpath": ini_fullpath,
        "scrfiles": scrfiles,
    }
