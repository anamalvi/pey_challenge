Follow the instructions below

* Fork the repository
* Unzip the census_data.tar.gz folder.
* Plot a histogram for the age column in csv_train.csv. Suggested python library is matplotlib.
* Drop the fnlwgt columns in both csv files, as well as the header row.
* Fit a [logistic regression](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) on the dataset. Suggested python library is scikit-learn. Use the fit function. Use default values for all parameters.
* Score census_test.csv using the model generated in the previous step. Use the score function. Report the accuracy.
* Include results for all tasks given, and all the code you wrote to get them. The submission should be zipped.