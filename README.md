# Powerball Article Generator API

This API generates a news article about the Powerball lottery, including information about the most recent drawing and the next drawing.

## Installation and Usage

To use this API, you will need to have Python 3 installed on your local machine.

1. Clone the GitHub repository:
   ```
   git clone https://github.com/[USERNAME]/powerball-article-generator.git
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   export FLASK_APP=app.py
   flask run
   ```

4. Access the API endpoint by navigating to `http://127.0.0.1:5000/powerball-article/` in your web browser or by sending an HTTP GET request to that URL.

## API Endpoint

### `GET /powerball-article/`

This endpoint generates a news article about the Powerball lottery. The response will be in JSON format.

#### Response Body

A successful response will have a JSON object with the following properties:

- `data`: an object with two properties:
  - `headline`: a plain-text string indicating if there was a Powerball winner at the last drawing.
  - `body`: an HTML string of the article body, including information about the most recent drawing and the next drawing.

#### Example Request

```
GET /powerball-article/
```

#### Example Response

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "data": {
    "headline": "No Powerball winner at the last drawing",
    "body": "<p>The Powerball lottery held its most recent drawing on Saturday, April 17th. Unfortunately, there was no winner of the jackpot prize. The winning numbers were 22, 36, 48, 55, 57, and the Powerball number was 24. Despite there being no jackpot winner, there were several winners of smaller prizes.</p><p>The next drawing will be held on Wednesday, April 21st. The jackpot prize for that drawing is estimated to be $90 million.</p>"
  }
}
```

## Key Decisions

- Flask was chosen as the web framework for this API due to its simplicity and ease of use.
- The `requests` library was used to make HTTP requests to the Powerball website to retrieve the most recent drawing information.
- The `beautifulsoup4` library was used to parse the HTML response from the Powerball website and extract the necessary information.
- The article body is generated dynamically based on the most recent drawing information and the date of the next drawing.