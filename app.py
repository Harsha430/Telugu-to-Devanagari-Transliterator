from flask import Flask, request, jsonify, render_template
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

app = Flask(__name__)

# Function to transliterate Telugu script to Devanagari script (Sanskrit)
def transliterate_telugu_to_sanskrit(telugu_text):
    sanskrit_text = transliterate(telugu_text, sanscript.TELUGU, sanscript.DEVANAGARI)
    return sanskrit_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transliterate', methods=['POST'])
def transliterate_text():
    data = request.get_json()
    telugu_para = data.get('text', '')
    sanskrit_script = transliterate_telugu_to_sanskrit(telugu_para)
    return jsonify({'transliterated_text': sanskrit_script})

if __name__ == '__main__':
    app.run(debug=True)
