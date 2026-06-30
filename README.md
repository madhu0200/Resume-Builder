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
