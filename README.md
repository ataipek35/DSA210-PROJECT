# Exploring Addiction-Risk in MMORPG Players  
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
   - Subreddits like r/MMORPG, r/gaming, Turkish game forums.  
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
  - Charts and insights will be created with python to show trends in gaming habits and risk indicators.  
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
