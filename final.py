# Opens a website that explains the coding process for this project, developed and hosted by the coder using Streamlit - Written by Hritesh Ghosh
import webbrowser; webbrowser.open_new_tab('https://baarproject.streamlit.app/')

# Import required libraries - Written by Hritesh Ghosh
import requests  # For API requests - Written by Hritesh Ghosh
import pandas as pd  # For data manipulation and analysis - Written by Hritesh Ghosh

# API Key and Base URL for AllSportsAPI - Written by Hritesh Ghosh
API_KEY = '413d101d1e60dd334ffe8202781937d45e25044e9defea1db882eec3962bb31f'
BASE_URL = 'https://apiv2.allsportsapi.com/football/'

# Step 1: Fetch the country_key for Spain - Written by Hritesh Ghosh
def get_country_key(country_name):
    response = requests.get(BASE_URL, params={'met': 'Countries', 'APIkey': API_KEY})
    if response.status_code != 200:
        print("Failed to fetch countries.")
        return None
    countries = response.json().get('result', [])
    for country in countries:
        if country.get('country_name', '').lower() == country_name.lower():
            return country.get('country_key')
    return None

# Step 2: Fetch the league_id for the Spanish La Liga using the country_key - Written by Hritesh Ghosh
def get_league_id(country_key, league_names):
    for league_name in league_names:
        response = requests.get(BASE_URL, params={'met': 'Leagues', 'APIkey': API_KEY, 'countryId': country_key})
        if response.status_code != 200:
            print("Failed to fetch leagues.")
            return None
        leagues = response.json().get('result', [])
        for league in leagues:
            if league.get('league_name', '').lower() == league_name.lower():
                return league.get('league_key') or league.get('league_id')
    return None

# Step 3: Fetch current standings data for the La Liga using league_id - Written by Hritesh Ghosh
def get_standings(league_id):
    response = requests.get(BASE_URL, params={'met': 'Standings', 'APIkey': API_KEY, 'leagueId': league_id})
    if response.status_code != 200:
        print("Failed to fetch standings.")
        return {}
    result = response.json().get('result', {})
    if result:
        print("\nAvailable keys in standings result:", result.keys())
    return result

# Step 4: Convert JSON standings section into a structured DataFrame - Written by Hritesh Ghosh
def create_standings_df(standings_section):
    df = pd.DataFrame(standings_section)
    print("\nAvailable columns:")
    print(df.columns.tolist())

    # Define and select the expected columns - Written by Hritesh Ghosh
    expected_cols = [
        'standing_place', 'standing_team', 'standing_P', 'standing_W',
        'standing_D', 'standing_L', 'standing_F', 'standing_A',
        'standing_GD', 'standing_PTS', 'team_key', 'league_key',
        'league_season', 'league_round', 'standing_updated'
    ]
    available_cols = [col for col in expected_cols if col in df.columns]
    if not available_cols:
        raise ValueError("No expected columns found in standings data.")
    return df[available_cols]

# Step 5: Save the collected standings data to an Excel file - Written by Hritesh Ghosh
def save_to_excel(dfs_dict, filename='la_liga_standings.xlsx'):
    with pd.ExcelWriter(filename) as writer:
        for sheet_name, df in dfs_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print(f"\nStandings saved to {filename}")

# Step 6: Analyze standings to assign European qualifications and relegation - Written by Hritesh Ghosh
def analyze_standings(df):
    # Convert positions to integer and sort accordingly - Written by Hritesh Ghosh
    df['standing_place'] = df['standing_place'].astype(int)
    df = df.sort_values(by='standing_place')
    analysis = []

    # Step-by-step classification based on position - Written by Hritesh Ghosh
    for _, row in df.iterrows():
        pos = row['standing_place']
        team = row['standing_team']
        if pos <= 4:
            tag = "Champions League"
        elif pos == 5:
            tag = "Europa League Group Stage"
        elif pos == 6:
            tag = "Europa Conference League Qualifiers"
        elif pos > len(df) - 3:
            tag = "Relegation"
        else:
            continue
        analysis.append({'Team': team, 'Position': pos, 'Qualification': tag})

    return pd.DataFrame(analysis)

# Step 7: Main driver function to coordinate all steps - Written by Hritesh Ghosh
def main():
    # Get country key for Spain - Written by Hritesh Ghosh
    country_key = get_country_key('Spain')
    if not country_key:
        print("Couldn't fetch country key.")
        return
    print(f"\n Country Key for Spain: {country_key}")

    # Get league ID for Spanish La Liga - Written by Hritesh Ghosh
    league_id = get_league_id(country_key, ['La Liga', 'Primera Division'])
    if not league_id:
        print("Couldn't fetch league ID.")
        return
    print(f"\nLeague ID for Spanish La Liga: {league_id}")

    # Fetch standings data - Written by Hritesh Ghosh
    standings = get_standings(league_id)
    if not standings or 'total' not in standings:
        print("No standings data found.")
        return

    # Process 'total', 'home', and 'away' standings (if available) - Written by Hritesh Ghosh
    dfs = {}
    for section in ['total', 'home', 'away']:
        if section in standings:
            try:
                df_section = create_standings_df(standings[section])
                dfs[section.capitalize()] = df_section
                print(f"\nStandings Data - {section.capitalize()}:\n", df_section)
            except Exception as e:
                print(f"Skipping {section} due to error: {e}")

    # Save standings to Excel file - Written by Hritesh Ghosh
    if not dfs:
        print("No valid standings data to save.")
        return
    save_to_excel(dfs)

    # Analyze the Total standings to determine qualifications - Written by Hritesh Ghosh
    if 'Total' in dfs:
        analysis_df = analyze_standings(dfs['Total'])
        print("\n--- La Liga Qualification Summary ---")
        print(analysis_df.to_string(index=False)) 

# Execute the main function - Written by Hritesh Ghosh
if __name__ == "__main__":
    main()
