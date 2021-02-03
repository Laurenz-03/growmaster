from flask import render_template, url_for, flash, redirect, request
from app import app

growmaster_kapitel = [
    {"index": 1,
    "title": "Einleitung",
    "duration": "12min",
    "progress": 100},
    {"index": 2,
    "title": "Basics",
    "duration": "1h21",
    "progress": 80},
    {"index": 3,
    "title": "Algorithmus",
    "duration": "2h08min",
    "progress": 50},
    {"index": 4,
    "title": "Design",
    "duration": "1hm29in",
    "progress": 12},
    {"index": 5,
    "title": "Account-Wachstum",
    "duration": "3h55min",
    "progress": 4},
    {"index": 6,
    "title": "Branding",
    "duration": "58min",
    "progress": 0},
    {"index": 7,
    "title": "Verkaufen",
    "duration": "3h14min",
    "progress": 0},
]

# Startseite (Landing Page)
@app.route('/')
def home():
    return render_template('pages/home.html', title="Startseite", heading="GROWMASTER")

@app.route('/login')
def login():
    return render_template('pages/login.html', title="Login", heading="GROWMASTER", show_top_section=False, sidebar=False)
    
@app.route('/app-download')
def app_download():
    return render_template('pages/app-download.html', heading="App-Downloads", title="Die GrowMaster App")
    
@app.route('/coachings')
def coachings():
    return render_template('pages/coachings.html', heading="COACHINGS", title="Coachings")
    
@app.route('/kurs')
def kurs_uebersicht():
    return render_template('pages/kurs.html', heading="GROWMASTER", title="GrowMaster", growmaster_kapitel=growmaster_kapitel)

@app.route('/kurs/<kapitel>')
def gm_kapitel(kapitel):
    return render_template(f'pages/gm-kapitel/{kapitel}.html', heading="Kapitel", title=kapitel.capitalize(), show_top_section=False)
    
@app.route('/gruppen')
def gruppen():
    return render_template('pages/gruppen.html', heading="GRUPPEN", title="Gruppen")
    
@app.route('/affiliate-link')
def aff_link():
    return render_template('pages/aff-link.html', heading="Affiliate-Link", title="Affiliate-Link", show_top_section=False, sidebar=False)

@app.route('/growking')
def growking():
    return render_template('pages/growking.html', heading="GrowKing", title="GrowKing", growkinglogo=True)

@app.route('/bücher')
def buecher():
    return render_template('pages/bücher.html', heading="BÜCHER", title="Bücher")


#Impressum, AGBs, Datenschutz
@app.route('/impressum')
def impressum():
    return render_template('pages/impressum.html', heading="Impresssum", title="Impresssum", show_top_section=False, sidebar=False)

@app.route('/agb')
def agb():
    return render_template('pages/agb.html', heading="AGBs", title="AGBs", show_top_section=False, sidebar=False)

@app.route('/datenschutz')
def datenschutz():
    return render_template('pages/datenschutz.html', heading="Datenschutz", title="Datenschutz", show_top_section=False, sidebar=False)
