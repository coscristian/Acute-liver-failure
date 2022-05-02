from ui import ui
from knowledgeBase import knowledge_base
import os

def make_diagnosis(symptoms_list):
    ui.clear()
    treatment = {}
    if len(symptoms_list) >= 3:
        ui.show_acute_liver()
    else:
        ui.no_have_acute()

    ui.next_treatment()
    for symptom in symptoms_list:
        result_diagnosis = knowledge_base.make_rule(symptom)
        antibiotic = result_diagnosis.v()[1]
        treatment[symptom] = antibiotic   #In this dict will be saved the {symptom: antibiotic} treament for the patient

    for symptom, antibiotic in treatment.items():
        ui.show_treatment(symptom, antibiotic, knowledge_base.recommendations)


def get_symptom(select_option):
    if select_option != 14:
        if select_option == 1:
            return 'Yellow Skin'
        elif select_option == 2:
            return 'Headache'
        elif select_option == 3:
            return 'Upper Abdomen'
        elif select_option == 4:
            return 'Abdomen'
        elif select_option == 5:
            return 'Nausea'
        elif select_option == 6:
            return 'Vomiting'
        elif select_option == 7:
            return 'Stomachache'
        elif select_option == 8:
            return 'Malaise'
        elif select_option == 9:
            return 'Confusion'
        elif select_option == 10:
            return 'Sleepiness'
        elif select_option == 11:
            return 'Breath'
        elif select_option == 12:
            return 'Tremors'
        return None


def ask_for_symptom():
    selected_opt = 0
    symptoms_list = []
    while selected_opt != 14:
        ui.menu()
        selected_opt = ui.user_input()
        symptom = get_symptom(selected_opt)
        if symptom is not None:
            symptoms_list.append(symptom)
            ui.symptom_added()
        if selected_opt == 13 and len(symptoms_list) > 0:
            make_diagnosis(symptoms_list)
            symptoms_list = []
        elif selected_opt == 13 and len(symptoms_list) == 0:
            ui.clear()
            ui.no_selected_sympt()

        ui.wait_for_input()
        ui.clear()


ask_for_symptom()

