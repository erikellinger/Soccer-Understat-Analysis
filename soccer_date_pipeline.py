# soccer_data_pipeline.py (Understat team + player scraper for multiple seasons)

import requests
import pandas as pd
import json
import os
import re
import time

HEADERS = {"User-Agent": "Mozilla/5.0"}

# Teams by league (Understat format)
teams_by_league = {
    "Premier League": ["Arsenal", "Manchester_City", "Liverpool", "Chelsea", "Manchester_United"],
    "La Liga": ["Real_Madrid", "Barcelona", "Atletico_Madrid", "Real_Sociedad", "Sevilla"],
    "Bundesliga": ["Bayern_Munich", "Borussia_Dortmund", "Bayer_Leverkusen", "Union_Berlin"],
    "Serie A": ["Inter", "Juventus", "AC_Milan", "Roma", "Napoli"],
    "Ligue 1": ["Marseille", "Lyon", "Monaco", "Lille"]
}

# Seasons in Understat are formatted as the starting year only
seasons = ["2023", "2024"]


def scrape_understat_team(team, season):
    url = f"https://understat.com/team/{team}/{season}"
    try:
        res = requests.get(url, headers=HEADERS)
        raw = res.text
        start = raw.find("('") + 2
        end = raw.find("')")
        if start < 2 or end <= start:
            raise ValueError("No JSON data found in page")

        json_data = raw[start:end].encode('utf8').decode('unicode_escape')
        data = json.loads(json_data)
        df = pd.DataFrame(data)
        df['Team'] = team
        df['Season'] = season
        return df
    except Exception as e:
        print(f"Error scraping Understat TEAM data for {team} {season}: {e}")
        return pd.DataFrame()


def scrape_understat_players(team, season):
    url = f"https://understat.com/team/{team}/{season}"
    try:
        res = requests.get(url, headers=HEADERS)
        matches = re.findall(r"playersData\s+=\s+JSON\.parse\('([^']+)'\)", res.text)
        if not matches:
            raise ValueError("No player JSON data found")

        json_data = json.loads(matches[0].encode('utf8').decode('unicode_escape'))
        df = pd.json_normalize(json_data)
        df['Team'] = team
        df['Season'] = season
        return df
    except Exception as e:
        print(f"Error scraping Understat PLAYER data for {team} {season}: {e}")
        return pd.DataFrame()


def main():
    os.makedirs("output", exist_ok=True)
    all_team_stats = []
    all_player_stats = []

    for league, teams in teams_by_league.items():
        for season in seasons:
            print(f"Scraping Understat {league} {season}...")
            for team in teams:
                df_team = scrape_understat_team(team, season)
                if not df_team.empty:
                    df_team['League'] = league
                    all_team_stats.append(df_team)

                df_players = scrape_understat_players(team, season)
                if not df_players.empty:
                    df_players['League'] = league
                    all_player_stats.append(df_players)

                time.sleep(1)  # Be polite to the server

    if all_team_stats:
        team_df = pd.concat(all_team_stats, ignore_index=True)
        team_df.to_csv("output/understat_team_stats_2023_2024.csv", index=False)
        print("Understat team data saved.")
    else:
        print("No Understat team data to save.")

    if all_player_stats:
        player_df = pd.concat(all_player_stats, ignore_index=True)
        player_df.to_csv("output/understat_player_stats_2023_2024.csv", index=False)
        print("Understat player data saved.")
    else:
        print("No Understat player data to save.")


if __name__ == "__main__":
    main()
