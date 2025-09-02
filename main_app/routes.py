from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/peer_reviewed')
def peer_reviewed():
    return render_template('peer_reviewed.html')


@app.route('/ugc_care')
def ugc_care():
    return render_template('ugc_care.html')


@app.route('/DOI_Allocation')
def DOI_Allocation():
    return render_template('DOI_Allocation.html')


@app.route('/Payment')
def Payment():
    return render_template('Payment.html')

@app.route('/ai_anemia')
def ai_anemia():
    return render_template('ai_anemia.html')


@app.route('/current_issue')
def current_issue():
    return render_template('Current_issue.html')


@app.route('/data_science_emerging_field')
def data_science_emerging_field():
    return render_template('data_science_emerging_field.html')


@app.route('/machine_learning_study')
def machine_learning_study():
    return render_template('machine_learning_study.html')


@app.route('/internet_of_things')
def internet_of_things():
    return render_template('internet_of_things.html')


@app.route('/big_data_challenges')
def big_data_challenges():
    return render_template('big_data_challenges.html')

@app.route('/group')
def group():
    return render_template('group.html')
