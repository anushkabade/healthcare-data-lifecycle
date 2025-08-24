import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
patients = pd.read_csv("patients.csv")
doctors = pd.read_csv("doctors.csv")
appointments = pd.read_csv("appointments.csv")
treatments = pd.read_csv("treatments.csv")

# --- Summary Statistics ---
print("=== Healthcare Management System Summary ===")
print(f"Total Patients: {len(patients)}")
print(f"Total Doctors: {len(doctors)}")
print(f"Total Appointments: {len(appointments)}")
print(f"Total Treatments: {len(treatments)}")
print("\nAverage Patient Age:", patients["Age"].mean())

# Doctor with most appointments
doctor_counts = appointments["DoctorID"].value_counts()
top_doctor_id = doctor_counts.idxmax()
top_doctor_name = doctors.loc[doctors["DoctorID"] == top_doctor_id, "Name"].values[0]
print(f"\nDoctor with Most Appointments: {top_doctor_name} ({doctor_counts.max()} appointments)")

# --- Visualization 1: Appointments per Doctor ---
plt.figure(figsize=(8,5))
appointments["DoctorID"].value_counts().plot(kind="bar")
plt.title("Appointments per Doctor")
plt.xlabel("Doctor ID")
plt.ylabel("Number of Appointments")
plt.savefig("appointments_per_doctor.png")  # saves the chart as an image
plt.show()

# --- Visualization 2: Treatment Distribution ---
plt.figure(figsize=(6,6))
treatments["Description"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Treatment Distribution")
plt.savefig("treatment_distribution.png")
plt.show()
