# phising_domain_detector

Project Description 📄

❄️ To predict whether the domains are real or malicious.

##### Deployed Website: (https://phishing-detector-rqld.onrender.com/)

##### Jupyter Notebook: (https://github.com/shiv0112/phishing_domain_detector/blob/main/research/model.ipynb)

## Data:

```
:Phishing Websites Dataset

https://data.mendeley.com/datasets/72ptz43s9v/1

These data consist of a collection of legitimate as well as phishing website instances. Each website is represented by the set of features which denote, whether website is legitimate or not. Data can serve as an input for machine learning process.

In this repository the two variants of the Phishing Dataset are presented.

Full variant - dataset_full.csv
Short description of the full variant dataset:
Total number of instances: 88,647
Number of legitimate website instances (labeled as 0): 58,000
Number of phishing website instances (labeled as 1): 30,647
Total number of features: 111

Small variant - dataset_small.csv
Short description of the small variant dataset:
Total number of instances: 58,645
Number of legitimate website instances (labeled as 0): 27,998
Number of phishing website instances (labeled as 1): 30,647
Total number of features: 111
```

I trained this model using Random Forest:

#### Selected features

![Alt text](https://github.com/shiv0112/phising_domain_detector/raw/main/screenshots/features.png)

#### Metrics of best model used:

![Alt text](https://github.com/shiv0112/phising_domain_detector/raw/main/screenshots/metrics.png)

#### Grid Search Cross-validation on Random Forest:

![Alt text](https://github.com/shiv0112/phising_domain_detector/raw/main/screenshots/gscv.png)

#### The ROC Curve for Random Forest:

![Alt text](https://github.com/shiv0112/phising_domain_detector/raw/main/screenshots/plot.png)

## Demo Video:

![Alt text](https://github.com/shiv0112/phising_domain_detector/raw/main/screenshots/demo.gif)

### Page of Website:

![Alt text](https://github.com/shiv0112/phising_domain_detector/raw/main/screenshots/1.png)
![Alt text](https://github.com/shiv0112/phising_domain_detector/raw/main/screenshots/why.png)
![Alt text](https://github.com/shiv0112/phising_domain_detector/raw/main/screenshots/datareport.png)
![Alt text](https://github.com/shiv0112/phising_domain_detector/raw/main/screenshots/about.png)

### Data Input from user:

![Alt text](https://github.com/shiv0112/phising_domain_detector/raw/main/screenshots/2.png)

```bash
Authors
```
```
Rishabh
```
```
Shivansh Srivastava
```
```
Ashish Diwakar
```

