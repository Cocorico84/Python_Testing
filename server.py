import json
from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
current_competitions = [c['name'] for c in competitions if datetime.strptime(
    c['date'], '%Y-%m-%d %H:%M:%S') > datetime.now()]


@app.route('/')
def index():
    return render_template('index.html', clubs=clubs)


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email']
                == request.form['email']][0]
    except IndexError:
        flash("Your club is not registered!")
        return redirect(url_for('index'))
    return render_template('welcome.html', club=club, competitions=competitions, current_competitions=current_competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition and datetime.strptime(
            c['date'], '%Y-%m-%d %H:%M:%S') > datetime.now()][0]
        if foundClub and foundCompetition:
            return render_template('booking.html', club=foundClub, competition=foundCompetition)
    except IndexError:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions, current_competitions=current_competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name']
                   == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if int(competition['numberOfPlaces']) - placesRequired < 0:
        flash('You cannot buy more than your available places')
    elif placesRequired > 12:
        flash('You cannot buy more than 12 places!')
    elif int(club['points']) - placesRequired < 0:
        flash('Not enough points to buy places!')
    else:
        club['points'] = int(club['points']) - placesRequired
        competition['numberOfPlaces'] = int(
            competition['numberOfPlaces']) - placesRequired
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions, current_competitions=current_competitions)
    return render_template('booking.html', club=club, competition=competition)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
