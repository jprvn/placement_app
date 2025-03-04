import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite Database created and connected.")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return conn

def create_tables(conn):
    """ Create the tables in the SQLite database """
    try:
        cursor = conn.cursor()
        
        # Create Students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT,
                email TEXT,
                phone TEXT,
                enrollment_year INTEGER,
                course_batch TEXT,
                city TEXT,
                graduation_year INTEGER
            );
        ''')
        
        # Create Programming table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Programming (
                programming_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                language TEXT,
                problems_solved INTEGER,
                assessments_completed INTEGER,
                mini_projects INTEGER,
                certifications_earned INTEGER,
                latest_project_score REAL,
                FOREIGN KEY(student_id) REFERENCES Students(student_id)
            );
        ''')
        
        # Create SoftSkills table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SoftSkills (
                soft_skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                communication INTEGER,
                teamwork INTEGER,
                presentation INTEGER,
                leadership INTEGER,
                critical_thinking INTEGER,
                interpersonal_skills INTEGER,
                FOREIGN KEY(student_id) REFERENCES Students(student_id)
            );
        ''')
        
        # Create Placements table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Placements (
                placement_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                mock_interview_score REAL,
                internships_completed INTEGER,
                placement_status TEXT,
                company_name TEXT,
                placement_package REAL,
                interview_rounds_cleared INTEGER,
                placement_date TEXT,
                FOREIGN KEY(student_id) REFERENCES Students(student_id)
            );
        ''')
        
        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def main():
    # Create a connection to the database file
    conn = create_connection("placement.db")
    if conn:
        # Create the tables in the database
        create_tables(conn)
        # Close the connection
        conn.close()

if __name__ == '__main__':
    main()
<<<<<<< HEAD
=======

>>>>>>> 7acd674 (Resolved merge conflicts)
