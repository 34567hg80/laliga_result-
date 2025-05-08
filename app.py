import streamlit as st
import pandas as pd

# Title and intro line
st.title("Football League Standings Analysis - La Liga")
st.markdown("This website is made with Streamlit. It explains the coding process, algorithm analysis, and the final result table. - Developed by Hritesh Ghosh")

# Author and Task
st.header("Author & Task")
st.markdown("""
**Author:** Hritesh Ghosh  
**Task:** Football League Standings Analysis (Spanish La Liga)
""")

# Overview
st.header("Overview")
st.markdown("""
This script connects to the AllSportsAPI to fetch live football standings for Spain's La Liga. It then processes the data and categorizes teams based on their positions for various European competitions and relegation.
""")

# Steps Performed
st.header("Steps Performed")
steps = [
    "1. Authenticated the API using a free key from AllSportsAPI.",
    "2. Retrieved the country_key for Spain.",
    "3. Fetched the league_id for Spanish La Liga.",
    "4. Pulled current league standings using the API.",
    "5. Converted API data into a pandas DataFrame with selected columns.",
    "6. Saved the DataFrame to an Excel file named `la_liga_standings.xlsx`.",
    "7. Created a function to analyze standings and return:",
    "   - Top 4 teams → Champions League (Group Stage)",
    "   - 5th team → Europa League (Group Stage)",
    "   - 6th team → Europa Conference League (Qualifiers)",
    "   - Bottom 3 teams → Relegation",
    "8. Output the results in a structured DataFrame."
]
for step in steps:
    st.markdown(f"- {step}")

# Algorithm Explanation
st.header("Analysis Algorithm")
st.markdown("""
**Input:**  
A Pandas DataFrame `df` containing La Liga standings with at least the columns `standing_place` and `standing_team`.

**Output:**  
A new DataFrame containing only the teams that qualify for European competitions or face relegation, along with their positions and qualification labels.

**Algorithm Steps:**
1. Convert the `standing_place` column in `df` to integer type.  
2. Sort the DataFrame `df` in ascending order by `standing_place`.  
3. Initialize an empty list `analysis`.  
4. For each row in the sorted DataFrame:  
   - Let `pos` be the value of `standing_place`.  
   - Let `team` be the value of `standing_team`.  
   - If `pos` is between 1 and 4 (inclusive), set `tag` to `"Champions League"`.  
   - Else if `pos` is equal to 5, set `tag` to `"Europa League Group Stage"`.  
   - Else if `pos` is equal to 6, set `tag` to `"Europa Conference League Qualifiers"`.  
   - Else if `pos` is greater than total number of teams - 3, set `tag` to `"Relegation"`.  
   - Otherwise, skip the team.  
   - Append a dictionary `{ 'Team': team, 'Position': pos, 'Qualification': tag }` to `analysis`.  
5. Convert the `analysis` list into a new DataFrame and return it.
""")

# Result Table
st.header("Result: La Liga Qualification Summary")

data = {
    "Team": [
        "Barcelona", "Real Madrid", "Atl. Madrid", "Ath Bilbao",
        "Villarreal", "Betis", "Las Palmas", "Leganes", "Valladolid"
    ],
    "Position": [1, 2, 3, 4, 5, 6, 18, 19, 20],
    "Qualification": [
        "Champions League", "Champions League", "Champions League", "Champions League",
        "Europa League Group Stage", "Europa Conference League Qualifiers",
        "Relegation", "Relegation", "Relegation"
    ]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
