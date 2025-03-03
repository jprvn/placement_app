from faker import Faker
import random
import sqlite3

fake = Faker()

def generate_student():
    """Generate a single student record."""
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

def insert_student(conn, student):
    """Insert a student record into the Students table."""
    sql = '''
        INSERT INTO Students (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
        VALUES (:name, :age, :gender, :email, :phone, :enrollment_year, :course_batch, :city, :graduation_year)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, student)
    conn.commit()
    return cursor.lastrowid

def main():
    # Connect to the existing database (make sure the tables are already created)
    conn = sqlite3.connect("placement.db")
    
    # Generate and insert 100 synthetic student records
    for _ in range(100):
        student = generate_student()
        student_id = insert_student(conn, student)
        print(f"Inserted student with ID: {student_id}")
    
    conn.close()

if __name__ == "__main__":
    main()
