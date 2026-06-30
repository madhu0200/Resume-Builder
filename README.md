# Resume-Builder
# Django Resume Builder Platform

A full-stack web application built with Python and Django that automates dynamic, professional resume generation based on user inputs. The platform features robust multi-step form validation, secure user authentication, data persistence, and dynamic PDF/HTML rendering pipelines.

## 🚀 Features

* **User Authentication & State Management:** Secure registration, login, and session management using Django's built-in authentication system, allowing users to save progress and edit drafts.
* **Dynamic PDF Generation:** High-quality, dynamically rendered PDF resumes generated directly from backend data arrays using specialized Python libraries.
* **Relational Database Design:** Structured database schema managing data integrity for complex, multi-layered user profiles (e.g., separating education, skills matrices, and professional experience).
* **Robust Form Validation:** Multi-step Django forms implemented with strict backend verification to handle empty fields, edge cases, and ensure zero data loss during submission.

## 🛠️ Tech Stack

* **Backend:** Python, Django (MVT Architecture)
* **Database:** SQLite (Development) / PostgreSQL (Production)
* **PDF Generation:** ReportLab / WeasyPrint
* **Frontend:** HTML5, CSS3, Bootstrap 5

## 📊 Database Architecture

The application utilizes a relational database structure designed to maintain clean data mapping between users and their professional histories:

* `User / Profile Model`: Stores primary contact information and bio details.
* `Experience Model`: Linked via a Foreign Key to the User Profile to handle multiple chronological work entries.
* `Education Model`: Tracks academic histories dynamically.
* `Skills Model`: Categories and stores technical competencies in a structured matrix.

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/django-resume-builder.git](https://github.com/yourusername/django-resume-builder.git)
   cd django-resume-builder

## Project Screenshots
<img width="745" height="506" alt="Screenshot 2026-06-30 191308" src="https://github.com/user-attachments/assets/79069837-04ad-4830-9d78-a914d0f7b335" />
<img width="1877" height="737" alt="Screenshot 2026-06-30 191039" src="https://github.com/user-attachments/assets/09156721-5653-44cb-b2bf-618889f58d7e" />
<img width="1815" height="876" alt="Screenshot 2026-06-30 191059" src="https://github.com/user-attachments/assets/d087159b-c240-4883-a935-18013d92b697" />
<img width="1885" height="761" alt="Screenshot 2026-06-30 191125" src="https://github.com/user-attachments/assets/22226909-f888-4dc4-87be-3cea78d17dab" />
<img width="863" height="872" alt="Screenshot 2026-06-30 191231" src="https://github.com/user-attachments/assets/1dbb862b-07c5-44ac-9c35-4fd90935b2d4" />
<img width="752" height="888" alt="Screenshot 2026-06-30 191244" src="https://github.com/user-attachments/assets/ee66a5a0-e505-4875-853a-8c9e28ed11b0" />
<img width="1883" height="692" alt="Screenshot 2026-06-30 191135" src="https://github.com/user-attachments/assets/a5738f4c-4023-47e1-b4ed-02baf0027ddc" />
<img width="1887" height="551" alt="Screenshot 2026-06-30 191145" src="https://github.com/user-attachments/assets/db8e179c-7b6d-498c-baf2-249662bd2c3b" />
<img width="1877" height="861" alt="Screenshot 2026-06-30 191158" src="https://github.com/user-attachments/assets/585f8368-ef8a-4991-961a-9254b5e1a929" />
<img width="1692" height="957" alt="Screenshot 2026-06-30 191219" src="https://github.com/user-attachments/assets/a8a3be92-639b-4037-8b65-5e4a4961a95f" />

