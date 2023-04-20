import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/powerball-article/', methods=['GET'])
def powerball_article():
    # Scrape the Powerball website to get the latest winning number
    url = "https://www.powerball.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    winning_numbers = soup.select_one('div#numbers div.card-body div.row div.d-flex.col-auto.flex-nowrap.game-ball-group.mx-auto')

    
    # Get the winners data
    winners_header = soup.select_one('div#winner div.card-body div.row.winner-card:nth-of-type(1) h5.card-title')
    date = winners_header.text.strip()

    jackpot_winners = soup.select_one('div#winner div.card-body div.row.winners-group:nth-of-type(1) span.winner-location').text.strip()

    match_5_power_play_winners = soup.select_one('div#winner div.card-body div.row.winners-group:nth-of-type(2) span.winner-location').text.strip()

    match_5_winners = soup.select_one('div#winner div.card-body div.row.winners-group:nth-of-type(3) span.winner-location').text.strip()



    # Check if there was a Powerball winner
    if "None" in jackpot_winners:
        headline = "No Powerball Winner in the Last Drawing"
        body = f"<p>There was no Powerball winner in the last drawing, which took place on {date}.<p>"
    else:
        winner_state = jackpot_winners
        headline = f"There was a Powerball Winner from the state of {winner_state} in the Last Drawing"
        body = f"<p>The winning Powerball numbers for the last drawing, which took place on {date}, were {winning_numbers}. The winning ticket was sold in {winner_state}.<p>"

    # Get information about the next drawing
    next_drawing_date = soup.select_one("#next-drawing .title-date").text.strip()
    jackpot_amount = soup.select_one("#next-drawing .game-jackpot-number").text.strip()

    # Build the article body
    body += f"<p>The next Powerball drawing will take place on {next_drawing_date}, with a potential prize of {jackpot_amount}.<p>"

    # Build and return the response
    response_data = {"headline": headline, "body": body}
    return jsonify({"data": response_data})

@app.route('/powerball-article/', methods=['POST'])
def invalid_method():
    # Return an error message for invalid HTTP method
    return jsonify({
        'error': 'Invalid HTTP method used. Please use GET method.'
    }), 405

@app.route('/powerball-numbers/')
def powerball_numbers():
    # Scrape the latest Powerball drawing data from data.ny.gov
    url = 'https://data.ny.gov/resource/d6yy-54nr.json?$order=draw_date DESC&$limit=1'
    response = requests.get(url)
    data = response.json()[0]
    numbers = data['winning_numbers']
    powerball_number = data['powerball']

    date = datetime.datetime.strptime(data['draw_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%A, %B %d, %Y')

    # Return the latest drawing date and numbers as a JSON response
    response = jsonify({
        'data': {
            'date': date,
            'numbers': numbers,
            'powerball': powerball_number
        }
    })
    response.headers.add('Content-Type', 'application/json')
    return response

if __name__ == '__main__':
    app.run(debug=True)
