# projectCreator
Simple Mac App which allows create new project folder structure on storage.

![](https://github.com/wlazlomarek/projectCreator/blob/master/project_creator_screen.png)


### Pyinstaller:
```console
$ pyinstaller --windowed --icon icon_path --name ProjectCreator ProjectCreator_2020.py
$ cd dist/myapp.app/Contents/MacOs
$ mkdir tcl tk
$ cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/tcl* tcl/
$ cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/tk* tk/
$ cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/Tk* tk/ 
```
