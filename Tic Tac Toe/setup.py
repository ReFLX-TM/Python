from distutils.core import setup 
import py2exe 
 
setup(name = "Nombre ejecutable", 
 version = "1.0", 
 description = "Breve descripcion", 
 author = "autor", 
 author_email = "email del autor", 
 url = "url del proyecto", 
 license = "tipo de licencia", 
 scripts = "tic_tac_toeVtkinter.py", 
 console = "tic_tac_toeVtkinter.py", 
 options = {"py2exe": {"bundle_files": 1}}, 
 zipfile = None,
)