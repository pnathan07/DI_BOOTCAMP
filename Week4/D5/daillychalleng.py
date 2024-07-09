# Import the necessary libraries
import pandas as pd
import sqlite3

# Connect to the IPL database
conn = sqlite3.connect('IPL_database.sqlite')

# Load and explore the data
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql_query(query, conn)
print(tables)

# Load all the tables and print their column names
for table in tables['name']:
    print(f"Table: {table}")
    query = f"PRAGMA table_info({table})"
    columns = pd.read_sql_query(query, conn)
    print(columns[['name', 'type']])
# Select all columns from the Player_Match table
query = "SELECT * FROM Player_Match;"
player_match_df = pd.read_sql_query(query, conn)
print(player_match_df.head())
# Calculate the total runs scored by each batsman
query = """
SELECT batsman, SUM(runs) as total_runs
FROM Ball_by_Ball
GROUP BY batsman
ORDER BY total_runs DESC;
"""
batsman_runs_df = pd.read_sql_query(query, conn)
print(batsman_runs_df.head())
# Calculate the number of fifties and hundreds scored by each batsman
query = """
SELECT batsman, 
       COUNT(CASE WHEN runs >= 50 AND runs < 100 THEN 1 END) AS fifties,
       COUNT(CASE WHEN runs >= 100 THEN 1 END) AS hundreds
FROM (
    SELECT batsman, match_id, SUM(runs) as runs
    FROM Ball_by_Ball
    GROUP BY batsman, match_id
) AS subquery
GROUP BY batsman
ORDER BY hundreds DESC, fifties DESC;
"""
fifties_hundreds_df = pd.read_sql_query(query, conn)
print(fifties_hundreds_df.head())
# Find the best bowling figures for each bowler
query = """
SELECT bowler, MAX(wickets) as best_figures
FROM (
    SELECT bowler, match_id, COUNT(*) as wickets
    FROM Ball_by_Ball
    WHERE dismissal_kind IN ('caught', 'bowled', 'lbw', 'stumped', 'caught and bowled', 'hit wicket')
    GROUP BY bowler, match_id
) AS subquery
GROUP BY bowler
ORDER BY best_figures DESC;
"""
best_bowling_figures_df = pd.read_sql_query(query, conn)
print(best_bowling_figures_df.head())
# Combine all previous chunks into a single comprehensive query to get detailed career metrics for players
query = """
WITH BatsmanRuns AS (
    SELECT batsman, SUM(runs) as total_runs
    FROM Ball_by_Ball
    GROUP BY batsman
),
FiftiesAndHundreds AS (
    SELECT batsman, 
           COUNT(CASE WHEN runs >= 50 AND runs < 100 THEN 1 END) AS fifties,
           COUNT(CASE WHEN runs >= 100 THEN 1 END) AS hundreds
    FROM (
        SELECT batsman, match_id, SUM(runs) as runs
        FROM Ball_by_Ball
        GROUP BY batsman, match_id
    ) AS subquery
    GROUP BY batsman
),
BestBowling AS (
    SELECT bowler, MAX(wickets) as best_figures
    FROM (
        SELECT bowler, match_id, COUNT(*) as wickets
        FROM Ball_by_Ball
        WHERE dismissal_kind IN ('caught', 'bowled', 'lbw', 'stumped', 'caught and bowled', 'hit wicket')
        GROUP BY bowler, match_id
    ) AS subquery
    GROUP BY bowler
)
SELECT p.player_id, p.player_name, br.total_runs, fh.fifties, fh.hundreds, bb.best_figures
FROM Player AS p
LEFT JOIN BatsmanRuns AS br ON p.player_name = br.batsman
LEFT JOIN FiftiesAndHundreds AS fh ON p.player_name = fh.batsman
LEFT JOIN BestBowling AS bb ON p.player_name = bb.bowler;
"""
career_metrics_df = pd.read_sql_query(query, conn)
print(career_metrics_df.head())
