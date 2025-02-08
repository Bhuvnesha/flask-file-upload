from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd

app = Flask(__name__)

# Configure the upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Path to the Excel file
EXCEL_FILE = 'file_details.xlsx'


# Route to display the upload form and uploaded images
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return redirect(request.url)

        if file:
            # Save the file to the upload folder
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Save file details to Excel
            save_file_details(file.filename, filepath)

            return redirect(url_for('index'))

    # Load file details from Excel
    file_details = load_file_details()

    return render_template('index.html', file_details=file_details)


def save_file_details(filename, filepath):
    # Create a DataFrame with the file details
    new_entry = pd.DataFrame({'Filename': [filename], 'Filepath': [filepath]})

    # Check if the Excel file already exists
    if os.path.exists(EXCEL_FILE):
        # Load the existing Excel file
        df = pd.read_excel(EXCEL_FILE)
        # Append the new entry
        df = pd.concat([df, new_entry], ignore_index=True)
    else:
        # Create a new DataFrame
        df = new_entry

    # Save the DataFrame to Excel
    df.to_excel(EXCEL_FILE, index=False)


def load_file_details():
    # Check if the Excel file exists
    if os.path.exists(EXCEL_FILE):
        # Load the Excel file
        df = pd.read_excel(EXCEL_FILE)
        return df.to_dict('records')
    else:
        return []


@app.route('/delete/<filename>', methods=['GET'])
def delete_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Check if the file exists
    if os.path.exists(filepath):
        # Delete the file
        os.remove(filepath)
        print(f"Deleted file: {filepath}")

        # Remove the file details from the Excel file
        if os.path.exists(EXCEL_FILE):
            df = pd.read_excel(EXCEL_FILE)
            df = df[df['Filename'] != filename]  # Filter out the deleted file
            df.to_excel(EXCEL_FILE, index=False)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)