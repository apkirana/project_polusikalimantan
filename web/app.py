import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Folder to save the images
IMAGE_FOLDER = 'static/images'
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

# Load and process the data
data_file_path = 'naivebayespolution.csv'
data = pd.read_csv(data_file_path)
data['date'] = pd.to_datetime(data['date'], format='%m/%d/%y')
data['month'] = data['date'].dt.strftime('%Y-%m')

# Define a function to label pollution levels based on AQI
def label_aqi(pm25):
    if pm25 <= 50:
        return 0  # Good
    elif pm25 <= 100:
        return 1  # Moderate
    elif pm25 <= 150:
        return 2  # Unhealthy for Sensitive Groups
    elif pm25 <= 200:
        return 3  # Unhealthy
    elif pm25 <= 300:
        return 4  # Very Unhealthy
    else:
        return 5  # Hazardous

data['Pollution Level'] = data['pm 2.5'].apply(label_aqi)

# Encode the station names for Naive Bayes input
label_encoder = LabelEncoder()
data['stasiun_encoded'] = label_encoder.fit_transform(data['stasiun'])

# Prepare features and labels for the model
X = data[['stasiun_encoded', 'pm 2.5']]
y = data['Pollution Level']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Gaussian Naive Bayes classifier
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predict the pollution level for the test data
y_pred = classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_report_text = classification_report(y_test, y_pred, target_names=['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous'])

@app.route('/')
def index():
    # Group by station and month to get the average PM2.5 for each station in each month
    monthly_avg_pm25 = data.groupby(['stasiun', 'month'])['pm 2.5'].mean().reset_index()

    # Plotting the average PM2.5 for each station over time
    stations = monthly_avg_pm25['stasiun'].unique()

    # Generate and save plots
    for station in stations:
        station_data = monthly_avg_pm25[monthly_avg_pm25['stasiun'] == station]

        plt.figure(figsize=(10, 6))
        sns.barplot(x='month', y='pm 2.5', data=station_data, palette='viridis')

        plt.title(f'Average PM2.5 per Month for {station}')
        plt.xlabel('Month')
        plt.ylabel('Average PM2.5')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot
        plot_filename = f'{station}_monthly_avg_pm25.png'
        plt.savefig(os.path.join(IMAGE_FOLDER, plot_filename))
        plt.close()

    # Pass the list of generated images to the template
    images = [f'{station}_monthly_avg_pm25.png' for station in stations]
    return render_template('index.html', images=images, accuracy=accuracy, classification_report=classification_report_text)

@app.route('/station/<station>')
def station_detail(station):
    # Filter the data for the specific station
    station_data = data[data['stasiun'] == station]
    avg_pm25 = station_data.groupby('month')['pm 2.5'].mean().reset_index()

    # Prepare the data for the table
    data_for_table = [{'month': row['month'], 'pm25': row['pm 2.5']} for _, row in avg_pm25.iterrows()]

    # Image file for the station
    image_filename = f'{station}_monthly_avg_pm25.png'

    return render_template('station_detail.html', station_name=station, image=image_filename, data=data_for_table)

@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)