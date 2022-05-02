import os


def show_treatment(symptom, antibiotic, recommendations):
    print("-----")
    print("Symptom: ", symptom, "\nAntibiotic: ", antibiotic, "\nRecommendations: ", recommendations[symptom])


def next_treatment():
    print("Following is the best Treatment for you: ")


def no_have_acute():
    print("Possibly, you don't have Acute liver Failure")


def show_acute_liver():
    print("You have Acute liver Failure")


def user_input():
    option = int(input())
    return option


def wait_for_input():
    input("Press Enter to continue...")


def no_selected_sympt():
    print("First you should select at least one symptom....")


def clear():
    os.system("clear")


def symptom_added():
    print("Symptom added...")


def menu():
    print("Expert System which identifies the Illness Acute liver Failure and gives a treatment")
    print("--------")
    print("Choose the symptoms the kid has: ")
    print(
        "1. Yellowing of your skin and eyeballs (jaundice)\n"
        "2. Headache\n"
        "3. Pain in your upper right abdomen\n"
        "4. Abdominal swelling (ascites)\n"
        "5. Nausea\n"
        "6. Vomiting\n"
        "7. Stomachache\n"
        "8. A general sense of feeling unwell (malaise)\n"
        "9. Disorientation or confusion\n"
        "10. Sleepiness\n"
        "11. Breath may have a musty or sweet odor\n"
        "12. Tremors\n"
        "------\n"
        "13. Make Diagnosis\n"
        "14. Exit\n"
        "Select an option: "
    )
