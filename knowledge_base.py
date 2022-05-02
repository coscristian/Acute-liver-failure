from pyDatalog import pyDatalog

pyDatalog.create_terms('Treatment,Illness,symptom_of,X,Y,Z,diagnosis,treatment_of')

# Symptom - Illness
+symptom_of('Vomiting', 'any_illness')
+symptom_of('Nausea', 'any_illness')
+symptom_of('Yellow Skin', 'any_illness')
+symptom_of('Abdomen', 'any_illness')
+symptom_of('Upper Abdomen', 'any_illness')
+symptom_of('Malaise', 'any_illness')
+symptom_of('Confusion', 'any_illness')
+symptom_of('Sleepiness', 'any_illness')
+symptom_of('Breath', 'any_illness')
+symptom_of('Tremors', 'any_illness')
+symptom_of('Headache', 'any_illness')
+symptom_of('Stomachache', 'any_illness')

# Antibiotic - Symptom
+treatment_of('Bismuth subsalicylate', 'Vomiting')
+treatment_of('No', 'Nausea')
+treatment_of('No', 'Yellow Skin')
+treatment_of('PhysioRelax', 'Abdomen')
+treatment_of('PhysioRelax', 'Upper Abdomen')
+treatment_of('Tyleno', 'Malaise')
+treatment_of('No', 'Confusion')
+treatment_of('No', 'Sleepiness')
+treatment_of('Carbotural', 'Breath')
+treatment_of('No', 'Tremors')
+treatment_of('Aspirina', 'Headache')
+treatment_of('Pepto Bismol', 'Stomachache')


#Rule
diagnosis(Illness, Treatment, X) <= symptom_of(X, Y) & treatment_of(Z, X) & (Y == Illness) & (Z == Treatment)


# Rule to make the Diagnosis
def make_rule(X):
    result = diagnosis(Illness, Treatment, X)
    return result


recommendations = {
    'Vomiting':
        'Taking small sips of an oral rehydration solution (ORS) can prevent dehydration.'
        'If the vomiting stops, eating toast, crackers, gelatin, or easily digestible foods'
        'can improve an upset stomach.',
    'Nausea':
        'Resting and eating lightly seasoned foods, as well as avoiding strong food odors, '
        'perfumes, smoke, and poorly ventilated rooms, can reduce nausea. Taking motion '
        'sickness medicine can also relieve symptoms.',
    'Yellow Skin':
        'Resting and limiting salt intake to less than 2,000 milligrams a day can ease symptoms.',
    'Abdomen':
        'Drink water or other clear liquids. You can drink sports drinks in small amounts. '
        'People with diabetes should check their blood sugar regularly and adjust medications as needed.',
    'Upper Abdomen':
        'Drink water or other clear liquids. You can drink sports drinks in small amounts. '
        'People with diabetes should check their blood sugar regularly and adjust medications as needed.',
    'Malaise':
        'Maintaining regular sleep schedules, following a healthy diet, and exercising regularly can help '
        'relieve symptoms of malaise.',
    'Confusion':
        'Eating or drinking something sweet can help.',
    'Sleepiness':
        'Getting enough sleep and keeping regular sleep schedules can help ease sleep. Following a healthy'
        ' diet, exercising regularly, and avoiding caffeine at night can also help.',
    'Breath':
        'Brushing your teeth and tongue after eating, flossing at least once a day, and changing your toothbrushes'
        ' regularly can improve bad breath. Avoiding foods known to cause bad breath, such as onions and garlic, can '
        'also help.',
    'Tremors': 'Avoiding excess caffeine and limiting alcohol intake can help reduce tremor. Practicing relaxation '
               'techniques, such as massage or meditation, and doing tasks differently, such as paying bills online '
               'instead of writing checks, can also help.',
    'Headache':
        'Medications that can reduce headache pain include aspirin, acetaminophen, and ibuprofen. Resting in a dark '
        'room can also help.',
    'Stomachache':
        'Taking an antacid or anti-gas medication, in addition to eating less, can relieve heartburn or gas. Avoid '
        'aspirin, ibuprofen, and naproxen, as these medications can worsen some types of abdominal pain.'
}
