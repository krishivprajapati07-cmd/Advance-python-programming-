class Patient:
    def __init__(self, patient_id, name, treatment_cost, category):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost
        self.category = category

    def display(self):
        print("Patient ID     :", self.patient_id)
        print("Name           :", self.name)
        print("Treatment Cost :", self.treatment_cost)
        print("Category       :", self.category)
        print("-" * 35)


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully!")

    def display_all(self):
        if len(self.patients) == 0:
            print("No patient records found.")
        else:
            print("\n===== Patient Records =====")
            for patient in self.patients:
                patient.display()


# Main Program
hospital = Hospital()

while True:
    print("\n===== Hospital Patient Management System =====")
    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        treatment_cost = float(input("Enter Treatment Cost: "))

        print("Select Patient Category:")
        print("1. General")
        print("2. Special")

        category_choice = input("Enter category: ")

        if category_choice == "1":
            category = "General"
        elif category_choice == "2":
            category = "Special"
        else:
            print("Invalid category!")
            continue

        patient = Patient(patient_id, name, treatment_cost, category)
        hospital.add_patient(patient)

    elif choice == "2":
        hospital.display_all()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")