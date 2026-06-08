# MAN6777.3 – Activity 3: Data Analytics Portfolio
**Edith Cowan University | Data Driven Managerial Decisions | 2026 Semester 1**

---

##  Project Overview

This portfolio was completed as part of **Activity 3 (20%)** for MAN6777.3 at Edith Cowan University.

The objective was to select a real-world dataset, frame a meaningful managerial decision problem, apply appropriate data analytics techniques, and translate the findings into clear, evidence-based recommendations for a decision-maker.

---

##  Managerial Decision Problem

> **"Should universities implement a structured policy to encourage and regulate student AI tool usage in academic study, and if so, for which purposes and student groups should it be recommended?"**

**Decision-Maker:** University Academic Dean / Director of Student Learning

Universities face increasing pressure to develop evidence-based policies on student AI use. Without reliable data, institutions risk either suppressing a beneficial technology or enabling practices that undermine academic integrity. This project uses data to inform that decision.

---

##  Dataset

| Detail | Information |
|--------|-------------|
| **Dataset Name** | Students' AI Usage and Academic Performance |
| **Source** | Kaggle (2025) |
| **Link** | https://www.kaggle.com/datasets/aminasalamt/students-ai-usage-and-academic-performance |
| **Records** | 100 students |
| **Variables** | 9 (age, education level, study hours, AI usage, AI tool, purpose, grades before/after AI, screen time) |
| **Missing Values** | 0 — fully clean dataset |

---

##  Key Findings

| Finding | Result |
|---------|--------|
| AI users grade improvement | **+9.8 points** (65.3 → 75.2) |
| Non-AI users grade improvement | **+0.0 points** (64.4 → 64.4) |
| Best performing tool | Gemini (+10.8 pts) |
| Best performing purpose | Research (+10.3 pts) |
| All tools effective | ChatGPT, Copilot, Gemini all ~+10 pts |
| All purposes effective | Research, Coding, Homework all 9–10 pts |

---

##  Visualisations

The following charts were produced from the dataset using Python (matplotlib):

- **Figure 1** – Bar chart: AI vs Non-AI grade improvement
- **Figure 2** – Bar chart: Grade improvement by AI tool (ChatGPT, Copilot, Gemini)
- **Figure 3** – Bar chart: Grade improvement by purpose of AI use
- **Figure 4** – Scatter plot: Study hours vs post-AI grades with trend line

All visualisations are embedded in the submitted PDF report.

---

##  Analytical Workflow

```
Step 1 → Problem Framing & Dataset Selection
Step 2 → Data Loading & Inspection (pandas)
Step 3 → Data Preparation & Cleaning
Step 4 → Analysis & Descriptive Statistics
Step 5 → Interpretation Linked to Decision Problem
Step 6 → Limitations & Analytical Integrity
```

**Tools used:** Python, pandas, matplotlib

---

##  Recommendations

1. **Introduce an AI Adoption Policy** — Formally encourage responsible AI use across all student groups
2. **Develop AI Literacy Programs** — Provide guided training on ChatGPT, Copilot, and Gemini
3. **Integrate into Assessment Guidelines** — Publish transparent guidelines on appropriate AI use cases

---

##  Repository Contents

| File | Description |
|------|-------------|
| `MAN6777_Activity3_DataAnalyticsPortfolio.pdf` | Full submission — written report + data analytics portfolio |
| `students_ai_usage.csv` | Raw dataset used for analysis |
| `README.md` | This file |

---

##  References

- Salamt, A. (2025). *Students' AI Usage and Academic Performance* [Dataset]. Kaggle. https://www.kaggle.com/datasets/aminasalamt/students-ai-usage-and-academic-performance



