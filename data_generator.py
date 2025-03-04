from faker import Faker
import random
import sqlite3

fake = Faker()

# Function to generate a student record
def generate_student():
    return {
        "name": fake.name(),
        "age": random.randint(18, 30),
        "gender": random.choice(["Male", "Female", "Other"]),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "enrollment_year": random.choice([2018, 2019, 2020, 2021]),
        "course_batch": random.choice(["Batch A", "Batch B", "Batch C"]),
        "city": fake.city(),
        "graduation_year": random.choice([2022, 2023, 2024])
    }

# Generate programming record for a student
def generate_programming(student_id):
    return {
        "student_id": student_id,
        "language": random.choice(["Python", "SQL", "JavaScript"]),
        "problems_solved": random.randint(20, 150),
        "assessments_completed": random.randint(1, 10),
        "mini_projects": random.randint(1, 5),
        "certifications_earned": random.randint(0, 3),
        "latest_project_score": round(random.uniform(50, 100), 2)
    }

# Generate soft skills record for a student
def generate_soft_skills(student_id):
    return {
        "student_id": student_id,
        "communication": random.randint(50, 100),
        "teamwork": random.randint(50, 100),
        "presentation": random.randint(50, 100),
        "leadership": random.randint(50, 100),
        "critical_thinking": random.randint(50, 100),
        "interpersonal_skills": random.randint(50, 100)
    }

# Generate placements record for a student
def generate_placement(student_id):
    status = random.choice(["Ready", "Not Ready", "Placed"])
    return {
        "student_id": student_id,
        "mock_interview_score": round(random.uniform(50, 100), 2),
        "internships_completed": random.randint(0, 3),
        "placement_status": status,
        "company_name": fake.company() if status == "Placed" else None,
        "placement_package": round(random.uniform(30000, 120000), 2) if status == "Placed" else None,
        "interview_rounds_cleared": random.randint(1, 5),
        "placement_date": fake.date_this_year().isoformat() if status == "Placed" else None
    }

# Insert a record into the Students table
def insert_student(conn, student):
    sql = '''
        INSERT INTO Students (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
        VALUES (:name, :age, :gender, :email, :phone, :enrollment_year, :course_batch, :city, :graduation_year)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, student)
    conn.commit()
    return cursor.lastrowid

# Insert a record into the Programming table
def insert_programming(conn, programming):
    sql = '''
        INSERT INTO Programming (student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score)
        VALUES (:student_id, :language, :problems_solved, :assessments_completed, :mini_projects, :certifications_earned, :latest_project_score)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, programming)
    conn.commit()

# Insert a record into the SoftSkills table
def insert_soft_skills(conn, soft_skills):
    sql = '''
        INSERT INTO SoftSkills (student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills)
        VALUES (:student_id, :communication, :teamwork, :presentation, :leadership, :critical_thinking, :interpersonal_skills)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, soft_skills)
    conn.commit()

# Insert a record into the Placements table
def insert_placement(conn, placement):
    sql = '''
        INSERT INTO Placements (student_id, mock_interview_score, internships_completed, placement_status, company_name, placement_package, interview_rounds_cleared, placement_date)
        VALUES (:student_id, :mock_interview_score, :internships_completed, :placement_status, :company_name, :placement_package, :interview_rounds_cleared, :placement_date)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, placement)
    conn.commit()

def main():
    conn = sqlite3.connect("placement.db")
    # Generate data for 100 students and corresponding records for other tables
    for _ in range(100):
        student = generate_student()
        student_id = insert_student(conn, student)

        # Generate and insert data for the related tables
        programming = generate_programming(student_id)
        soft_skills = generate_soft_skills(student_id)
        placement = generate_placement(student_id)

        insert_programming(conn, programming)
        insert_soft_skills(conn, soft_skills)
        insert_placement(conn, placement)

        print(f"Inserted data for student ID: {student_id}")

    conn.close()

if __name__ == "__main__":
    main()
