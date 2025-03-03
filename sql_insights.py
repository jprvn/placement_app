import sqlite3
import pandas as pd

def get_connection(db_file="placement.db"):
    """Establish a connection to the SQLite database."""
    return sqlite3.connect(db_file)

def average_programming_per_batch():
    """Query: Average programming performance per batch."""
    conn = get_connection()
    query = """
    SELECT s.course_batch, AVG(p.problems_solved) AS avg_problems
    FROM Students s
    JOIN Programming p ON s.student_id = p.student_id
    GROUP BY s.course_batch;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def top_5_students_ready():
    """Query: Top 5 students ready for placement based on mock interview score."""
    conn = get_connection()
    query = """
    SELECT s.name, pl.mock_interview_score
    FROM Students s
    JOIN Placements pl ON s.student_id = pl.student_id
    WHERE pl.placement_status = 'Ready'
    ORDER BY pl.mock_interview_score DESC
    LIMIT 5;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def soft_skills_distribution():
    """Query: Distribution of soft skills scores (example for communication)."""
    conn = get_connection()
    query = """
    SELECT communication, COUNT(*) AS count
    FROM SoftSkills
    GROUP BY communication;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Additional queries can be added similarly

if __name__ == '__main__':
    print("Average Programming Performance per Batch:")
    print(average_programming_per_batch())
    
    print("\nTop 5 Students Ready for Placement:")
    print(top_5_students_ready())
    
    print("\nDistribution of Communication Scores:")
    print(soft_skills_distribution())
