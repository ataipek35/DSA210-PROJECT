# Exploring Addiction-Risk in MMORPG Players  
### DSA 210 Project Proporsal

---

## Motivation  
Massively Multiplayer Online Role-Playing Games (MMORPGs) often involve long play sessions, social guild dynamics, and in-game economies that can encourage high time and financial investment. Some players while being in their 30s or older, continue to engage heavily in these games, sometimes spending thousands of turkish liras and hours on these games. This project aims to explore **addiction-risk indicators** rather than clinical addiction, focusing broadly on MMORPGs.

---

## Research Questions  
- RQ1: What behavioural patterns (in playtime, spending, social pressure) correlate with increased risk of problem-gaming in MMORPGs?  
- RQ2: How does forum/community discourse reflect addiction-risk language among MMORPG players?  
- RQ3: Can a simple risk-score model be created from survey responses and/or forum-derived features to identify higher-risk profiles?

---

## Data Sources  
1. **Public Forum Posts / Community Texts** (Secondary Data):  
   - Subreddits like r/MMORPG, r/gaming, Turkish game forums.  
   - Posts and comments containing keywords such as “can’t stop playing”, “spent too much”, “event missed”.  
2. **Anonymous Survey (Primary Data, Optional):**  
   - Age range, gender (optional)  
   - Weekly playtime, in-game spending, guild/peer pressure, feelings of control/loss.  
   - Short problem-gaming scale (5-7 items Likert 1-5).

---

## Methodology  
- **Data Collection & Cleaning:**  
  - Scrape/forum download of public posts.  
  - Removal of personal IDs, usernames; anonymisation.  
  - Survey responses gathered via Google Forms/Typeform (anonymous).  
- **Exploratory Analysis:**  
  - Summary statistics: playtime, spending distribution.  
  - Text analysis: keyword counts, sentiment distribution, topic modelling for forum posts.  
- **Modeling (if applicable):**  
  - Compute a “risk score” from survey data (sum/average of Likert items).  
  - Build a logistic regression/decision tree: high-risk vs. low-risk classification based on features (e.g., > 30 hrs/week, > €100/month spending, frequent “missed event” posts).  
- **Visualization & Reporting:**  
  - Histograms, box-plots for survey metrics.  
  - Bar charts for keyword frequencies and sentiment.  
  - Feature importance plot for model.

---

## Expected Outcomes  
- Identification of a profile of MMORPG players at elevated risk (e.g., more than X hours/week + Y spending + high peer/guild pressure).  
- Insights from community discourse about how players express loss of control, FOMO, peer obligation.  
- A deliverable “risk-score” tool (prototype) and set of visualisations to support findings.

---

## Ethical Considerations  
- Survey is anonymous and voluntary; no personally identifiable information is collected.  
- Only publicly-available forum posts are used; usernames and personal data will be removed or anonymised.  
- Results will be presented as “risk indicators” rather than clinical diagnosis.  
- All data sources will be cited and usage will respect platform terms of service.

python src/preprocess_text.py  
python src/model.py  
