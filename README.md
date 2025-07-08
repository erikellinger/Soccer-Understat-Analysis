# ⚽ Understat Web Scraper + Analysis for Europe's Top 5 Leagues

This project scrapes match and player data from [Understat](https://understat.com/) for the top 5 European leagues — Premier League, La Liga, Bundesliga, Serie A, and Ligue 1 — covering the 2023–24 and 2024–25 seasons.

I built this to automate data collection for soccer analytics work — cutting out the need to rely on expensive or closed-off third-party sources. Everything is scraped, saved as CSV, and then explored in a Jupyter Notebook.

---

## 🔧 What's Included

### 📂 Data Pipeline
- [`soccer_data_pipeline.py`] Python script that scrapes team and player-level stats from Understat.
- Outputs:
  - [`understat_team_stats_2023_2024.csv`](./output/understat_team_stats_2023_2024.csv)
  - [`understat_player_stats_2023_2024.csv`](./output/understat_player_stats_2023_2024.csv)

### 📊 Analysis Notebook
- [`Exploring Team and Player Performance in Europe's Top 5 Leagues (Understat Data).ipynb`](./Exploring%20Team%20and%20Player%20Performance%20in%20Europe's%20Top%205%20Leagues%20(Understat%20Data).ipynb)
- Visual breakdowns of:
  - Top players by xG
  - Over- vs under-performance based on xG vs goals
  - League-wide scatterplots
  - Bonus charts for trends and comparisons

---

## 📁 Folder Structure
├── output/ # Scraped CSVs
├── soccer_data_pipeline.py # Web scraper script
├── *.ipynb # Jupyter notebook analysis
└── README.md # This file
