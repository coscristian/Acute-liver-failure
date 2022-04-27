from pyDatalog import pyDatalog

pyDatalog.create_terms('padre,madre,sexo,X,Y,Z,Sexo,abuelos_pat,abuelos_mat,Abuelo,K,Abuela')

+padre ('juan' ,'carlos')
+padre ('juan','rosario')
+padre ('juan','soltero')
+padre ('victor' ,'belen' )
+padre ('carlos' ,'elena' )
+padre ('carlos' ,'carlitos')
+madre ('maria' ,'soltero')
+madre ('maria' ,'carlos' )
+madre ('maria' ,'rosario')
+madre ('consuelo','belen')
+madre ('belen','elena')
+madre ('belen','carlitos')

+sexo ('juan', 'M')
+sexo ('carlos', 'M')
+sexo ('rosario', 'F')
+sexo ('soltero', 'M')
+sexo ('victor', 'M')
+sexo ('belen', 'F')
+sexo ('elena', 'F')
+sexo ('carlitos', 'M')
+sexo ('maria', 'F')
+sexo ('consuelo', 'F')

#Abuelos Paternos
abuelos_pat(Abuelo,Abuela, Y) <= padre(X,Y) & (padre(Z,X) & madre(K, X)) & (Abuelo == Z) & (Abuela == K)

#Abuelos Maternos
abuelos_mat(Abuelo,Abuela, Y) <= madre(X,Y) & (padre(Z,X) & madre(K, X)) & (Abuelo == Z) & (Abuela == K)


def usar_regla(nieto):
    #resultado = abuelos_pat(Abuelo,Abuela, nieto)
    resultado = abuelos_mat(Abuelo, Abuela, nieto)
    return resultado
def pedir_por_pantalla():
    nombre = input("Ingrese el nombre del nieto: ")
    return nombre
def main():
    hijo = pedir_por_pantalla()
    resultado = usar_regla(hijo)
    print(resultado)
main()