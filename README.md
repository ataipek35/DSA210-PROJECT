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

  

