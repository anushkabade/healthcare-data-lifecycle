import pandas as pd

def load_data():
    try:
        patients = pd.read_csv("patients.csv")
        doctors = pd.read_csv("doctors.csv")
        appointments = pd.read_csv("appointments.csv")
        treatments = pd.read_csv("treatments.csv")
        return patients, doctors, appointments, treatments
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit()

def show_summary(patients, doctors, appointments, treatments):
    print("\n--- Healthcare Data Lifecycle Summary ---\n")

    print(f"Total Patients: {len(patients)}")
    print(f"Total Doctors: {len(doctors)}")
    print(f"Total Appointments: {len(appointments)}")
    print(f"Total Treatments: {len(treatments)}\n")

    print("Sample Patients:")
    print(patients.head(), "\n")

    print("Sample Doctors:")
    print(doctors.head(), "\n")

    print("Appointments Overview:")
    print(appointments.head(), "\n")

    print("Treatments Overview:")
    print(treatments.head(), "\n")

    # Extra insights
    print("Appointments per Doctor:")
    print(appointments['doctor_id'].value_counts(), "\n")

    print("Appointments per Patient:")
    print(appointments['patient_id'].value_counts(), "\n")

if __name__ == "__main__":
    patients, doctors, appointments, treatments = load_data()
    show_summary(patients, doctors, appointments, treatments)
