@echo off
cd /d %~dp0

poetry install

set poppler="poppler-0.68.0_x86.7z"
if not exist "poppler-0.68.0"\ (
    @REM Download poppler
    set url=http://blog.alivate.com.au/wp-content/uploads/2018/10/%poppler%
    bitsadmin /TRANSFER download %url% %CD%\%poppler%
    "C:\Program Files\7-Zip\7z.exe" x %poppler%
    xcopy .\poppler-0.68.0\bin\ .\bin\
)

poetry run pyinstaller .\main.py --onefile --noconsole
poetry run python .\tools\embed_binaries.py
poetry run pyinstaller main.spec
