from pyDatalog import pyDatalog

pyDatalog.create_terms('padece,sintoma,suprime,enfermedad_de,Enfermedad,X,Y,Z,padece_de,Paciente,tiene_sintomas_de,Sintomas,'
                       'tiene_sintoma_de,alivia_a,K,Farmaco,compartido_entre,Q,K,N,Sintoma')
#Enfermedades: Gripe, Hepatitis, Intoxicacion
#Paciente - Enfermedad
+padece('Pedro', 'Gripe')
+padece('Pedro', 'Hepatitis')
+padece('Juan', 'Hepatitis')
+padece('Maria', 'Gripe')
+padece('Carlos', 'Intoxicacion')

#Sintoma - Enfermedad
+sintoma('Fiebre', 'Gripe')
+sintoma('Cansancio', 'Hepatitis')
+sintoma('Diarrea', 'Intoxicacion')
+sintoma('Cansancio', 'Gripe')

#Farmaco - Sintoma
+suprime('Aspirina', 'Fiebre')
+suprime('Lomotil', 'Diarrea')

#Predicados Y Reglas
# ¿Podemos conocer que enfermedad tiene Pedro? ¿Y Maria?
enfermedad_de(Enfermedad, X) <= padece(X,Y) & (Y == Enfermedad)

# ¿Quien padece Gripe?
padece_de(Paciente, X) <= padece(Y, X) & (Y == Paciente)

# ¿Qué sintomas tiene Pedro?
tiene_sintomas_de(Sintomas, X) <= padece(X, Y) & sintoma(Z, Y) & (Z == Sintomas)

# ¿Quien padece Diarrea?
padece_de(Paciente, X) <= padece(Y, X) & (Y == Paciente)

#Quien esta cansado?
tiene_sintoma_de(Paciente, Y) <= sintoma(Y, X) & padece(Z, X) & (Z == Paciente)

#¿Hay un farmaco que alivie a Pedro?
alivia_a(Farmaco, Y) <= padece(Y, X) & sintoma(Z, X) & suprime(K, Z) & (K == Farmaco)

#¿Hay algun sintoma que compartan Juan Y Maria?
compartido_entre(Sintoma, X, Y) <= padece(X, Z) & padece(Y, K) & sintoma(N, Z) & sintoma(Q, K) & (N == Sintoma) & (Q == Sintoma)

def usar_regla(paciente):
    enfermedad = tiene_sintomas_de(Sintoma, paciente)
    return enfermedad


def pedir_por_pantalla():
    print("Encontrar Sintoma. Dado el paciente")
    resultado = ( input("Ingrese el Paciente: "))
    return resultado


def main():
    persona = pedir_por_pantalla()
    enfermedad = usar_regla(persona)
    print(enfermedad)


main()