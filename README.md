# VisualAttend – AI‑Powered Attendance System


## Overview

**VisualAttend** is an AI‑powered attendance system that eliminates the need for manual roll‑call. Teachers can capture or upload a single classroom photograph, and the system instantly records attendance for all students in the image.

---

## Key Features

- **Instant Face‑Based Attendance** – Detects and recognizes multiple students from one classroom image.
- **High‑Accuracy Face Recognition** – Utilises **dlib‑bin** and **face_recognition_models** to generate reliable facial encodings that work under varied lighting and angles.
- **Teacher Portal** – Manage subjects, upload classroom photos, run AI‑powered attendance, and export attendance records.
- **Student Dashboard** – View enrolled courses, attendance history, present/absent statistics, and real‑time attendance percentages.
- **Cloud‑Based Data Management** – Powered by **Supabase** for secure storage and real‑time sync of attendance data.
- **Responsive Web Application** – Built with **Streamlit** for a fast, intuitive, and accessible UI.

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| **Language** | Python |
| **AI Libraries** | NumPy, dlib‑bin, face_recognition_models, Pillow |
| **Database & Cloud** | Supabase |
| **Web Framework** | Streamlit |

---

## Live Demo

[VisualAttend Demo](https://visualattendlanding.vercel.app)  <!-- URL kept from the reference; replace with your own if available -->


## Repository

[GitHub – VisualAttend](https://github.com/PreethamAcharya86/VisualAttend)

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/PreethamAcharya86/VisualAttend.git
   cd VisualAttend
   ```
2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   .\\venv\\Scripts\\activate   # Windows
   pip install -r requirements.txt
   ```
3. **Configure Supabase** – Add your Supabase URL and anon key to a `.env` file (see `example.env`).
4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---