# wut4lunch with Pyramid

## Steps

1. `python3 -m venv myvenv`
2. `source myvenv/bin/activate`
3. `pip install -r requirements.txt`
4. `pcreate -s starter wut4lunch`
5. `cd wut4lunch`
6. `pip install -e .`
7. `pip install -e ".[testing]"`
8. `py.test -q`
9. `pserve development.ini`
10. `deactivate`

### Current status:

NameError: lunches

 - Expression: "lunches"
 - Filename:   ... pyramid/wut4lunch/wut4lunch/wut4lunch/templates/index.pt
 - Location:   (line 2: col 20)
 - Source:     <div tal:condition="lunches">
                                   ^^^^^^^
 - Arguments:  renderer_name: templates/index.pt
               renderer_info: <RendererHelper - at 0x1047ffa20>
               context: <DefaultRootFactory None at 0x1047edc88>
               project: wut4lunch
               req: <Request - at 0x1047edac8>
               view: <function my_view at 0x101863620>
               request: <Request - at 0x1047edac8>
               repeat: {...} (0)

## Reference
* http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/install.html#installing-chapter
* http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html#creating-a-project