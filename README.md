# Udacity Data Science Capstone

This is my repository for the Udacity Data Science Capstone. I decided to work on the [Greate Energy Prediction]https://www.kaggle.com/c/ashrae-energy-prediction/overview() competition on Kaggle.
You can read my blogpost about the solution here.

### Introduction

In Greate Energy Prediction, the goal is to develop models that can predict the future energy consumption of buildings. The purpose is that better models allows property managers to compare energy consumptions after they've made changes to a probable comsumption without the changes based on historical data. Without those kinds of models in place, it's hard to know if the changes actually acomplished something.

### Libraries

The libraries needed to run the code are:
- [Pandas](https://pandas.pydata.org/) & [Numpy](https://numpy.org/) for managing and working with data
- [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/) for visualizing data
- [LightGBM](https://lightgbm.readthedocs.io/en/latest/) for training Gradient Boosted Decision Trees
- [Tqdm](https://github.com/tqdm/tqdm) for logging during training

### Code structure

* GreatEnergyPrediction.ipnb - This is where I train the models
* Preprocessing.ipnb - Going through details and ideas behind preprocessing
* utils/load_data.py - Helper functions for loading data 
* utils/preprocessing.py - Helper functions for preprocessing data
* utils/plotting.py - Helper functions for plotting data

## Conclusions

It was a very challenging task because of data preprocessing. There are amny types of anomalies in the data and it's hard to know which ones you can remove. Some anomalies are most likely just as common in the test data as in the training data because it comes from the same source.

Apart from that, I'm happy with my solution where I decided to build many tiny models instead of a big one. It's might be more prone to overfitting, but I got a competitive result according to the best public solutions.

Unfortunately, I can't compare with the leaderboard because there was a big data leak in the competition where a large part of the test data became available. I decided to avoid the leaked data and as a consequence my score are way worse than the leaderboard.


