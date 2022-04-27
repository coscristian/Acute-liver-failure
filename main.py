from pyDatalog import pyDatalog

pyDatalog.create_terms()

""""

The diagnosis is given with the following rule:
* If a person has 3 or more symptoms of the Acute liver failure: the diagnosis is that illness, 
then the systems proceeds to give the possible treatment for the patient
*If the person does not have at least 3 of the specified symptoms, the system proceeds to give the possible treatment,
this treatment will only give the antibiotics name.

"""

def ask_for_symptom():
    kid_symptoms = []
    while True:
        result = input("Do you want to insert a symptom? (Y / N): ")
        if result == 'N':
            print("Thanks for using this system...")
        elif result == 'Y':
           symptom = input("Input the symptom the kid has: ")
           kid_symptoms.append(symptom)
        else:
            print("Input a correct answer")


def main():
    ask_for_symptom()


main()