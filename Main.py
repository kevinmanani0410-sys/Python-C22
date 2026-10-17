import CrudOp as c1


while True:

    print("\n==============================================")
    print("       PATIENT RECORD MANAGEMENT SYSTEM")
    print("==============================================")
    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Sort Patients by Age")
    print("7. Count Patients")
    print("8. Search Patient by Disease")
    print("9. Exit")
    print("==============================================")

    choice = input("Enter your choice (1-9): ")
    print("----------------------------------------------")

    if choice == "1":
        c1.add()
    elif choice == "2":
        c1.display()
    elif choice == "3":
        c1.search()
    elif choice == "4":
        c1.update()
    elif choice == "5":
        c1.deletebyPID()
    elif choice == "6":
        c1.sortByAge()
    elif choice == "7":
        c1.countPatient()
    elif choice == "8":
        c1.searchByDisease()
    elif choice == "9":
        print("Thank You for using Patient Record Management System")
        break
    else:
        print("Invalid choice. Please enter between 1 and 9.")
