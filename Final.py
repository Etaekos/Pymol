#script
from pymol import stored
from pymol import cmd
import sys
from glob import glob
cmd.reinitialize()
lst= glob("*.pdb")
lst.sort()
def load_all():

	for fil in lst: cmd.load(fil)


def super_contra1(p):

	lista=cmd.get_names("all")
	lista.remove(p)
	

	for x in range(len(lista)):
		k=cmd.super("{}".format(lista[x]),"{}".format(p))
		print("{} contra {} con RMS= {}".format(p,lista[x],k[0]))
		

theFiles= glob("*.pdb")

def ligand():

	for f in theFiles:
		cmd.remove("polymer or resn HOH");

def pocket():
	
	cmd.hide("everything","polymer")
	cmd.select("pocket","byres organic around 4.0 and polymer")
	cmd.show("surface","pocket")
	
def trash():
	cmd.select("res","resn Ca+GOL+CL+O+Na+MES+ACT+DMS+MG")
	
def fivefrom(selection):
	cmd.hide("everything","polymer")
	cmd.select("pocket","{} around 5.0 and polymer".format(selection))
	cmd.show("surface","pocket")

def delete_by_sele(selection):
	cmd.delete(' '.join(cmd.get_object_list('(' + selection + ')')))

cmd.extend("super_contra1",super_contra1)	
cmd.extend("load_all",load_all)		
cmd.extend("ligand",ligand)
cmd.extend("pocket",pocket)
cmd.extend("trash",trash)
cmd.extend("delete_by_sele",delete_by_sele)
cmd.extend("fivefrom",fivefrom)



def prep(p,ligand):
	super_contra1(p)
	cmd.remove("polymer or resn HOH")
	trash()
	cmd.remove("res")
	cmd.delete("res")
	cmd.select("stuff","{} expand 5".format(ligand))
	#k=cmd.identify("stuff",1)
	#di={}
	#for tuples in k:
		#if tuples[0] not in di and tuples[0]!="prep":
		#	m=open("{}.pdb".format(tuples[0]),"r")
		#	for lines in m:
		#		if lines.startswith("HETATM") and int(tuples[1])==int(lines[7:12]):
		#			di[tuples[0]]=lines[17:20]
					
												   
	cmd.extract("prep","stuff")
	cmd.group("rubbish","not prep")
	cmd.delete("rubbish")
	cmd.save("prep.pdb")
cmd.extend("prep",prep)


def pocket2(ligand):
	cmd.hide("everything","polymer")
	trash()
	cmd.remove("res")
	cmd.delete("res")
	cmd.select("stuff","{} expand 5".format(ligand))
	k=cmd.identify("stuff",1)
	di={}
	for tuples in k:
		if tuples[0] not in di and tuples[0]!="prep":
			m=open("{}.pdb".format(tuples[0]),"r")
			for lines in m:
				if lines.startswith("HETATM") and int(tuples[1])==int(lines[7:12]):
					di[tuples[0]]=lines[17:20]				
	nombres=di.items()
	
	for obj,res in nombres:
		cmd.select("pocket_{}".format(res),"resn {} around 5 and polymer".format(res))
		cmd.show("surface","pocket_{}".format(res))
	
	cmd.group("pockets","pocket_*")
		
cmd.extend("pocket2",pocket2)

		
	
	
	
	
	
	
