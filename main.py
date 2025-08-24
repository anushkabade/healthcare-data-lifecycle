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

    # Load CSV files (only if they exist)
    patients = load_csv("patients.csv")
    doctors = load_csv("doctors.csv")
    appointments = load_csv("appointments.csv")
    billing = load_csv("billing.csv")
    departments = load_csv("departments.csv")
    treatments = load_csv("treatments.csv")  # won't crash if missing

    # Show quick summary
    if not patients.empty and not appointments.empty:
        print("\n📊 Patient & Appointment Counts:")
        print(f"Patients: {len(patients)} | Appointments: {len(appointments)}")

    if not billing.empty:
        print("\n📊 Billing Data Preview:")
        print(billing.head())


if __name__ == "__main__":
    main()
