:: app name: {{cookiecutter.project_name}}
:: Set this file for compiling the executable of the macro.
:: So it can be added to the user custom theme in solidedge. 
ipyc.exe /main:./{{cookiecutter.project_name}}/__main__.py ^
./{{cookiecutter.project_name}}/Interop.SolidEdge.dll ^
./{{cookiecutter.project_name}}/api.py ./bullet/holes.py ^
./{{cookiecutter.project_name}}/equivalences.py ^
./{{cookiecutter.project_name}}/customs.py ^
/embed ^
/out:{{cookiecutter.project_name}}_macro_64x_0-0-0 ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:logo.ico 
