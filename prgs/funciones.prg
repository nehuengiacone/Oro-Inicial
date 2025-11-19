FUNCTION leerTxt (sRutaArchivo, sNombreArchivo)
	LOCAL lcPathFile as String,;
	      lcConnectionString as String
	      
	lcPathFile = TEXTMERGE("<<sRutaArchivo>>\<<sNombreArchivo>>")
	lnOpenTxt = FOPEN(lcPathFile, 0)

	IF lnOpenTxt > -1 then
		DO WHILE !FEOF(lnOpenTxt)
			lcConnectionString = FGETS(lnOpenTxt)
*!*				WAIT WINDOW lcConnectionString
		ENDDO
		
		FCLOSE(lnOpenTxt)
		RETURN lcConnectionString
	ELSE
*!*			MESSAGEBOX("Ocurrio un problema al abrir el archivo", 0+16, "ConnectionString")
		WAIT WINDOW "Ocurrio un problema al abrir el archivo" TIMEOUT 2
		FCLOSE(lnOpenTxt)
		RETURN ""
	ENDIF
ENDFUNC 


FUNCTION conectarBaseDeDatos(sConnectionString)
	LOCAL nConexion as Number
	nConexion = SQLSTRINGCONNECT(sConnectionString)
		
	IF nConexion > -1 THEN 
		WAIT WINDOW TEXTMERGE("Conexion exitosa <<nConexion>>")
		RETURN nConexion 
	ENDIF
	
	WAIT WINDOW TEXTMERGE("Fallo la conexion <<nConexion>>")
	RETURN nConexion
ENDFUNC


FUNCTION desconectarBaseDeDatos(nConexion)
	LOCAL nDesconexion as Number, lbFlag as Boolean
	lbFlag = .F.
	
	TRY
		nDesconexion = SQLDISCONNECT(nConexion) 
		IF nDesconexion == 1 THEN 
			WAIT WINDOW TEXTMERGE("Desconexion exitosa de Conexion <<nConexion>>")
			lbFlag = .T.
		ENDIF
	CATCH TO loFallo
		WAIT WINDOW TEXTMERGE("Desconexion fallida de Conexion <<nConexion>>; <<loFallo.message>>")
	ENDTRY
	
	RETURN lbFlag
ENDFUNC


FUNCTION holaMundo(sMensaje)
	MESSAGEBOX(sMensaje)
ENDFUNC


FUNCTION validarConsulta(nRespuesta)
	IF nRespuesta != -1 THEN 
		RETURN .t.
	ENDIF
	
	RETURN .f.
ENDFUNC


FUNCTION consultaFallida(nError, nConexion)
	MESSAGEBOX(TEXTMERGE("Algo Ocurrio <<nError[1]>>"), 0+16,"Mensaje del Sistema")
*!*		RETURN SQLROLLBACK(nConexion)
ENDFUNC


FUNCTION coeficienteBinomial(n, k)
*!*		A = (n k) = n! / k!.(n - k)!
	RETURN factorial(n) / (factorial(k) * factorial(n - k))
ENDFUNC

FUNCTION factorial(n)
*!*		n = n.(n - 1) ... 3.2.1
	IF n == 0 THEN 
		RETURN 1
	ENDIF 
	
	LOCAL i as double
	i = n - 1
	
	DO WHILE i > 0
		IF i == 0 THEN 
			n = n * 1
		ELSE 
			n = n * i
		ENDIF
		i = i - 1
	ENDDO
	
	RETURN n
ENDFUNC 

FUNCTION distribucionHipergeometrica(N, n1, k, x)
*!*	    N: tamaño de la poblacion
*!*	    n: tamaño de la muestra
*!*	    k: numero de "individuos" o elementos favorables en la poblacion
*!*	    x: variable aleatoria, es el numero de elementos favorables obtenidos. 
*!*	    nota: P(A) = p y P(A) = q ; p + q = 1
*!*	    P(X = x) = (k x) * ( (N - k) (n - x) ) / (N n)
*!*	    P(X = x) = CB1 * ( CB2 ) / CB3
	LOCAL CB1 as double,;
		  CB2 as Double,;
		  CB3 as Double
		  
	CB1 = coeficienteBinomial(k, x)
	CB2 = coeficienteBinomial((N-k), (n1-x))
	CB3 = coeficienteBinomial(N, n1)
 	
 	RETURN (CB1 * CB2) / CB3
ENDFUNC 

FUNCTION probabilidadAcumulada(N, n1, k, x)
*!*		P(X <= x) = P(X = 0) + P( X = 1) + .. P(X = x)
*!*		Suma de las probabilidades calculadas de la distribucion hipergeometrica
	LOCAL pAcum as Double,;
	      i as number
	pAcum = 0
	i = x
	DO WHILE i >= 0
		pAcum = pAcum + distribucionHipergeometrica(N, n1, k, i)
		i = i - 1
	ENDDO
	
	RETURN pAcum
ENDFUNC 


FUNCTION porcentaje(n1, n2)
	RETURN ROUND(((n1/n2) * 100), 2)
ENDFUNC 

