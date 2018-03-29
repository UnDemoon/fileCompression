import  os  
if __name__ == '__main__':  
    from PyInstaller.__main__ import run  
    opts=['fileCompression.py','fileHanding.py','ui_fileCompression.py', 'fileOpener.py','-F','-w','--icon=bitbug_favicon.ico']  
    run(opts)  