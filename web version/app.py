import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI rendering

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, send_from_directory
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer  # Import SimpleImputer for missing values

app = Flask(__name__)

# Folder to save the images
IMAGE_FOLDER = 'static/images'
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

# Load and process the data
data_file_path = 'data/naivebayespolution.csv'
data = pd.read_csv(data_file_path)
data['date'] = pd.to_datetime(data['date'], format='%m/%d/%y')
data['month'] = data['date'].dt.strftime('%Y-%m')
data['year'] = data['date'].dt.strftime('%Y')

# Handle missing values by imputing with the mean
imputer = SimpleImputer(strategy='mean')
data['pm 2.5'] = imputer.fit_transform(data[['pm 2.5']])

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

    # Generate and save monthly plots
    for station in monthly_avg_pm25['stasiun'].unique():
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

    # Group by station and year to get the average PM2.5 for each station in each year
    yearly_avg_pm25 = data.groupby(['stasiun', 'year'])['pm 2.5'].mean().reset_index()

    # Generate and save yearly plots (bar plots and trend lines)
    for station in yearly_avg_pm25['stasiun'].unique():
        station_data = yearly_avg_pm25[yearly_avg_pm25['stasiun'] == station]

        # Bar plot
        plt.figure(figsize=(10, 6))
        sns.barplot(x='year', y='pm 2.5', data=station_data, palette='Blues')

        plt.title(f'Average PM2.5 per Year for {station}')
        plt.xlabel('Year')
        plt.ylabel('Average PM2.5')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plot_filename = f'{station}_yearly_avg_pm25.png'
        plt.savefig(os.path.join(IMAGE_FOLDER, plot_filename))
        plt.close()

        # Trend line plot
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='year', y='pm 2.5', data=station_data, marker='o', color='blue')

        plt.title(f'PM2.5 Trend per Year for {station}')
        plt.xlabel('Year')
        plt.ylabel('PM2.5')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plot_filename = f'{station}_yearly_trend_pm25.png'
        plt.savefig(os.path.join(IMAGE_FOLDER, plot_filename))
        plt.close()

    # Generate a comparison line plot across all stations
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=yearly_avg_pm25, x='year', y='pm 2.5', hue='stasiun', marker='o')

    plt.title('PM2.5 Comparison Across Stations')
    plt.xlabel('Year')
    plt.ylabel('PM2.5')
    plt.xticks(rotation=45)
    plt.legend(title='Station')
    plt.tight_layout()
    comparison_plot_filename = 'pm25_comparison_across_stations.png'
    plt.savefig(os.path.join(IMAGE_FOLDER, comparison_plot_filename))
    plt.close()

    # Pass the list of generated images to the template
    monthly_images = [f'{station}_monthly_avg_pm25.png' for station in monthly_avg_pm25['stasiun'].unique()]
    yearly_images = [f'{station}_yearly_avg_pm25.png' for station in yearly_avg_pm25['stasiun'].unique()]
    yearly_trend_images = [f'{station}_yearly_trend_pm25.png' for station in yearly_avg_pm25['stasiun'].unique()]
    return render_template('index.html', monthly_images=monthly_images, yearly_images=yearly_images, yearly_trend_images=yearly_trend_images, comparison_image=comparison_plot_filename, accuracy=accuracy, classification_report=classification_report_text)

@app.route('/station/<station>/<period>')
def station_detail(station, period):
    # Filter the data for the specific station and period
    if period == 'monthly':
        station_data = data[data['stasiun'] == station].groupby('month')['pm 2.5'].mean().reset_index()
        image_filename = f'{station}_monthly_avg_pm25.png'
    elif period == 'yearly':
        station_data = data[data['stasiun'] == station].groupby('year')['pm 2.5'].mean().reset_index()
        image_filename = f'{station}_yearly_avg_pm25.png'
    else:
        station_data = data[data['stasiun'] == station].groupby('year')['pm 2.5'].mean().reset_index()
        image_filename = f'{station}_yearly_trend_pm25.png'

    # Prepare the data for the table
    data_for_table = [{'period': row[0], 'pm25': row['pm 2.5']} for _, row in station_data.iterrows()]

    return render_template('station_detail.html', station_name=station, period=period, image=image_filename, data=data_for_table)

@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)