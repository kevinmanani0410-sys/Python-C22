patient = []


def add():
    pid = int(input("Enter Patient ID: "))

    for p1 in patient:
        if p1["PID"] == pid:
            print("Patient ID already exists")
            return

    pname = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Gender (Male/Female): ")
    disease = input("Enter Disease: ")
    phone = input("Enter Phone Number: ")

    p1 = {
        "PID": pid,
        "PName": pname,
        "Age": age,
        "Gender": gender,
        "Disease": disease,
        "Phone": phone
    }

    patient.append(p1)
    print("Patient added successfully")


def display():
    if len(patient) == 0:
        print("No patient records available")
    else:
        print("==============================================================")
        print("ID\tName\t\tAge\tGender\tDisease\t\tPhone")
        print("==============================================================")
        for p1 in patient:
            print(p1["PID"], "\t", p1["PName"], "\t\t",
                  p1["Age"], "\t", p1["Gender"], "\t",
                  p1["Disease"], "\t\t", p1["Phone"])


def search():
    pid = int(input("Enter Patient ID to search: "))
    found = 0
    for p1 in patient:
        if p1["PID"] == pid:
            found = 1
            break

    if found == 1:
        print("Patient found")
        print("Patient ID :", p1["PID"])
        print("Name       :", p1["PName"])
        print("Age        :", p1["Age"])
        print("Gender     :", p1["Gender"])
        print("Disease    :", p1["Disease"])
        print("Phone      :", p1["Phone"])
    else:
        print("Patient not found")


def update():
    pid = int(input("Enter Patient ID to update: "))
    found = 0
    for p1 in patient:
        if p1["PID"] == pid:
            found = 1
            break

    if found == 1:
        print("1. Update Name")
        print("2. Update Age")
        print("3. Update Gender")
        print("4. Update Disease")
        print("5. Update Phone")
        choice = input("Enter your choice: ")

        if choice == "1":
            p1["PName"] = input("Enter New Name: ")
            print("Name updated successfully")
        elif choice == "2":
            p1["Age"] = int(input("Enter New Age: "))
            print("Age updated successfully")
        elif choice == "3":
            p1["Gender"] = input("Enter New Gender: ")
            print("Gender updated successfully")
        elif choice == "4":
            p1["Disease"] = input("Enter New Disease: ")
            print("Disease updated successfully")
        elif choice == "5":
            p1["Phone"] = input("Enter New Phone Number: ")
            print("Phone updated successfully")
        else:
            print("Invalid choice")
    else:
        print("Patient not found")


def deletebyPID():
    pid = int(input("Enter Patient ID to delete: "))
    found = 0
    for p1 in patient:
        if p1["PID"] == pid:
            patient.remove(p1)
            found = 1
            print("Patient deleted successfully")
            break

    if found == 0:
        print("Patient not found")


def sortByAge():
    if len(patient) == 0:
        print("No patient records available")
    else:
        patient.sort(key=lambda x: x["Age"])
        print("Patients sorted by age")
        display()


def countPatient():
    print("Total number of patients:", len(patient))


def searchByDisease():
    disease = input("Enter Disease to search: ")
    found = 0
    for p1 in patient:
        if p1["Disease"].lower() == disease.lower():
            print("----------------------------------")
            print("Patient ID :", p1["PID"])
            print("Name       :", p1["PName"])
            print("Age        :", p1["Age"])
            print("Gender     :", p1["Gender"])
            print("Disease    :", p1["Disease"])
            print("Phone      :", p1["Phone"])
            found = 1

    if found == 0:
        print("No patient found with this disease")
