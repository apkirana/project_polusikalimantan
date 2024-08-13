# Project Polusi Kalimantan

This repository contains the code and resources for analyzing and visualizing air pollution data in Kalimantan. The project includes monthly and yearly analysis of PM2.5 levels across various stations, as well as a web application that provides interactive visualizations and insights.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Web Application](#web-application)
- [Visualizations](#visualizations)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Air pollution is a significant issue in many parts of the world, including Kalimantan. This project aims to provide tools for analyzing air pollution data, focusing on PM2.5 levels. The project includes both data analysis scripts and a Flask-based web application for visualizing the results.

## Features
- **Monthly Analysis**: Visualizes average PM2.5 levels for each station on a monthly basis.
- **Yearly Analysis**: Provides yearly trends and comparisons across different stations.
- **Interactive Web Application**: A Flask-based app that allows users to explore the analysis and visualizations.
- **Naive Bayes Classification**: Uses a Naive Bayes model to classify pollution levels based on PM2.5 data.
- **Conditional Formatting**: Tables are color-coded to indicate air quality levels (Good, Moderate, Unhealthy, etc.).

## Installation
To get started with the project, clone the repository and install the required dependencies:

`bash
git clone https://github.com/apkirana/project_polusikalimantan.git
cd project_polusikalimantan
pip install -r requirements.txt`

## Usage

To run the analysis and start the web application:

1.	Run Data Analysis: Use the provided Jupyter notebooks to analyze the data (polusi_monthly_kalimantan.ipynb, polusi_yearly_kalimantan.ipynb, and visualisasi_tahunan_kalimantan.ipynb).
2.	Start the Web Application: Run the Flask app to view the visualizations in your browser.

`python app.py`

## Data

The data used in this project is derived from air quality monitoring stations in Kalimantan. The primary focus is on PM2.5 data, which is a key indicator of air quality.

	•	PM2.5: Particulate matter with a diameter of less than 2.5 micrometers.
	•	Stations: Multiple monitoring stations across Kalimantan are included in the analysis.

## Web Application

The Flask web application allows users to:

	•	View monthly and yearly PM2.5 analysis for each station.
	•	Explore trends and comparisons across different stations.
	•	Interact with tables that display air quality data with color-coded levels.

Visualizations

The project includes a variety of visualizations to help users understand air quality trends:

	•	Monthly Bar Charts: Show the average PM2.5 levels for each month.
	•	Yearly Bar Charts: Display yearly averages for each station.
	•	Trend Lines: Illustrate trends in PM2.5 levels over time.
	•	Comparisons: Compare air quality across multiple stations.

## Contributing

Contributions to this project are welcome. If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
- **LinkedIn:** [Annisa Puspa Kirana](https://id.linkedin.com/in/annisapuspakirana/en)
- **Social Links:** [linktr.ee/puspakirana](http://linktr.ee/puspakirana)
