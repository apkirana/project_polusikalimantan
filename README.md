# project_polusikalimantan



Bayes’ Theorem

The foundation of Naive Bayes is Bayes’ Theorem, which describes the probability of a hypothesis  H  given data  D :


P(H | D) = \frac{P(D | H) \cdot P(H)}{P(D)}


Where:

	•	 P(H | D)  is the posterior probability: the probability of hypothesis  H  given the data  D .
	•	 P(D | H)  is the likelihood: the probability of data  D  given that the hypothesis  H  is true.
	•	 P(H)  is the prior probability: the initial probability of the hypothesis  H  before seeing the data.
	•	 P(D)  is the marginal likelihood: the total probability of the data under all possible hypotheses.

Naive Bayes Assumption

The “naive” assumption in Naive Bayes is that the features \( X_1, X_2, \dots, X_n \) are conditionally independent given the class  C . This simplifies the computation of the likelihood:

\[
P(X_1, X_2, \dots, X_n | C) = P(X_1 | C) \cdot P(X_2 | C) \cdot \dots \cdot P(X_n | C)
\]

Classification Rule

To classify a new instance, we compute the posterior probability for each class  C  and choose the class with the highest posterior probability:

\[
C_{\text{MAP}} = \arg\max_{C} \ P(C | X_1, X_2, \dots, X_n)
\]

Using Bayes’ Theorem and the independence assumption, this becomes:


C_{\text{MAP}} = \arg\max_{C} \ P(C) \prod_{i=1}^{n} P(X_i | C)


Types of Naive Bayes Classifiers

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


Applying Naive Bayes to Your Problem

For this problem, assuming the station name is categorical and pollution levels are continuous, we would typically use a Gaussian Naive Bayes classifier if you want to classify based on numerical features (like pm 2.5). The station name would need to be encoded as a feature or used as the class itself.