# 📋 Project Explanation
<p align="justify">
A decision tree is built to predict diabetes for women in the PIMA Indians dataset based on predictor variables such as number of pregnancies, insulin, bmi, age, glucose, bp, and pedigree. A subset of the PIMA Indians data from the UCI Machine Learning Repository is a built-in dataset in the MASS library. The PIMA data in MASS contains 768 complete records from the original dataset. These 768 records have been broken down into two splits: Training data has 70% and Testing data has 30% of total data records. All records with zeros that don’t make sense have been cleaned out of these datasets.
</p>
<p align="justify">
A decision tree is a flowchart-like tree structure where an internal node represents feature (or attribute), the branch represents a decision rule, and each leaf node represents the outcome. The topmost node in a decision tree is known as the root node. It learns to partition on the basis of the attribute value. It partitions the tree in recursively manner call recursive partitioning. This flowchart-like structure helps in decision making. It’s visualization like a flowchart diagram which easily mimics the human level thinking. That is why decision trees are easy to understand and interpret.
</p>

# 📋 Steps performed in the Project


- Importing and Loading necessary libraries like Pandas, sklearn.
- Loading the PIMA Indian Diabetes Dataset using read_csv().
- Feature Selection-The columns are divided into two types of variables: dependent and independent variable. The target variable in the data set is Outcome and other variables are independent variables. The target variable is dropped from the data set so as to train the model without any biasing.
- Data Split- To understand model performance, dividing the dataset into a training set and a test set is a good strategy. In this project, the data is split into 70% training and 30% testing data.
- Building Model- Decision Tree Model is built on the training data.
- Evaluating Model- The model is evaluated by using the evaluation metric like accuracy. It is identified by comparing the actual test values and predicted values. The model obtained 77.05% using metrics.accuracy_score() of sklearn package.


# 📋 Downloading the Project and using it
<p align="justify">
Before downloading the Project, ensure that the Anaconda Navigator is installed on the machine. The steps to download and installation can be obtained from the official site: https://www.anaconda.com/products/individual. Download the decisiontreeclass.ipynb and execute each block of code in the Jupyter Notebook environment.
</p>

# 📋 Documentation

#### Pregnant Woman Diabetic Prediction Model using DecisionTree Classifier
<p align="justify"><b>Aim</b> : To predict whether a woman is suffering from Diabetes or not.  </p>
<p align="justify"><b>Description of the Project</b>:</p>
<p align="justify">
  
 
- Problem Statement: The number of people with diabetes rose from 108 million in 1980 to 422 million in 2014. It has been just increasing since then. Having such an increase is really alarming and therefore there’s a need to predict whether a person is suffering from it or not, so as to start providing medical assistance a bit early and try to cure it off in the initial stage itself. Having said that, this project targets a specific set of people i.e., the pregnant women. This project mainly aims to develop a model of higher accuracy that is capable of predicting diabetes effectively.
- Ways of solving it: The model is going to use a dataset which consists of several medical predictors (independent) variables and the target (dependent) variable. The dataset is going to be split into testing data and training data. Initially, the model is going to be trained on the training data. Then the model is run on testing data to verify the accuracy and efficiency metrics. 
- Algorithm used: DecisionTree Classifier
- Technologies Used: Jupyter Notebook (Required Python Packages Pre-Installed)
  
  
  </p>
<p align="justify">
<b>Expected Results</b>: A high accuracy model capable of predicting whether a pregnant woman is suffering from diabetes or not. 

