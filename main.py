class Citizen:
    def __init__(self, citizen_id, citizen_name, gender, contact):
        self.citizen_id = citizen_id
        self.citizen_name = citizen_name
        self.gender = gender
        self.contact = contact

    # Display Citizen Information
    def display_citizen_info(self):
        print("=" * 60)
        print("\t\t\tCitizen Information")
        print("=" * 60)
        print(f"Citizen ID  : {self.citizen_id}")
        print(f"Citizen Name: {self.citizen_name}")
        print(f"Gender      : {self.gender}")
        print(f"Contact     : {self.contact}")


# Complaint Class
class Complaint:
    complaint_statuses = ("Pending", "Resolved", "Still In Progress")

    def __init__(self, complaint_id, complaint_type, status, description, citizen):
        self.complaint_id = complaint_id
        self.complaint_type = complaint_type
        self.status = status
        self.description = description
        self.citizen = citizen

    # Display Complaint Info
    def display_complaint_info(self):
        print(f"Complaint ID: {self.complaint_id}")
        print(f"Citizen Name: {self.citizen.citizen_name}")
        print(f"Citizen ID  : {self.citizen.citizen_id}")
        print(f"Type        : {self.complaint_type}")
        print(f"Description : {self.description}")
        print(f"Status      : {self.status}")
        print("=" * 30)

    def update_status(self, new_status):
        if new_status in Complaint.complaint_statuses:
            self.status = new_status
            print("\nStatus updated successfully.")
        else:
            print("\nInvalid status. Update failed.")


# Complaint System Class
class ComplaintSystem:

    complaint_count = 0

    def __init__(self):
        self.complaints = []

    # Class Method
    @classmethod
    def total_complaints(cls):
        return cls.complaint_count

    # Display message using a static method
    @staticmethod
    def complaint_system_message():
        print("=" * 60)
        print("\t\tCitizen Complaint Record System")
        print("=" * 60)

    # Add complaint
    def add_complaint(self):
        # Get Citizen name
        while True:
            name = input("Enter citizen name: ").strip()
            if not name:
                print("\nInput Required!")
                continue
            if not name.replace(" ", "").isalpha():
                print("\nName must be letters only.")
                continue
            break

        # Get Citizen ID
        while True:
            try:
                citizen_id = int(input("Enter citizen ID: "))

                # Check if ID already exists
                if any(c.citizen.citizen_id == citizen_id for c in self.complaints):
                    print("Citizen ID already exists. Enter a different ID.")
                    continue
                break
            except ValueError:
                print("INVALID INPUT! Please enter a number.")

        # Get citizen gender
        while True:
            gender = input("Enter citizen gender (male/female): ").strip().lower()
            if gender in ("male", "female"):
                break
            print("\nGender must be male or female.")

        # Get Citizen contact
        while True:
            contact = input("Enter citizen contact (eg:+23276000000): ").strip()
            if not contact.startswith("+232"):
                print("\nThe country code for Sierra Leone is +232")
                continue
            if not (len(contact) == 12 and contact[1:].isdigit()):
                print("\nContact must be +232 followed by 8 digits (12 characters total).")
                continue
            break

        # Get Complaint ID
        while True:
            try:
                complaint_id = int(input("Enter complaint ID: "))
            except ValueError:
                print("INVALID INPUT! Please enter a number.")
                continue
            if any(c.complaint_id == complaint_id for c in self.complaints):
                print("\nComplaint ID already exists. Enter a different one.")
                continue
            break

        # Get Complaint type
        while True:
            complaint_type = input("Enter complaint type: ").strip()
            if complaint_type:
                break
            print("\nInput Required!")

        # Get Status
        while True:
            status = input(
                f"Enter status {Complaint.complaint_statuses}: "
            ).strip().title()
            if status in Complaint.complaint_statuses:
                break
            print("Invalid status. Please choose from the available options.")

        # Get the description of the complaint
        while True:
            description = input("Enter description: ").strip()
            if description:
                break
            print("\nInput Required!")

        # Create the citizen and complaint objects
        citizen = Citizen(citizen_id, name, gender, contact)
        complaint = Complaint(complaint_id, complaint_type, status, description, citizen)

        # Add the complaint to the complaints list
        self.complaints.append(complaint)
        ComplaintSystem.complaint_count += 1
        print("\nComplaint added successfully.")

    # Display complaint records
    def display_all_complaint_records(self):
        if not self.complaints:
            print("\nNo Complaint Records Found")
            return None

        print("=" * 60)
        print("\t\tAll Complaint Records")
        print("=" * 60)
        number = 1
        for complaint in self.complaints:
            print(f"Complaint No. {number}")
            complaint.display_complaint_info()
            number += 1

        # Display total complaints
        print(f"Total Complaints: {ComplaintSystem.total_complaints()}")

    # Display the records of citizens who have filed complaints
    def display_all_citizen_records(self):
        if not self.complaints:
            print("\nNo Citizen Records Found")
            return None

        print("=" * 60)
        print("\t\tAll Citizen Records")
        print("=" * 60)
        number = 1
        for complaint in self.complaints:
            print(f"Citizen No. {number}")
            complaint.citizen.display_citizen_info()
            number += 1

    # Search for a specific complaint record
    def search_complaint_record(self):
        if not self.complaints:
            print("\nNo Complaints Record found.")
            return None

        while True:
            try:
                search_id = int(input("Enter complaint ID to search: "))
                break
            except ValueError:
                print("\nINVALID INPUT. Please enter a number.")

        # Check if complaint matches search ID
        found = False
        for complaint in self.complaints:
            if complaint.complaint_id == search_id:
                print("\nComplaint Found:")
                complaint.display_complaint_info()
                found = True
                break

        if not found:
            print(f"No complaint found with ID {search_id}.")

    # Update complaint status
    def update_complaint_status(self):
        if not self.complaints:
            print("\nNo complaints found.")
            return None

        while True:
            try:
                search_id = int(input("Enter complaint ID to update: "))
                break
            except ValueError:
                print("\nINVALID INPUT. Please enter a number.")

        # check for complaint
        for complaint in self.complaints:
            if complaint.complaint_id == search_id:
                print("These are the valid Complaint Statuses:")
                print(Complaint.complaint_statuses)
                new_status = input("Enter new status: ").strip().title()
                complaint.update_status(new_status)
                return new_status

        print(f"\nNo complaint found with ID {search_id}.")
        return None

# Display main menu function
def display_menu():
    print("=" * 60)
    print("\t\t\tMain Menu")
    print("=" * 60)
    print("1. Add Complaint")
    print("2. Display All Complaint Records")
    print("3. Display All Citizen Records")
    print("4. Search Complaint by ID")
    print("5. Update Complaint Status")
    print("6. Exit")

def main():
    system = ComplaintSystem()
    system.complaint_system_message()

    is_running = True

    while is_running:
        display_menu()
        while True:
            try:
                choice = int(input("\nChoose an option from the menu: "))
                break
            except ValueError:
                print("\nINVALID INPUT. Please enter a number.")

        if choice == 1:
            system.add_complaint()
        elif choice == 2:
            system.display_all_complaint_records()
        elif choice == 3:
            system.display_all_citizen_records()
        elif choice == 4:
            system.search_complaint_record()
        elif choice == 5:
            system.update_complaint_status()
        elif choice == 6:
            is_running = False
            print("Program Ended...")
        else:
            print("INVALID INPUT. Choose an option between 1 and 6.")

if __name__ == "__main__":
    main()