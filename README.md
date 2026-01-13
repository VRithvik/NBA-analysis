<div align="center">

<h1>🏀 NBA Players Analysis Dashboard</h1>

<p>
  <b>Interactive NBA data visualization app (1996–2023)</b><br>
  Built with <b>Python Shiny</b>, <b>Pandas</b>, and <b>Plotly</b>
</p>

<img src="https://img.shields.io/badge/Python-3.9+-blue.svg">
<img src="https://img.shields.io/badge/Shiny-Python-brightgreen.svg">
<img src="https://img.shields.io/badge/Plotly-Interactive-orange.svg">
<img src="https://img.shields.io/badge/Status-Active-success.svg">

<br><br>

</div>

---

## 📌 Overview

The **NBA Players Analysis Dashboard** is an interactive web application that allows users to explore **NBA player and team statistics from 1996 to 2023**.  
It provides season-wise insights, comparisons, global player distribution, and individual player performance trends using modern visualizations.

---

## ✨ Key Features

### 🧾 Season Highlights
- Select any NBA season from **1996–2023**
- Dynamic stat cards showing:
  - 🏆 Most Games Played
  - 🔥 Highest Average Points
  - 🎯 Highest Average Assists
  - 📈 Best Net Rating

---

### 🏟️ Team Performance Analysis
- Average points per team (bar chart)
- Compare two different seasons interactively
- Clear, sortable, and visually engaging charts

---

### 🌍 Global Player Distribution
- Interactive world map (choropleth)
- Shows number of NBA players by country
- Compare international representation across seasons

---

### 📊 Usage vs Scoring
- Scatter plot showing relationship between:
  - Usage Percentage (USG%)
  - Average Points Per Game
- Helps identify high-usage, high-impact players

---

### 👤 Player Performance Tracker
- Select any NBA player
- View season-by-season trends:
  - 📉 Average Points
  - 🏀 Average Rebounds
  - 🎯 Average Assists
- Smooth interactive line charts

---

## 🛠️ Tech Stack

<ul>
  <li><b>Python</b></li>
  <li><b>Shiny for Python</b></li>
  <li><b>Pandas</b> – data processing</li>
  <li><b>Plotly Express</b> – interactive charts</li>
  <li><b>shinywidgets</b> – Plotly rendering</li>
  <li><b>faicons</b> – UI icons</li>
</ul>

---

## 📁 Project Structure

<pre>
nba-shiny-analysis/
│
├── app.py                # Main Shiny app
├── nba_players.csv       # Dataset
├── README.md             # Documentation
└── requirements.txt      # Dependencies
</pre>

---

## 📊 Dataset Information

<b>File:</b> <code>nba_players.csv</code>

<b>Includes:</b>
<ul>
  <li>Player Name</li>
  <li>Season</li>
  <li>Team Abbreviation</li>
  <li>Games Played (gp)</li>
  <li>Points (pts)</li>
  <li>Rebounds (reb)</li>
  <li>Assists (ast)</li>
  <li>Usage Percentage (usg_pct)</li>
  <li>Net Rating</li>
  <li>Country</li>
</ul>

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
<pre>
git clone https://github.com/your-username/nba-shiny-analysis.git
cd nba-shiny-analysis
</pre>

### 2️⃣ Install Dependencies
<pre>
pip install -r requirements.txt
</pre>

### 3️⃣ Run the Application
<pre>
shiny run app.py
</pre>

📍 The app will open automatically in your web browser.

---

## 🎨 UI Highlights

- 🌗 Dark mode toggle
- 🧩 Card-based layout
- 📑 Pill-style navigation tabs
- 🎯 Responsive and clean design
- ⚡ Fast interactive plots

---

## 🔮 Future Enhancements

- Advanced metrics (PER, TS%, BPM)
- Position-based filtering
- Team win/loss comparisons
- Export charts and data
- Player similarity analysis

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork the repository, submit pull requests, or open issues.

---

## 📜 License

This project is licensed under the <b>MIT License</b>.

---

<div align="center">

⭐ If you like this project, don’t forget to star the repository! ⭐

</div>
