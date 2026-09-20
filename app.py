from flask import Flask, render_template, request, redirect, url_for, session
import json, os

app = Flask(__name__)
app.secret_key = 'lord-of-beans-v7'
LANGS = ['pt', 'en', 'es', 'de', 'fr', 'it']
DEFAULT = 'pt'

with open(os.path.join('translations', 'translations.json'), encoding='utf-8') as f:
    T = json.load(f)

@app.route('/')
def home():
    lang = session.get('lang', DEFAULT)
    return render_template('index.html', t=T[lang], lang=lang, langs=LANGS)

@app.route('/<lang>')
def localized(lang):
    if lang not in LANGS:
        return redirect(url_for('home'))
    session['lang'] = lang
    return render_template('index.html', t=T[lang], lang=lang, langs=LANGS)

@app.route('/set-language/<lang>')
def set_language(lang):
    if lang in LANGS:
        session['lang'] = lang
    return redirect(request.referrer or url_for('home'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
app.run(debug=False, host="0.0.0.0", port=port)
