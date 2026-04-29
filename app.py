from flask import Flask, render_template, request, redirect, url_for, abort
import os
from utils.predictor import predict_species
from utils.animal_data import get_animal_info, get_all_species, ANIMAL_DATA

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/audio_uploads"

# Store prediction history for dashboard (in-memory, resets on restart)
prediction_history = {}


@app.route('/')
def index():
    species = get_all_species()
    return render_template('index.html', species=species)


@app.route('/dashboard')
def dashboard():
    species = get_all_species()
    total = sum(prediction_history.values()) if prediction_history else 0
    max_count = max(prediction_history.values()) if prediction_history else 1
    return render_template(
        'dashboard.html',
        history=prediction_history,
        total_predictions=total,
        max_count=max_count,
        species=species
    )


@app.route('/about')
def about():
    species = get_all_species()
    return render_template('about.html', species=species)


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/animal-info/<species>')
def animal_info(species):
    info = get_animal_info(species)
    if info is None:
        abort(404)
    return render_template('animal_info.html', animal=info)


@app.route('/predict', methods=['POST'])
def predict():
    if 'audio_file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['audio_file']
    if file.filename == '':
        return redirect(url_for('index'))

    # Save uploaded audio
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(save_path)

    # Predict species
    species_name, confidence = predict_species(save_path)

    # Update prediction history
    prediction_history[species_name] = prediction_history.get(species_name, 0) + 1

    # Get emoji for the predicted species
    animal_info = get_animal_info(species_name)
    emoji = animal_info['emoji'] if animal_info else '🐾'

    # Get all species for the gallery
    all_species = get_all_species()

    return render_template(
        'index.html',
        prediction=species_name,
        prediction_key=species_name,
        confidence=confidence,
        filename=file.filename,
        emoji=emoji,
        species=all_species
    )


if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
