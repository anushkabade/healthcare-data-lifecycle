import os
import pandas as pd


def load_csv(file_name: str) -> pd.DataFrame:
    """
    Safely load a CSV file if it exists.
    Returns an empty DataFrame if the file is missing.
    """
    if os.path.exists(file_name):
        print(f"✅ Loaded: {file_name}")
        return pd.read_csv(file_name)
    else:
        print(f"⚠️ Missing: {file_name} (skipped)")
        return pd.DataFrame()


def main():
    print("\n🚀 Healthcare Data Lifecycle Project\n")

    # Load CSV files (skip if missing)
    patients = load_csv("patients.csv")
    doctors = load_csv("doctors.csv")
    appointments = load_csv("appointments.csv")
    treatments = load_csv("treatments.csv")

    # Show quick summary
    if not treatments.empty:
        print("\n📊 Treatments Data Preview:")
        print(treatments.head())
    else:
        print("\n⚠️ No treatments data found.")

    if not patients.empty and not appointments.empty:
        print("\n📊 Patient & Appointment Counts:")
        print(f"Patients: {len(patients)} | Appointments: {len(appointments)}")


if __name__ == "__main__":
    main()

