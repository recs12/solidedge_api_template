
:: Set this file for compiling the executable of the macro.

ipyc.exe /main:__main__.py ^
Interop.SolidEdge.dll ^
/embed ^
/out:{{cookiecutter.project_name}}_macro_64x_0-0-0 ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:logo.ico
