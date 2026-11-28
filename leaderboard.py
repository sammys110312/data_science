import pandas as pd
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index = ["NightWolf", "StarBlaze", "PixelKing", "Cyberfox", "IronStorm"])
print(players)
print()
data = {
    "Player": ["NightWolf", "StarBlaze", "PixelKing", "Cyberfox", "IronStorm"],
    "Level": [42, 38, 35, 30, 27],
    "Score": [98500, 87200, 76400, 65100, 54800],
    "Wins": [210, 185, 162, 140, 118]
}
df = pd.DataFrame(data)
print(df)
print()
print("Row 0 (Top Player)")
print(df.loc[0])
print()
print("Rows 2 & 3")
print(df.loc[2:3])
print()
full_df = pd.read_csv("leaderboard.csv")
print("First 5 rows:")
print(full_df.head())
print()
print("Last 3 rows:")
print(full_df.tail(3))
print()
print("Dataset info:")
print(full_df.info())
print()
print("Rows with missing values removed:")
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print("Missing values filled with 0")
filled_df = full_df.fillna(0)
print(filled_df.to_string())