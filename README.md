# battlefield-decision-agent
An AI-powered intelligent agent that makes battlefield decisions using rule-based logic and search strategies.
# 🎖️ Battlefield Decision Agent

An AI-powered intelligent agent that analyzes battlefield conditions and recommends the best tactical decision using rule-based logic and search strategies.

---

## 📌 Problem Statement

In high-pressure battlefield scenarios, commanders must make split-second decisions with incomplete information. Poor decisions can lead to mission failure or loss of life. This project builds an AI agent that assists commanders by analyzing key battlefield inputs and recommending the most rational tactical action.

---

## 🧠 How It Works

The agent takes 4 battlefield inputs:
- **Enemy Strength** (Low / Medium / High)
- **Troop Health** (High / Medium / Low)
- **Ammunition Level** (High / Medium / Low)
- **Terrain Type** (Forest / Urban / Open)

It evaluates each input using a scoring system and maps the total score to one of 4 decisions:

| Score | Decision |
|-------|----------|
| 6 to 8 | ⚔️ Attack |
| 3 to 5 | 🛡️ Hold Position |
| 0 to 2 | 📡 Call for Support |
| Below 0 | 🚨 Retreat |

---

## 🤖 AI Concepts Used

- **Intelligent Agents** — The program acts as a goal-based agent that perceives its environment and takes action
- **Rule-Based Reasoning** — Decision logic is based on structured if-then rules
- **Search & Problem Solving** — The agent evaluates all inputs to find the optimal decision
- **Knowledge Representation** — Battlefield knowledge is encoded as weighted scoring rules

---

## 🚀 How to Run

### Requirements
- Python 3.x

### Steps
1. Clone the repository:
```
   git clone https://github.com/chanekar25bai10603-sketch/battlefield-decision-agent.git
```
2. Navigate to the folder:
```
   cd battlefield-decision-agent
```
3. Run the agent:
```
   python agent.py
```
4. Answer the 4 questions when prompted
5. The agent will display its tactical recommendation

---

## 📊 Sample Output
```
===================================================
   🎖️  BATTLEFIELD DECISION AGENT - AI System
===================================================

1. Enemy Strength   : Low
2. Troop Health     : High (75-100%)
3. Ammunition       : High
4. Terrain          : Forest

===================================================
          📊 SITUATION ANALYSIS REPORT
===================================================
  Situation Score : 9/8
  🎯 DECISION: ⚔️  ATTACK
  📌 Reason: Conditions are highly favorable.
  📋 Strategy: Move forward aggressively.
===================================================
```

---

## 👩‍💻 Author

- **Name:** Sanskruti
- **Course:** Fundamentals of AI and ML
- 
