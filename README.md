Exploring Team and Player Performance in Europe's Top 5 Leagues (Understat Data)

This project scrapes and analyzes advanced match and player data from [Understat.com](https://understat.com) across the top five European soccer leagues:  
**Premier League, La Liga, Bundesliga, Serie A, and Ligue 1** for the **2023–2024 and 2024–2025** seasons.

## 📊 Features

- Scrapes match-level and player-level xG data from Understat
- Cleans and saves CSV outputs for teams and players
- Jupyter notebook with visualizations:
  - Top players by xG
  - Over- and under-performance vs. xG
  - xG vs. actual goals scatter plots
  - Faceted breakdowns by league

## 📁 Output Files
- `output/understat_team_stats_2023_2024.csv`
- `output/understat_player_stats_2023_2024.csv`

## 📓 Notebook
Check out the notebook:
**`Exploring Team and Player Performance in Europe's Top 5 Leagues (Understat Data).ipynb`**

It walks through:
- Data loading
- Cleaning
- Exploratory visualizations
- Insights into player performance

## ⚙️ How to Run

1. Clone the repo
2. Run `soccer_data_pipeline.py` to generate fresh data
3. Open the notebook for analysis

```bash
python soccer_data_pipeline.py
