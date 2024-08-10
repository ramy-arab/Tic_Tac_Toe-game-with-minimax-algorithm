import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

rules = [

    (("fever", "cough"), "common cold"),
    (("fever", "rash"), "measles"),
    (("fever", "fatigue"), "underlying infection"),
    (("pain", "fatigue"), "chronic pain"),
    (("chest pain",), "respiratory issues "),
    (("nausea", "vomiting"), " infections"),
    (("diarrhea", "nausea"), "food poisoning"),
    (("migraines",), "headaches "),
    (("rash", "itching"), "skin conditions"),
    (("swelling", "pain"), "inflammation"),
    (("fatigue", "swelling"), "autoimmune diseases"),
    (("cough", "chest_pain"), "respiratory infections"),


    (("fever", "chronic pain"), "exhaustion"),
    (("respiratory infections", "cough"), "asthma"),
    (("headaches", "infections"),"gastrointestinal issues"),
    (("gastrointestinal issues", "food poisoning"), "gastrointestinal infections"),


    (("common cold", "measles"), "influenza"),
    (("underlying infection",), "influenza"),
    (("inflammation",), "mononucleosis"),
    (("exhaustion",), "fibromyalgia"),
    (("asthma",), "pneumonia"),
    (("respiratory infection,",), "bronchitis"),
    (("gastrointestinal infections",), "food poisoning"),
    (("gastrointestinal issues",), "stomach flu"),
    (("skin conditions",), "eczema"),
    (("inflammation",), "arthritis"),
    (("autoimmune diseases",), "rheumatoid arthritis")

]

#while True:
#    new_fact = False
 #   for rule in rules:
  #      if is_rule_applicable(rule, facts) and not all(premise in facts for premise in rule['conclusion']):
   #         apply_rule(rule, facts)
    #        new_fact = True
    #if not new_fact:
    #    break


final_results = ["influenza","mononucleosis" , "fibromyalgia" ,"pneumonia" ,"bronchitis" 
           , "food poisoning" ,"stomach flu" ,"eczema" , "arthritis" , "rheumatoid arthritis"]

def Reset () :
    result_var.set("")
    Facts.clear()
    results.clear()
    return ""

Facts = [] 
results = []

def show_results():
    result_window = tk.Toplevel()
    result_window.title("Results")
    result_window.geometry("500x300")

    tree = ttk.Treeview(result_window, columns=("diagnosis"), show="headings")
    tree.heading("diagnosis", text="Knowlege Base")

    facts_dict = {item: item for item in Facts}
    for diagnosis, probability in facts_dict.items():
        tree.insert("", "end", values=(diagnosis, probability))

    tree.pack(fill="both", expand=True)

def diagnose(symptoms):

    for x in symptoms:
        if symptoms[x] ==  True :
             Facts.append(x)  
    fact_is_added = True
    while(fact_is_added):
        print("start")
        for antecedent, diagnosis in rules:
            add = True
            for a in antecedent :
                if (a not in Facts):
                    print(a)
                    add = False        
            if(add== True and diagnosis not in Facts):
                Facts.append(diagnosis)
                if (diagnosis in final_results):
                    results.append(diagnosis)
                fact_is_added = True
                #print(diagnosis)
                #print(Facts)
                #print("breaking")
                break
            else : 
                fact_is_added = False
    #print(results)
    #print("end")
    return results

def submit_symptoms():
    fever = fever_var.get()
    cough = cough_var.get()
    rash = rash_var.get()
    fatigue = fatigue_var.get()
    chest_pain = chest_pain_var.get()
    nausea = nausea_var.get()
    vomiting = vomiting_var.get()
    diarrhea = diarrhea_var.get()
    migraines = migraines_var.get()
    itching = itching_var.get()
    swelling = swelling_var.get()
    pain = pain_var.get()






    symptoms = {
        "fever": fever,
        "cough": cough,
        "rash": rash,
        "chest_pain": chest_pain,
        "fatigue": fatigue,
        "nausea": nausea,
        "vomiting": vomiting,
        "diarrhea": diarrhea,
        "pain": pain,
        "migraines": migraines,
        "itching": itching,
        "swelling" : swelling
    }

    disease = diagnose(symptoms)

    #result_label.config(text="You may have : " + re)


    t = ', '.join(results)

    illness = "You may have : " + t if t else "pick other choices"

    result_var.set(illness)

window = tk.Tk()
window.title("Expert System Diagnosis")
window.geometry("1000x700")
window.minsize(780, 660)
#window.resizable(False,False)
#window.config(background="#41B77F")
frame = tk.Frame(window,bg='#41B77F')
frame.grid()


#label_title = tk.Label(frame, text="select symptoms",font=("Courrier",40 ),bg='#41B77F',fg='white')
#label_title.grid()


fever_var = tk.BooleanVar()
cough_var = tk.BooleanVar()
rash_var = tk.BooleanVar()
nausea_var = tk.BooleanVar()
vomiting_var = tk.BooleanVar()
diarrhea_var = tk.BooleanVar()
chest_pain_var = tk.BooleanVar()
migraines_var = tk.BooleanVar()
itching_var = tk.BooleanVar()
swelling_var = tk.BooleanVar()
pain_var = tk.BooleanVar()
fatigue_var = tk.BooleanVar()

fever_check = tk.Checkbutton(window, text="Fever", variable=fever_var,font=("Courrier",20 ))
cough_check = tk.Checkbutton(window, text="Cough", variable=cough_var,font=("Courrier",20 ))
rash_check = tk.Checkbutton(window, text="Rash", variable=rash_var,font=("Courrier",20 ))
nausea_check = tk.Checkbutton(window, text="nausea", variable=nausea_var,font=("Courrier",20 ))
vomiting_check = tk.Checkbutton(window, text="vomiting", variable=vomiting_var,font=("Courrier",20 ))
diarrhea_check = tk.Checkbutton(window, text="diarrhea", variable=diarrhea_var,font=("Courrier",20 ))
chest_pain_check = tk.Checkbutton(window, text="Chest Pain", variable=chest_pain_var,font=("Courrier",20 ))
migraines_check = tk.Checkbutton(window, text="migraines", variable=migraines_var,font=("Courrier",20 ))
itching_check = tk.Checkbutton(window, text="itching", variable=itching_var,font=("Courrier",20 ))
swelling_check = tk.Checkbutton(window, text="swelling", variable=swelling_var,font=("Courrier",20 ))
pain_check = tk.Checkbutton(window, text="pain", variable=pain_var,font=("Courrier",20 ))
fatigue_check = tk.Checkbutton(window, text="Fatigue", variable=fatigue_var,font=("Courrier",20 ))


fever_check.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")
cough_check.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")
rash_check.grid(row=3, column=0, padx=(20, 10), pady=5, sticky="w")
nausea_check.grid(row=4, column=0, padx=(20, 10), pady=5, sticky="w")
vomiting_check.grid(row=5, column=0, padx=(20, 10), pady=5, sticky="w")
diarrhea_check.grid(row=1, column=1, padx=(20, 10), pady=5, sticky="w")
chest_pain_check.grid(row=2, column=1, padx=(20, 10), pady=5, sticky="w")
migraines_check.grid(row=3, column=1, padx=(20, 10), pady=5, sticky="w")
itching_check.grid(row=4, column=1, padx=(20, 10), pady=5, sticky="w")
swelling_check.grid(row=5, column=1, padx=(20, 10), pady=5, sticky="w")
pain_check.grid(row=6, column=0, padx=(20, 10), pady=5, sticky="w")
fatigue_check.grid(row=6, column=1, padx=(20, 10), pady=5, sticky="w")





submit_button = tk.Button(window, text="Diagnose", command=submit_symptoms,font=("Courrier",30 ),bg='#41B77F',fg='white' )
reset_button = tk.Button(window, text="Reset", command=Reset,font=("Courrier",30 ),bg='#41B77F',fg='white' )
submit_button.grid()
submit_button.place(x=50, y=450)
reset_button.grid()
reset_button.place(x=700, y=450)
button = tk.Button(window, text="Show knowledge base", command=show_results,font=("Courrier",15),bg='#41B77F',fg='white')
button.grid()
button.place(x=670, y=350)




result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var, font=("Courrier",20 ),wraplength=400)
result_label.grid()
result_label.place(x=600, y=100)


window.mainloop()
