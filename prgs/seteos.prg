LOCAL lcDirectorio as String,;
	  lcDirectorioClases as String,;
	  lcDirectorioPrgs as String,;
	  lcConnectionString as String
	  
lcDirectorio = FULLPATH(CURDIR())
lcDirectorioClases = "clases"
lcDirectorioPrgs = "prgs"
lcDirectorioMenu = "menu"

SET DEFAULT TO (lcDirectorio)
SET PATH TO ADDBS(lcDirectorio)
SET PATH TO (lcDirectorioClases) ADDITIVE 
SET PATH TO (lcDirectorioPrgs) ADDITIVE 
SET PATH TO (lcDirectorioMenu) ADDITIVE 

SET PROCEDURE TO (lcDirectorioPrgs + "\funciones") ADDITIVE 
SET PROCEDURE TO (lcDirectorioPrgs + "\salir") ADDITIVE
SET CLASSLIB TO (lcDirectorioClases + "\App") ADDITIVE  
SET CLASSLIB TO (lcDirectorioClases + "\Login") ADDITIVE
SET CLASSLIB TO (lcDirectorioClases + "\Colecciones") ADDITIVE 
SET CLASSLIB TO (lcDirectorioClases + "\Menu") ADDITIVE  