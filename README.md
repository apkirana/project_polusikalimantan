# Project Polusi Kalimantan

## Overview
This project is focused on analyzing air quality in Kalimantan, Indonesia, particularly by examining PM2.5 pollution levels across various stations. The analysis is performed on both monthly and yearly bases, with visualizations to help understand the pollution trends in different regions.

## Repository Structure

- **data/**: This folder contains the raw and processed data files used in the analysis.
- **notebooks/**: Jupyter notebooks used for data cleaning, processing, and analysis.
- **scripts/**: Python scripts used for generating visualizations and performing analysis.
- **output/**: Generated output files, including visualizations and processed data.
- **README.md**: This file, which explains the project and how to use the repository.

## Data Sources
The data for this project includes PM2.5 measurements from various air quality monitoring stations in Kalimantan. The data is aggregated by month and year to provide insights into pollution levels over time.

## Bayes Theorem

The foundation of Naive Bayes is Bayes’ Theorem, which describes the probability of a hypothesis  H  given data  D :


P(H | D) = \frac{P(D | H) \cdot P(H)}{P(D)}


Where:

	•	 P(H | D)  is the posterior probability: the probability of hypothesis  H  given the data  D .
	•	 P(D | H)  is the likelihood: the probability of data  D  given that the hypothesis  H  is true.
	•	 P(H)  is the prior probability: the initial probability of the hypothesis  H  before seeing the data.
	•	 P(D)  is the marginal likelihood: the total probability of the data under all possible hypotheses.

#### Naive Bayes Assumption

The “naive” assumption in Naive Bayes is that the features \( X_1, X_2, \dots, X_n \) are conditionally independent given the class  C . This simplifies the computation of the likelihood:

\[
P(X_1, X_2, \dots, X_n | C) = P(X_1 | C) \cdot P(X_2 | C) \cdot \dots \cdot P(X_n | C)
\]

#### Classification Rule

To classify a new instance, we compute the posterior probability for each class  C  and choose the class with the highest posterior probability:

\[
C_{\text{MAP}} = \arg\max_{C} \ P(C | X_1, X_2, \dots, X_n)
\]

Using Bayes’ Theorem and the independence assumption, this becomes:


C_{\text{MAP}} = \arg\max_{C} \ P(C) \prod_{i=1}^{n} P(X_i | C)


#### Types of Naive Bayes Classifiers

	1.	Gaussian Naive Bayes: Assumes that the continuous features follow a Gaussian (normal) distribution.
	•	The likelihood for a feature  X_i  given class  C  is:

P(X_i | C) = \frac{1}{\sqrt{2\pi\sigma_C^2}} \exp\left(-\frac{(X_i - \mu_C)^2}{2\sigma_C^2}\right)

where  \mu_C  and  \sigma_C^2  are the mean and variance of the feature for class  C .
	2.	Multinomial Naive Bayes: Often used for text classification where features represent word counts or frequencies.
	•	The likelihood is modeled as:

P(X_i | C) = \frac{(N_{C_i} + 1)}{(N_C + n)}

where  N_{C_i}  is the number of times word  i  appears in class  C ,  N_C  is the total number of words in class  C , and  n  is the total number of unique words.
	3.	Bernoulli Naive Bayes: Used for binary/boolean features.
	•	The likelihood is:

P(X_i | C) = P(X_i = 1 | C)^{X_i} \cdot P(X_i = 0 | C)^{(1-X_i)}


For this problem, assuming the station name is categorical and pollution levels are continuous, we would typically use a Gaussian Naive Bayes classifier if you want to classify based on numerical features (like pm 2.5). The station name would need to be encoded as a feature or used as the class itself.

## Analysis and Visualizations
The analysis involves generating bar graphs that illustrate the average PM2.5 values across different stations:
- **Monthly Analysis**: Shows the average PM2.5 values per station for each month.
- **Yearly Analysis**: Displays the average PM2.5 values per station for each year, with separate graphs for 2023 and 2024.

### Monthly Analysis
The monthly analysis provides insights into how PM2.5 levels change on a month-to-month basis at each station. The graphs highlight the trends and help identify any seasonal patterns or anomalies in air quality.

### Yearly Analysis
The yearly analysis aggregates the data to provide an overview of air quality trends over longer periods. This helps in understanding the broader impact of environmental factors on air pollution in the region.

## How to Run the Analysis
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/apkirana/project_polusikalimantan.git```
2. **Run the Scripts**:
To generate the monthly and yearly graphs, run the appropriate scripts from the scripts/ folder. For example:
  ```bash
python scripts/generate_monthly_graphs.py
python scripts/generate_yearly_graphs.py```


