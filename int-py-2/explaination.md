# 📋 Project Explaination
<p align="justify">
A decision tree is built to predict diabetes for women in the PIMA Indians dataset based on predictor variables such as number of pregnancies, insulin, bmi, age, glucose, bp, and pedigree. A subset of the PIMA Indians data from the UCI Machine Learning Repository is a built-in dataset in the MASS library. The PIMA data in MASS contains 768 complete records from the original dataset. These 768 records have been broken down into two splits: Training data has 70% and Testing data has 30% of total data records. All records with zeros that don’t make sense have been cleaned out of these datasets.
</p>
<p align="justify">
A decision tree is a flowchart-like tree structure where an internal node represents feature (or attribute), the branch represents a decision rule, and each leaf node represents the outcome. The topmost node in a decision tree is known as the root node. It learns to partition on the basis of the attribute value. It partitions the tree in recursively manner call recursive partitioning. This flowchart-like structure helps in decision making. It’s visualization like a flowchart diagram which easily mimics the human level thinking. That is why decision trees are easy to understand and interpret.
</p>
# 📋 Steps performed in the Project


- Importing and Loading necessary libraries like Pandas, sklearn, 
- Loading the PIMA Indian Diabetes Dataset using read_csv()
- Feature Selection-The columns are divided into two types of variables: dependent and independent variable. The target variable in the data set is Outcome and other variables are independent variables. The target variable is dropped from the data set so as to train the model without any biasing.
- Data Split- To understand model performance, dividing the dataset into a training set and a test set is a good strategy. In this project, the data is split into 70% training and 30% testing data.
- Building Model- Decision Tree Model is built on the training data.
- Evaluating Model- The model is evaluated by using the evaluation metric like accuracy. It is identified by comparing the actual test values and predicted values. The model obtained 77.05% using metrics.accuracy_score() of sklearn package.

