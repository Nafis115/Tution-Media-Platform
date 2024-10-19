# Tuition Media Platform Backend

This repository contains the backend of the **Tuition Media Platform**, a Django-based application for connecting students with tutors. The backend manages user authentication, profiles, tuition posts, tutor listings, ratings, and more.

## Features

### User Management:
- **Student and Tutor Registration**: Role-based user registration and authentication.
- **Admin**: Admin can login and manage profile.
- **Profile Management**: Separate profiles for students and tutors with editable details.
- **Password Management**: Secure password change and reset functionality.

### Tuition Management:
- **Create Tuition Posts**: Students and admin can create and manage tuition requests.
- **Tutor Listings**: Search and filter tutors based on subjects, location, class and others.
- **Reviews and Ratings**: Students can give star-based rating system for tutors.


## Technology Stack

- **Backend Framework**: Django (Python)
- **Database**: PostgreSQL
- **Media Storage**: Cloudinary (for profile pictures and documents)



## Installation

Clone the repository:

```bash
https://github.com/nafijur-rahaman/Tution-Media-Platform-Backend-
cd donation-platform-backend
```
Create a virtual environment and activate it:

```bash
py -m venv myworld
venv\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
```bash
SECRET_KEY= your_secret_key

NB: Create email for send email:

EMAIL= your_email
EMAIL_PASSWORD= your_email_pass

NB: Create a free database on supabase then fulfiled the require fields:

DB_NAME=postgres
Db_USER=
DB_PASS=
DB_HOST=aws-0-ap-southeast-1.pooler.supabase.com
DB_PORT=6543

NB: Create a fre cloud on cloudinary and then fulfiled the require fields:
CLOUD_NAME=
API_KEY=
API_SECRET_KEY=
```
Run migrate and migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
Create a superuser for the admin panel:
```bash
python manage.py createsuperuser
```
Start the development server:
```bash
python manage.py runserver
```




Visit `http://127.0.0.1:8000` to access the platform locally.



## Models

### User Models

#### `StudentModel`
Represents a student in the system, inheriting from Django's `AbstractUser`.

- **Fields**:
  - `user`: ForeignKey to the user model (Django User).
  - `education`: CharField representing the education level of the student.
  - `location`: CharField for the student's location.
  - `phone_number`: CharField for the student’s contact number.
  - `subjects`: CharField for the student's selected subjects (can select multiple).
  - `designation`: CharField (optional) for any professional titles or designations.
  - `profile_image`: ImageField for storing the student’s profile image using Cloudinary.

#### `TutorModel`
Represents a tutor in the system.

- **Fields**:
  - `user`: ForeignKey to the user model (Django User).
  - `gender`: ChoiceField based on `GENDER_CHOICES` (Male/Female).
  - `phone_number`: CharField for the tutor's contact number.
  - `location`: CharField representing the tutor’s location.
  - `salary`: IntegerField for the tutor's expected salary range.
  - `tutoring_experience`: IntegerField to record the number of years of tutoring experience.
  - `medium_of_instruction`: ChoiceField from `MEDIUM_OF_INSTRUCTION_CHOICES` to select preferred teaching medium (e.g., English, Bangla).
  - `education`: CharField for educational background.
  - `designation`: CharField for professional titles (optional).
  - `subjects`: CharField for subjects taught (allows multiple selections).
  - `profile_image`: ImageField for storing the tutor’s profile image using Cloudinary.
  - `rating`: FloatField (auto-calculated average from student reviews).

### Tuition Models

#### `TuitionPostModel`
Represents a tuition post created by a student looking for a tutor.

- **Fields**:
  - `student`: ForeignKey to the `StudentModel`, indicating who posted the tuition request.
  - `subject`: CharField for the requested subject(s).
  - `location`: CharField for where the tutoring will take place (either in-person or online).
  - `medium`: ChoiceField for the tutoring medium (in-person or online).
  - `additional_details`: TextField for any extra information about the request.
  - `created_at`: DateTimeField auto-set when the post is created.

#### `ReviewModel`
Represents a review or rating given by a student to a tutor.

- **Fields**:
  - `student`: ForeignKey to the `StudentModel` who is giving the review.
  - `tutor`: ForeignKey to the `TutorModel` being reviewed.
  - `rating`: ChoiceField for rating (1 to 5 stars) based on `STAR_CHOICES`.
  - `comment`: TextField for additional feedback from the student.
  - `created_at`: DateTimeField auto-set to the date and time the review is created.

## Database Schema

- **Users**: Stores information for both students and tutors, linked to Django’s `User` model.
- **Tuition Posts**: Contains data related to tuition requests made by students.
- **Reviews**: Stores tutor reviews and ratings from students.
- **ReviewModel**: Stores reviews and ratings given by students to tutors.

---
## API Endpoints

### Authentication

- **Student Login**  
  `POST` [https://tution-media-platform-backend.vercel.app/api/student/login/](https://tution-media-platform-backend.vercel.app/api/student/login/)
  
- **Tutor Login**  
  `POST` [https://tution-media-platform-backend.vercel.app/api/tutor/login/](https://tution-media-platform-backend.vercel.app/api/tutor/login/)
  
- **Admin Login**  
  `POST` [https://tution-media-platform-backend.vercel.app/api/admin_panel/login/](https://tution-media-platform-backend.vercel.app/api/admin_panel/login/)
  
- **Register Student**  
  `POST` [https://tution-media-platform-backend.vercel.app/api/student/register/](https://tution-media-platform-backend.vercel.app/api/student/register/)
  
- **Register Tutor**  
  `POST` [https://tution-media-platform-backend.vercel.app/api/tutor/register/](https://tution-media-platform-backend.vercel.app/api/tutor/register/)

---

### Student Endpoints

- **Get Profile**  
  `GET` [https://tution-media-platform-backend.vercel.app/api/student/list/user_id](https://tution-media-platform-backend.vercel.app/api/student/list/user_id)
  
- **Create Tuition Post**  
  `POST` [https://tution-media-platform-backend.vercel.app/api/tuition/list/](https://tution-media-platform-backend.vercel.app/api/tuition/list/)
  
- **List Tuition Posts**  
  `GET` [https://tution-media-platform-backend.vercel.app/api/tuition/list/](https://tution-media-platform-backend.vercel.app/api/tuition/list/)
  
- **Change Password**  
  `PUT` [https://tution-media-platform-backend.vercel.app/api/student/change-password/](https://tution-media-platform-backend.vercel.app/api/student/change-password/)

---

### Tutor Endpoints

- **Get Profile**  
  `GET` [https://tution-media-platform-backend.vercel.app/api/tutor/list/user_id](https://tution-media-platform-backend.vercel.app/api/tutor/list/user_id)
  
- **List of Tutors**  
  `GET` [https://tution-media-platform-backend.vercel.app/api/tutor/list/](https://tution-media-platform-backend.vercel.app/api/tutor/list/)
  
- **Update Profile**  
  `PUT` [https://tution-media-platform-backend.vercel.app/api/tutor/list/user_id](https://tution-media-platform-backend.vercel.app/api/tutor/list/user_id)
  
- **Change Password**  
  `PUT` [https://tution-media-platform-backend.vercel.app/api/tutor/change-password/](https://tution-media-platform-backend.vercel.app/api/tutor/change-password/)

---

### Tuition API Endpoints

- **Create Tuition Post**  
  `POST` [https://tution-media-platform-backend.vercel.app/api/tuition/list/](https://tution-media-platform-backend.vercel.app/api/tuition/list/)  
  *Description*: Create a new tuition post.

- **List Tuition Posts**  
  `GET` [https://tution-media-platform-backend.vercel.app/api/tuition/list/](https://tution-media-platform-backend.vercel.app/api/tuition/list/)  
  *Description*: Retrieve a list of all tuition posts.

- **Edit Tuition Post**  
  `PUT` [https://tution-media-platform-backend.vercel.app/api/tuition/list/tuitionId/](https://tution-media-platform-backend.vercel.app/api/tuition/list/tuitionId/)  
  *Description*: Update an existing tuition post.

- **Delete Tuition Post**  
  `DELETE` [https://tution-media-platform-backend.vercel.app/api/tuition/list/tuitionId](https://tution-media-platform-backend.vercel.app/api/tuition/list/tuitionId)  
  *Description*: Delete a specific tuition post.

---


### Notes

- Replace `user_id` and `tuitionId` in the URLs with the actual user or tuition post ID as required.
- Ensure you handle authentication tokens properly in your requests.





## Contact

For inquiries or support, please contact:
- **Project Developer**: Md. Nafijur Rahaman
- **Email**: tanjidnafis@gmail.com
