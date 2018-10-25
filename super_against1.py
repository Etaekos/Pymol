#script Super_against1(p)
#Funcion que realiza funcion super de pymol sobre una proteina "p" contra todas
#las otras proteinas del directorio actual(formato pdb)
from pymol import stored
from pymol import cmd
import sys
from glob import glob


def load_all():
	lst= glob("*.pdb")
	lst.sort()
	for fil in lst: cmd.load(fil)

def super_against1(p):

	lista=cmd.get_names("all")
	lista.remove(p)
	

	for x in range(len(lista)):
		k=cmd.super("{}".format(lista[x]),"{}".format(p))
		print("{} contra {} con RMS= {}".format(p,lista[x],k[0]))
		
cmd.extend("super_against1",super_against1)
cmd.extend("load_all",load_all)
