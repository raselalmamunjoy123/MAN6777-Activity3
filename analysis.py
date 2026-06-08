# my analysis for MAN6777 activity 3
# using the students AI usage dataset from kaggle
# rasel al mamun joy - 10677322

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load the data first
df = pd.read_csv('students_ai_usage.csv')

# just checking what we have
print(df.shape)
print(df.head())
print(df.columns.tolist())

# check for missing values - good habit
print(df.isnull().sum())

# i noticed that non-ai users have null in ai_tools_used and purpose_of_ai
# thats fine because they dont use ai so those fields are empty
# no actual data problems

# basic stats
print(df.describe())

# -------------------------------------------------------------------
# split into two groups - people who use ai and people who dont
# -------------------------------------------------------------------

# add improvement column before splitting
df['improvement'] = df['grades_after_ai'] - df['grades_before_ai']

ai = df[df['uses_ai'] == 'Yes'].copy()
no_ai = df[df['uses_ai'] == 'No'].copy()

print('ai users:', len(ai))
print('non ai users:', len(no_ai))

# -------------------------------------------------------------------
# compare average grades before and after
# -------------------------------------------------------------------

ai_avg_before = ai['grades_before_ai'].mean()
ai_avg_after = ai['grades_after_ai'].mean()

no_ai_avg_before = no_ai['grades_before_ai'].mean()
no_ai_avg_after = no_ai['grades_after_ai'].mean()

print('\nai users - before:', round(ai_avg_before, 1))
print('ai users - after:', round(ai_avg_after, 1))
print('improvement:', round(ai_avg_after - ai_avg_before, 1))

print('\nnon ai users - before:', round(no_ai_avg_before, 1))
print('non ai users - after:', round(no_ai_avg_after, 1))
print('improvement:', round(no_ai_avg_after - no_ai_avg_before, 1))

# -------------------------------------------------------------------
# which tool works best
# -------------------------------------------------------------------

for tool in ['ChatGPT', 'Copilot', 'Gemini']:
    group = ai[ai['ai_tools_used'] == tool]
    avg = group['improvement'].mean()
    print(f'{tool}: avg improvement = {round(avg, 1)} pts (n={len(group)})')

# -------------------------------------------------------------------
# does the purpose matter
# -------------------------------------------------------------------

for p in ['Research', 'Homework', 'Coding']:
    group = ai[ai['purpose_of_ai'] == p]
    avg = group['improvement'].mean()
    print(f'{p}: avg improvement = {round(avg, 1)} pts (n={len(group)})')

# -------------------------------------------------------------------
# charts
# -------------------------------------------------------------------

# chart 1 - main comparison ai vs non ai
fig, ax = plt.subplots(figsize=(7, 4))

groups = ['AI Users (n=40)', 'Non-AI Users (n=60)']
before_vals = [round(ai_avg_before, 1), round(no_ai_avg_before, 1)]
after_vals  = [round(ai_avg_after, 1),  round(no_ai_avg_after, 1)]

x = np.arange(len(groups))
width = 0.35

bars1 = ax.bar(x - width/2, before_vals, width, label='Before', color='lightgray', edgecolor='white')
bars2 = ax.bar(x + width/2, after_vals,  width, label='After',  color=['steelblue', 'coral'], edgecolor='white')

# add numbers on top of bars
for b, v in zip(bars1, before_vals):
    ax.text(b.get_x() + b.get_width()/2, v + 0.4, str(v), ha='center', fontsize=9)
for b, v in zip(bars2, after_vals):
    ax.text(b.get_x() + b.get_width()/2, v + 0.4, str(v), ha='center', fontsize=9, fontweight='bold')

ax.set_title('Grade Improvement: AI Users vs Non-AI Users')
ax.set_ylabel('Average Grade (%)')
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.set_ylim(55, 85)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('chart1_ai_vs_nonai.png', dpi=150)
plt.close()
print('saved chart 1')

# chart 2 - by tool
tools = ['ChatGPT', 'Copilot', 'Gemini']
tool_avgs = []
for t in tools:
    g = ai[ai['ai_tools_used'] == t]
    tool_avgs.append(round(g['improvement'].mean(), 1))

fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(tools, tool_avgs, color=['#2196F3', '#1565C0', '#64B5F6'], width=0.5, edgecolor='white')
for b, v in zip(bars, tool_avgs):
    ax.text(b.get_x() + b.get_width()/2, v + 0.2, f'+{v} pts', ha='center', fontsize=10, fontweight='bold')
ax.set_title('Grade Improvement by AI Tool')
ax.set_ylabel('Average Improvement (points)')
ax.set_ylim(0, 14)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('chart2_by_tool.png', dpi=150)
plt.close()
print('saved chart 2')

# chart 3 - by purpose
purposes = ['Research', 'Coding', 'Homework']
purpose_avgs = []
for p in purposes:
    g = ai[ai['purpose_of_ai'] == p]
    purpose_avgs.append(round(g['improvement'].mean(), 1))

fig, ax = plt.subplots(figsize=(6, 4))
colors = ['#4CAF50', '#1565C0', '#FF7043']
bars = ax.bar(purposes, purpose_avgs, color=colors, width=0.5, edgecolor='white')
for b, v in zip(bars, purpose_avgs):
    ax.text(b.get_x() + b.get_width()/2, v + 0.2, f'+{v} pts', ha='center', fontsize=10, fontweight='bold')
ax.set_title('Grade Improvement by Purpose of AI Use')
ax.set_ylabel('Average Improvement (points)')
ax.set_ylim(0, 14)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('chart3_by_purpose.png', dpi=150)
plt.close()
print('saved chart 3')

# chart 4 - scatter plot study hours vs grades
# wanted to see if studying more hours also helps when using ai
fig, ax = plt.subplots(figsize=(7, 4))

ax.scatter(no_ai['study_hours_per_day'], no_ai['grades_after_ai'],
           color='lightgray', edgecolors='gray', alpha=0.6, s=50, label='Non-AI Users')
ax.scatter(ai['study_hours_per_day'], ai['grades_after_ai'],
           color='steelblue', edgecolors='navy', alpha=0.7, s=60, label='AI Users')

# add a trend line just for ai users
z = np.polyfit(ai['study_hours_per_day'], ai['grades_after_ai'], 1)
p = np.poly1d(z)
x_line = np.linspace(ai['study_hours_per_day'].min(), ai['study_hours_per_day'].max(), 100)
ax.plot(x_line, p(x_line), color='navy', linestyle='--', linewidth=1.5, label='AI trend')

ax.set_xlabel('Study Hours per Day')
ax.set_ylabel('Grade After AI (%)')
ax.set_title('Study Hours vs Post-AI Grades')
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('chart4_scatter.png', dpi=150)
plt.close()
print('saved chart 4')

# -------------------------------------------------------------------
# summary of findings
# -------------------------------------------------------------------

print('\n--- SUMMARY ---')
print(f'AI users improved by +{round(ai_avg_after - ai_avg_before, 1)} pts on average')
print(f'Non-AI users improved by +{round(no_ai_avg_after - no_ai_avg_before, 1)} pts')
print('all 3 tools gave roughly the same improvement')
print('all 3 purposes also gave similar results')
print('conclusion: university should encourage AI tool use with proper guidelines')
