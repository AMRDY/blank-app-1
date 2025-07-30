import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Create a directory in the cloud workspace
excel_dir = "3d_printer_requests"
os.makedirs(excel_dir, exist_ok=True)
excel_file = os.path.join(excel_dir, "3d_printer_requests.xlsx")

st.title("🖨️ 3D Printer Request Form")

with st.form("request_form"):
    name = st.text_input("Name of Requestor")
    team = st.text_input("Team Name")
    length = st.number_input("Length (mm)", min_value=0.0)
    width = st.number_input("Width (mm)", min_value=0.0)
    height = st.number_input("Height (mm)", min_value=0.0)
    weight = st.number_input("Weight (grams)", min_value=0.0)
    date = st.date_input("Date of Request", value=datetime.today())
    material = st.selectbox("Type of Material", ["PLA", "ABS", "PETG", "TPU", "Nylon", "Resin"])
    submitted = st.form_submit_button("Submit Request")

    if submitted:
        # Create data frame
        df = pd.DataFrame([{
            "Name": name,
            "Team": team,
            "Length (mm)": length,
            "Width (mm)": width,
            "Height (mm)": height,
            "Weight (g)": weight,
            "Date": date.strftime('%Y-%m-%d'),
            "Material": material
        }])

        # Append to Excel or create new
        if os.path.exists(excel_file):
            existing_df = pd.read_excel(excel_file)
            df = pd.concat([existing_df, df], ignore_index=True)

        df.to_excel(excel_file, index=False)
        st.success("✅ Request submitted successfully!")

st.info(f"📁 Excel will be saved to: `{os.path.abspath(excel_file)}`")

