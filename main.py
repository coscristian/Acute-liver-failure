from pyDatalog import pyDatalog

pyDatalog.create_terms('sintoma_de, sintoma, Symptom_of')

""""
The diagnosis is given with the following rule:
* If a person has 3 or more symptoms of the Acute liver failure: the diagnosis is that illness, 
then the systems proceeds to give the possible treatment for the patient
*If the person does not have at least 3 of the specified symptoms, the system proceeds to give the possible treatment,
this treatment will only give the antibiotics name.
"""

# Symptom - Illness
+symptom_of('vomiting', 'poisoning')
#+symptom_of('nausea', 'normal')
+symptom_of('yellow', 'normal')
+symptom_of('abdomen', 'normal')
+symptom_of('malaise', 'normal')
+symptom_of('confusion', 'normal')
+symptom_of('sleepiness', 'normal')
+symptom_of('breath', 'normal')
+symptom_of('tremors', 'normal')

#Diagnosis
Illness('Acute_liver_Failure') <= symptom_of('vomiting', 'poisoning') &
                                  symptom_of('yellow_skin', 'poisoning') &


# Diagnosis
#+diagnosis('Acute liver Failure', 'vomiting' & 'nausea' & 'yellow')

#+sintoma_de('vomiting')
#Illness(Diagnosis, X) <= symptom_of(X, Y)

def determine_symptom(kid_symptoms):
    for symptom in kid_symptoms:
        diagnosis = Illness(Diagnosis, symptom)
        print(diagnosis)


def ask_for_symptom():
    kid_symptoms = []
    cont = True
    while cont:
        result = input("Do you want to insert a symptom? (Y / N): ")
        if result == 'Y':
            symptom = input("Input the symptom the kid has: ")
            kid_symptoms.append(symptom)
            determine_symptom(kid_symptoms)
        elif result == "N":
            cont = False
        else:
            print("Input a correct answer")


def main():
    ask_for_symptom()


main()
