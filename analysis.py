import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# ============= Load Data =============

CSV_FILE = "Başlıksız form.csv"
df = pd.read_csv(CSV_FILE)

df.columns = df.columns.str.strip().str.replace(r"\s+", " ", regex=True)

hours_mapping = {
    "1-3 Hours": 2,
    "3-6 Hours": 4.5,
    "6-9 Hours": 7.5
}

hours_col = "On average, how many hours per day do you spend playing MMORPGs?"
df["HoursNumeric"] = df[hours_col].map(hours_mapping)

pressure_col = (
    "I feel pressure from my guild, friends, or community to log in or stay online. "
    "(1 Star is Strongly disagree, 5 Star is Strongly agree)"
)

numeric_cols = [
    "Please enter your age:",
    "How much money do you spend on in-game MMORPG purchases per month ? (in TL)",
    pressure_col,
    "I often play longer than I originally intended.",
    "I find it difficult to stop playing even when I want to.",
    "My gaming habits sometimes interfere with my work, school, or health.",
    "I feel I spend too much money on these games.",
    "HoursNumeric"
]

df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
df_clean = df.dropna(subset=numeric_cols).copy()

# ============= Summary Statistics =============

summary_stats = df_clean[numeric_cols].describe()
summary_stats.to_csv("summary_statistics.csv")

# ============= Histograms =============

plt.hist(df_clean["HoursNumeric"], bins=10)
plt.title("Daily Playtime Distribution")
plt.xlabel("Hours per Day")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("figures/daily_playtime.png", dpi=200)
plt.close()

plt.hist(df_clean["How much money do you spend on in-game MMORPG purchases per month ? (in TL)"], bins=10)
plt.title("Monthly Spending Distribution")
plt.xlabel("Spending (TL)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("figures/monthly_spending.png", dpi=200)
plt.close()

plt.hist(df_clean["I often play longer than I originally intended."], bins=5)
plt.title("Loss of Control Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("figures/loss_of_control.png", dpi=200)
plt.close()

plt.hist(df_clean["I find it difficult to stop playing even when I want to."], bins=5)
plt.title("Difficulty Stopping Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("figures/difficulty_stopping.png", dpi=200)
plt.close()

# ============= Scatter Plot =============

plt.scatter(
    df_clean["HoursNumeric"],
    df_clean["I often play longer than I originally intended."]
)
plt.title("Hours Played per Day vs Loss of Control")
plt.xlabel("Hours per Day")
plt.ylabel("Loss of Control Score")
plt.tight_layout()
plt.savefig("figures/hours_vs_loss_of_control.png", dpi=200)
plt.close()

# ============= Correlation Matrix + Heatmap =============

corr = df_clean[numeric_cols].corr()
corr.to_csv("correlation_matrix.csv")

plt.figure(figsize=(8, 6))
im = plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar(im)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("figures/correlation_heatmap.png", dpi=200)
plt.close()

# ============= Hypothesis Testing (Pearson Correlation) =============

r1, p1 = pearsonr(
    df_clean["HoursNumeric"],
    df_clean["I often play longer than I originally intended."]
)
print("Hypothesis 1 - Hours vs Loss of Control:", "r =", round(r1, 2), "p =", round(p1, 3))

r2, p2 = pearsonr(
    df_clean["How much money do you spend on in-game MMORPG purchases per month ? (in TL)"],
    df_clean["I often play longer than I originally intended."]
)
print("Hypothesis 2 - Spending vs Loss of Control:", "r =", round(r2, 2), "p =", round(p2, 3))
