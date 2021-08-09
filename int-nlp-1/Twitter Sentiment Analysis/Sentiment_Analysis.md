# Twitter-Sentiment-Analysis
It is a Natural Language Processing Problem where Sentiment Analysis is done by Classifying the Positive tweets from negative tweets by machine learning models for classification,  text mining, text analysis, data analysis and data visualization

# Introduction

Natural Language Processing (NLP) is a hotbed of research in data science these days and one of the most common applications of NLP is sentiment analysis. From opinion polls to creating entire marketing strategies, this domain has completely reshaped the way businesses work, which is why this is an area every data scientist must be familiar with.

Thousands of text documents can be processed for sentiment (and other features including named entities, topics, themes, etc.) in seconds, compared to the hours it would take a team of people to manually complete the same task. 

We will do so by following a sequence of steps needed to solve a general sentiment analysis problem. We will start with preprocessing and cleaning of the raw text of the tweets. Then we will explore the cleaned text and try to get some intuition about the context of the tweets. After that, we will extract numerical features from the data and finally use these feature sets to train models and identify the sentiments of the tweets.

This is one of the most interesting challenges in NLP so I’m very excited to take this journey with you!

# Understand the Problem Statement

Let’s go through the problem statement once as it is very crucial to understand the objective before working on the dataset. The problem statement is as follows:

The objective of this task is to detect hate speech in tweets. For the sake of simplicity, we say a tweet contains hate speech if it has a racist or sexist sentiment associated with it. So, the task is to classify racist or sexist tweets from other tweets.

Formally, given a training sample of tweets and labels, where label ‘1’ denotes the tweet is racist/sexist and label ‘0’ denotes the tweet is not racist/sexist, your objective is to predict the labels on the given test dataset.

Note: The evaluation metric from this practice problem is F1-Score.

Take a look at the pictures below depicting two scenarios of an office space – one is untidy and the other is clean and organized. 

# Tweets Preprocessing and Cleaning

You are searching for a document in this office space. In which scenario are you more likely to find the document easily? Of course, in the less cluttered one because each item is kept in its proper place. The data cleaning exercise is quite similar. If the data is arranged in a structured format then it becomes easier to find the right information.

The preprocessing of the text data is an essential step as it makes the raw text ready for mining, i.e., it becomes easier to extract information from the text and apply machine learning algorithms to it. If we skip this step then there is a higher chance that you are working with noisy and inconsistent data. The objective of this step is to clean noise those are less relevant to find the sentiment of tweets such as punctuation, special characters, numbers, and terms which don’t carry much weightage in context to the text.

In one of the later stages, we will be extracting numeric features from our Twitter text data. This feature space is created using all the unique words present in the entire data. So, if we preprocess our data well, then we would be able to get a better quality feature space.

Let’s first read our data and load the necessary libraries.

# Generation and Visualization from Tweets

In this section, we will explore the cleaned tweets text. Exploring and visualizing data, no matter whether its text or any other data, is an essential step in gaining insights. Do not limit yourself to only these methods told in this tutorial, feel free to explore the data as much as possible.

Before we begin exploration, we must think and ask questions related to the data in hand. A few probable questions are as follows:

What are the most common words in the entire dataset?
What are the most common words in the dataset for negative and positive tweets, respectively?
How many hashtags are there in a tweet?
Which trends are associated with my dataset?
Which trends are associated with either of the sentiments? Are they compatible with the sentiments?

# Design FLow
![Screenshot (38)](https://user-images.githubusercontent.com/84801896/128295800-c52771a2-3d52-411b-b80f-0289694107d3.png)

# Code Flow

![Screenshot (39)](https://user-images.githubusercontent.com/84801896/128297053-6bd856db-2051-482a-bec3-8e1c2768d7a7.png)

![Screenshot (40)](https://user-images.githubusercontent.com/84801896/128297068-ed67c412-a8c0-4dba-904f-23d63bfd8c41.png)

![Screenshot (41)](https://user-images.githubusercontent.com/84801896/128297086-80ca6393-a5c8-44b4-80fd-a4a535bde352.png)

![Screenshot (42)](https://user-images.githubusercontent.com/84801896/128297109-427139f1-b5f6-4d00-8bc0-2c31e8523ef6.png)

![Screenshot (43)](https://user-images.githubusercontent.com/84801896/128297129-6b42650a-848c-45e1-8de9-e9d140f16f6e.png)

![Screenshot (44)](https://user-images.githubusercontent.com/84801896/128297148-177b8af1-0abb-4d44-8277-198aa24d4d6b.png)

![Screenshot (45)](https://user-images.githubusercontent.com/84801896/128297160-a87c9376-8e49-41e2-b034-c447f29509c4.png)

![Screenshot (46)](https://user-images.githubusercontent.com/84801896/128297183-ea8e8aff-ef84-4031-9ab7-a6fd442533f2.png)

![Screenshot (47)](https://user-images.githubusercontent.com/84801896/128297206-c40ca5ac-e6cd-49ae-a74e-4e77fb378b63.png)

![Screenshot (48)](https://user-images.githubusercontent.com/84801896/128297225-9ca205d5-7754-49d9-8135-e4edf39788a1.png)

![Screenshot (49)](https://user-images.githubusercontent.com/84801896/128297245-05a9dddc-3a72-4018-a429-8dc2c1f088e3.png)

![Screenshot (50)](https://user-images.githubusercontent.com/84801896/128297262-58ce08c7-685e-4d0e-8329-2aa97557c084.png)

![Screenshot (51)](https://user-images.githubusercontent.com/84801896/128297278-099d5b41-12bf-41e8-a0d9-e43a7f0804fd.png)

![Screenshot (52)](https://user-images.githubusercontent.com/84801896/128297298-443913c0-7dff-4bf4-bc9e-92dfc8ceb5bc.png)






# Summarize 

we learned how to approach a sentiment analysis problem. We started with preprocessing and exploration of data. Then we extracted features from the cleaned text using Bag-of-Words and TF-IDF. Finally, we were able to build a couple of models using both the feature sets to classify the tweets.

# Future Work or Study 
* We have covered most of the features in our classification. Bit, we didn’t include
effect of following features on classification accuracy.
– Taking care of emotions conveyed by abbreviations
– Analysing if subsequent sentences in a tweet are more important. (For eg.
giving greater weight to a 2
nd line in a tweet of 2 lines.)
* Although it was clear from work done by others on the same problem that SVM
tends to perform better than other classifers, it would be interesting to see how
hybrid of other classifiers (like naive bayes classifier) with SVM would perform. (In
our work we tried hybrid of bag of words with SVM which improved the accuracy)





