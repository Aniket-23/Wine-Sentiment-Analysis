from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the Flask application
app = Flask(__name__)

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the sentiment analysis route
@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the review text from the form
    review = request.form['review']

    # Perform sentiment analysis on the review text
    sentiment_score = analyzer.polarity_scores(review)
    compound_score = sentiment_score['compound']
    sentiment_class = 'Positive' if compound_score >= 0 else 'Negative'

    # Render the result template with the sentiment analysis results
    return render_template('result.html', review=review, sentiment=sentiment_class)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

