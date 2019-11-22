# projectCreator
Simple program to create new project folder structure on storage.

Building app by pyinstaller:
```console
$ pyinstaller --windowed --icon icon_path --name ProjectCreator myapp.py 
$ cd dist/myapp.app/Contents/MacOs
$ mkdir tcl tk
$ cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/tcl* tcl/
$ cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/tk* tk/
$ cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/Tk* tk/ 
```
