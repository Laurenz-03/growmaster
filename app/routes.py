from flask import render_template, url_for, flash, redirect, request
from app import app

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
    
@app.route('/gruppen')
def gruppen():
    return render_template('pages/gruppen.html', heading="GRUPPEN", title="Gruppen")
    
@app.route('/affiliate-link')
def aff_link():
    return render_template('pages/aff-link.html', heading="Affiliate-Link", title="Affiliate-Link", show_top_section=False, sidebar=False)
