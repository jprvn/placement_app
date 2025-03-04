import streamlit as st
import sqlite3
import pandas as pd

# Function to get a connection to the database
def get_connection():
    return sqlite3.connect("placement.db")

st.title("Placement Eligibility Dashboard")

# Sidebar for eligibility criteria
st.sidebar.header("Eligibility Criteria")
min_problems = st.sidebar.number_input("Minimum Problems Solved", min_value=0, value=50)
min_soft_score = st.sidebar.number_input("Minimum Average Soft Skills Score", min_value=0, value=75)

# Connect to the database and run a query to filter eligible candidates
conn = get_connection()
query = f"""
    SELECT s.student_id, s.name, p.problems_solved, 
           (ss.communication + ss.teamwork + ss.presentation + ss.leadership + ss.critical_thinking + ss.interpersonal_skills)/6.0 as avg_soft_score,
           pl.mock_interview_score, pl.placement_status
    FROM Students s
    JOIN Programming p ON s.student_id = p.student_id
    JOIN SoftSkills ss ON s.student_id = ss.student_id
    JOIN Placements pl ON s.student_id = pl.student_id
    WHERE p.problems_solved >= {min_problems}
      AND ((ss.communication + ss.teamwork + ss.presentation + ss.leadership + ss.critical_thinking + ss.interpersonal_skills)/6.0) >= {min_soft_score}
"""
df = pd.read_sql_query(query, conn)
conn.close()

st.subheader("Eligible Students")
st.dataframe(df)

st.write("### Additional Insights")
st.write("Use the SQL queries provided in the documentation for deeper analysis.")


import streamlit as st
from sql_insights import average_programming_per_batch, top_5_students_ready

st.write("## Average Programming Performance per Batch")
st.dataframe(average_programming_per_batch())

st.write("## Top 5 Students Ready for Placement")
st.dataframe(top_5_students_ready())
