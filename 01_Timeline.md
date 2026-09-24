```mermaid
gantt
    title News Credibility Model - Master Timeline
    dateFormat YYYY-MM-DD

    section Data Pipeline
    Scrape News Data        :done, d1, 2026-10-01, 5d
    Label Credibility Scores:active, d2, after d1, 7d
    Preprocess Text (NLTK)  :d3, after d2, 4d

    section Model Engineering
    Baseline TF-IDF Model   :crit, m1, after d3, 5d
    Transformer Fine-Tuning :crit, m2, after m1, 10d
    Model Evaluation        :m3, after m2, 3d

    section Deployment
    Build FastAPI Backend   :api, after m3, 5d
    Streamlit Dashboard     :after api, 4d
```
