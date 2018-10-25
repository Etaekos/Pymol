#pocket: Crea un pocket utilzando un ligando de referencia, es necesario que las proteinas
#esten superpuestas

def pocket(p,ligand):
	
	#superposicion de proteinas del directorio
	lista=cmd.get_names("all")
	lista.remove(p)
	for x in range(len(lista)):
		k=cmd.super("{}".format(lista[x]),"{}".format(p))
		print("{} contra {} con RMS= {}".format(p,lista[x],k[0]))
		
	#Eliminacion de ligandos extras
	cmd.remove("solvent")
	cmd.select("res","resn Ca+GOL+CL+O+Na+MES+ACT+DMS+MG")
	cmd.remove("res")
	cmd.delete("res")
	#creacion de pockets con ligando de referencia
	cmd.hide("everything","polymer")
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
		
cmd.extend("pocket",pocket)
	