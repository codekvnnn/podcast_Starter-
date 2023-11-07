# app.py

from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Example podcast data
podcasts = [
    {
        'id': 1,
        'title': 'The Daily',
        'host': 'Michael Barbaro',
        'description': 'This is what the news should sound like. The biggest stories of our time, told by the best journalists in the world.'
    },
    {
        'id': 2,
        'title': 'Radiolab',
        'host': 'Jad Abumrad & Robert Krulwich',
        'description': 'Investigating a strange world.'
    }
    # Add as many podcasts as you like
]

@app.route('/')
def index():
    return render_template('index.html', podcasts=podcasts)

@app.route('/api/podcasts')
def api_podcasts():
    return jsonify(podcasts)

if __name__ == '__main__':
    app.run(debug=True)
