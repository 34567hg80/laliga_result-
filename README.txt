
Author: Hritesh Ghosh
Task: Football League Standings Analysis (Spanish La Liga)

Overview:
---------
This script connects to the AllSportsAPI to fetch live football standings for Spain's La Liga. It then processes the data and categorizes teams based on their positions for various European competitions and relegation.

Steps Performed:
----------------
1. Authenticated the API using a free key from AllSportsAPI.
2. Retrieved the country_key for Spain.
3. Fetched the league_id for Spanish La Liga.
4. Pulled current league standings using the API.
5. Converted API data into a pandas DataFrame with selected columns.
6. Saved the DataFrame to an Excel file named `la_liga_standings.xlsx`.
7. Created a function to analyze standings and return:
   - Top 4 teams → Champions League (Group Stage)
   - 5th team → Europa League (Group Stage)
   - 6th team → Europa Conference League (Qualifiers)
   - Bottom 3 teams → Relegation
8. Output the results in a structured DataFrame.

Analysis Algorithm:
-------------------
Input:
A Pandas DataFrame df containing La Liga standings with at least the columns standing_place and standing_team.

Output:
A new DataFrame containing only the teams that qualify for European competitions or face relegation, along with their positions and qualification labels.

Algorithm Steps:
1. Convert the standing_place column in df to integer type.
2. Sort the DataFrame df in ascending order by standing_place.
3. Initialize an empty list analysis.
4. For each row in the sorted DataFrame:
(i) Let pos be the value of standing_place.
(ii) Let team be the value of standing_team.
(iii) If pos is between 1 and 4 (inclusive), set tag to "Champions League".
(iv) Else if pos is equal to 5, set tag to "Europa League Group Stage".
(v) Else if pos is equal to 6, set tag to "Europa Conference League Qualifiers".
(vi) Else if pos is greater than total number of teams - 3, set tag to "Relegation".
(vii) Otherwise, skip the team (do not include it in the analysis).
(viii) Append a dictionary { 'Team': team, 'Position': pos, 'Qualification': tag } to analysis.
5. Convert the analysis list into a new DataFrame and return it.

Dependencies:
-------------
- Python 3.x
- pandas
- requests
- openpyxl (for saving to Excel)
Note: I have created a portable BAT file named RUN.bat. Just double-click it to install the required Python libraries to run the code.

Usage:
------
1. Run the Python script named final.py
2. First, it opens a Streamlit website developed by the coder, which clearly explains the entire coding process for this project.
3. Check `la_liga_standings.xlsx` for saved data.
4. Review the printed DataFrame for qualification results.
5. The file named draft.ipynb contains the initial code experiments and rough work that formed the foundation for final.py.

Contact:
--------
Hritesh Ghosh
Email: ghoshhritesh@gmail.com


DEMO: https://baarproject.streamlit.app
