# Exploring Addiction-Risk in MMORPGs
### DSA 210 Project Proposal

---

## Motivation  
Massively Multiplayer Online Role-Playing Games (MMORPGs) often involve long play sessions, social guild dynamics, and in-game economies that encourage significant time and financial investment. Some people, even in their 30s or older, continue to engage heavily in these types of games. This project aims to explore why players spend thousands of hours and large amounts of money on MMORPGs, even when they don’t have much free time or disposable income.

In this project, i want to find out that,

- What behavioural patterns (in playtime, spending, social pressure) correlate with increased risk of problem-gaming in MMORPGs? 
- How does forum/community discourse reflect addiction-risk language among MMORPG players?  
- Can a simple risk-score model be created from survey responses and/or forum-derived features to identify higher-risk profiles?

---

## Data Sources  
1. **Public Forum Posts / Community Texts** (Secondary Data):  
   - Subreddits like r/MMORPG, r/gaming, game forums.  
   - Posts and comments containing keywords such as “can’t stop playing”, “spent too much”, “event missed”.  
2. **Anonymous Survey (Primary Data):**  
   - Age range, gender   
   - Weekly playtime, in-game spending, guild/peer pressure, feelings of control/loss.  
   - A short set of 5–7 questions rated from 1 (strongly disagree) to 5 (strongly agree) to measure how difficult it is for players to control their gaming habits.

---

## Methodology  
- **Data Collection & Cleaning:**  
  - Scrape/forum download of public posts.  
  - Removal of personal IDs, usernames; anonymisation.  
  - Survey responses gathered via Google Forms (anonymous).  
- **Exploratory Analysis:**  
  - Summary statistics: playtime, spending distribution.  
  - Text analysis: keyword counts, sentiment distribution, topic modelling for forum posts.  
- **Modeling:**  
  - Compute a “risk score” from survey data using sum/average of results.  
  - Build a logistic decision tree: high-risk vs. low-risk classification based on features (e.g., > 30 hrs/week, > €100/month spending, frequent “missed event” posts).  
- **Visualization & Reporting:**  
  - Charts and insights will be created with python (pandas, matplotlib, seaborn) to show trends in gaming habits and risk indicators.  
  - Findings will be summarized in tables and visual plots for clear interpretation.

---

## Expected Outcomes  
- Identification of a profile of MMORPG players at elevated risk (e.g., more than X hours/week + Y spending + high peer/guild pressure).  
- Insights from community discourse about how players express loss of control.  
- A deliverable “risk-score” tool (prototype) and set of visualisations to support findings.

---

## Ethical Considerations  
- Survey is anonymous and voluntary; no personally identifiable information is collected.  
- Only publicly-available forum posts are used; usernames and personal data will be removed or anonymised.  
- Results will be presented as “risk indicators” rather than clinical diagnosis. Just my personal thoughts and results of the topic.
- All data sources will be cited.

# Data Collection
Data for this project was gathered using both primary and secondary sources to better understand addiction-risk behaviors in MMORPG players.

## Primary Data (Survey Responses)

A total of 22 participants completed an anonymous online survey created using Google Forms.
The survey collected information about players’ demographic characteristics (age), daily playtime, monthly in-game spending, and a series of Likert-scale questions designed to measure key addiction-risk indicators such as:

loss of control,

difficulty stopping,

guilt or anxiety after missing events,

interference with daily life,

perceived social or guild pressure.

All responses were exported as a CSV file and processed in Python.
After removing incomplete or non-numeric entries, 11 fully-completed cases remained and were used in the statistical analysis and hypothesis testing.

 ## Secondary Data (Community Forum Posts)

To complement the survey data, additional qualitative insights were collected from public online forums such as Reddit’s r/MMORPG community.
Posts discussing topics like “can’t stop playing,” “MMOs are designed to be addictive,” and “spent too much on the game” were manually reviewed.
Players often describe MMORPGs as intentionally built around continuous reward systems (e.g., levels, cosmetics, mounts) and strong social expectations from guilds, which aligns with established research on MMORPG engagement patterns.

These forum posts were used as secondary qualitative data to contextualize the survey findings and illustrate how players themselves talk about addictive design, social pressure, and loss-of-control experiences.

 ## Ethical Considerations

All survey responses were anonymous and voluntary.
Forum posts used were publicly accessible and no usernames or identifying information were recorded.
Data was cleaned and anonymized before analysis.

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis was conducted on the cleaned subset of 11 complete survey responses.
The goal of this stage was to examine the distribution of key behavioral variables (playtime, spending, pressure, loss-of-control indicators) and identify preliminary patterns that may relate to addiction-risk in MMORPG players.

# Summary Statistics of Survey Variables {Google Forms} (n = 11; total collected = 22)

Table 1 reports descriptive statistics for all numeric variables, including age, daily playtime (converted to numeric midpoints), monthly spending, and all Likert-scale addiction-risk indicators.

Table 1
| Variable                            | Mean   | Std    | Min | 25% | 50% | 75%  | Max  |
| ----------------------------------- | ------ | ------ | --- | --- | --- | ---- | ---- |
| **Age**                             | 23.36  | 3.69   | 19  | 21  | 21  | 25.5 | 31   |
| **Monthly Spending (TL)**           | 616.36 | 750.56 | 0   | 90  | 200 | 600  | 2000 |
| **Guild/Social Pressure (1–5)**     | 2.45   | 1.37   | 1   | 1   | 2   | 4    | 5    |
| **Play longer than intended (1–5)** | 3.36   | 1.43   | 1   | 2   | 4   | 4    | 5    |
| **Difficulty stopping (1–5)**       | 3.45   | 1.69   | 1   | 1   | 4   | 4    | 5    |
| **Interference with life (1–5)**    | 3.18   | 1.60   | 1   | 1   | 4   | 4    | 5    |
| **Spending concern (1–5)**          | 2.36   | 1.56   | 1   | 1   | 2   | 4    | 5    |
| **Hours played per day (numeric)**  | 5.41   | 2.20   | 2   | 4.5 | 4.5 | 7.5  | 7.5  |

Key observations from the table:

- Average age of participants was 23.36, with a range from 19 to 31.
- Daily playtime averaged 5.41 hours, indicating relatively high engagement.
- Monthly spending showed large variability (mean = 616 TL, SD = 750 TL), suggesting that spending behavior differs significantly across players.
- Loss-of-control indicators (e.g., “I play longer than intended”, “I find it difficult to stop”) have mean values between 3.18 and 3.45, suggesting a tendency toward moderate-to-high levels of compulsive play.
- Guild/social pressure had a mean of 2.45, but some participants reported the maximum value of 5, indicating meaningful pressure for certain players.

## Distribution Analysis (Histograms)

Distribution plots were generated for the major behavioral variables:

- Daily Playtime Distribution

The distribution showed clustering around 3–6 hours and 6–9 hours, indicating that most participants engage in long daily sessions typical of MMORPG players.

- Monthly Spending Distribution

Spending data was right-skewed, with most players spending modest amounts (0–200 TL), while a few users reported much higher spending (up to 2,000 TL).

This heavy-tailed pattern is consistent with MMO monetization patterns where a minority of players contribute disproportionately to in-game revenue.

- Loss of Control & Difficulty Stopping (Likert-scale)

Both variables showed mid-to-high distributions, with a notable number of participants selecting 4 or 5, indicating difficulty regulating playtime.

These distribution results suggest that several players within the sample show elevated behavioral patterns commonly associated with problem gaming.

## Relationship Exploration (Scatter Plot)

A scatter plot was generated to examine the relationship between:

- Daily playtime (hours)

- Loss-of-control score

Visual inspection indicated a positive trend, with higher playtime corresponding to elevated loss-of-control levels.
Although this does not confirm causation, it provides preliminary support for testing the hypothesis that longer daily play sessions correlate with increased addiction-risk.

## Correlation Analysis
To further examine relationships between behavioral variables, a Pearson correlation analysis was conducted using the cleaned dataset (n = 11). The correlation matrix included daily playtime (numeric midpoint), monthly spending, and several addiction-risk indicators such as loss of control, difficulty stopping, and interference with daily life.

Key Findings:

- Daily Playtime → Loss of Control:
A positive relationship was observed, indicating that players who spend more hours per day tend to report higher levels of loss of control.

- Daily Playtime → Difficulty Stopping:
A similar positive correlation emerged, suggesting that increased daily engagement is associated with greater difficulty disengaging from gameplay.

- Monthly Spending → Loss of Control:
A moderate positive relationship was identified, meaning players who spend more money in-game are also more likely to experience loss-of-control behaviors.

- Guild/Social Pressure → Interference with Daily Life:
A noticeable relationship was found between social pressure and negative impacts on work, school, or health.

- Addiction-Risk Indicators Correlate with Each Other:
Variables such as loss of control, difficulty stopping, and interference with life showed meaningful positive correlations, suggesting they measure overlapping aspects of problematic gaming patterns.

# Hypothesis Testing

Two statistical hypothesis tests were conducted to examine whether key behavioral variables—such as daily playtime and monthly spending—are associated with addiction-risk indicators in MMORPG players. Both tests use Pearson’s correlation coefficient on the cleaned dataset (n = 11).

## Hypothesis 1: Daily playtime increases loss-of-control levels
Research Question:

Does spending more hours per day playing MMORPGs relate to higher levels of loss of control?

Hypotheses:

- H₀ (Null Hypothesis):
There is no significant relationship between daily playtime and loss-of-control scores.

- H₁ (Alternative Hypothesis):
There is a significant positive relationship: as daily playtime increases, loss-of-control scores also increase.

### Statistical Test  
**Pearson Correlation Coefficient**

```python
from scipy.stats import pearsonr
pearsonr(df_clean["HoursNumeric"], df_clean["I often play longer than I originally intended."])
```
Result:
- r = 0.52
- p = 0.089

## Interpretation:

Since p > 0.05, we fail to reject the null hypothesis.
Although the correlation is moderately positive (r = 0.52), the relationship is not statistically significant at the 5% level.
This means that within this sample, players who spend more hours per day tend to report more loss-of-control.
However, the evidence is not strong enough to confirm the relationship statistically.

## Hypothesis 2: In-game spending predicts loss-of-control levels
Research Question:

Do players who spend more money on MMORPGs report higher loss-of-control behaviors?

Hypotheses:

- H₀:
There is no significant relationship between monthly spending and loss-of-control.

- H₁:
Higher monthly spending is positively associated with loss-of-control.

### Statistical Test  
**Pearson Correlation Coefficient**

```python
pearsonr(df_clean["How much money do you spend on in-game MMORPG purchases per month ? (in TL)"], df_clean["I often play longer than I originally intended."])
```
Result:

- r = 0.47
- p = 0.132

## Interpretation

Again, p > 0.05, so we fail to reject H₀.
There is a moderate positive trend, meaning players who spend more money tend to report more loss-of-control, but this finding is not statistically significant.

This result also suggests that monetary spending alone may not fully explain addiction-risk and likely interacts with social features, game design, or player motivations.



  

