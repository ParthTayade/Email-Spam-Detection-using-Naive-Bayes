# Email-Spam-Detection-using-Naive-Bayes

### Project Overview
This project implements an email spam detection system using Naive Bayes algorithm. Text data is preprocessed and transformed using text vectorization techniques to convert emails into features. The trained model classifies emails as spam or ham based on learned patterns, demonstrating an efficient and probabilistic approach to text classification.

### Dataset Source : KAGGLE Spam Collection Dataset

This dataset contains a collection of email messages labeled as Spam or Ham (Not Spam). It is designed for email spam detection and text classification tasks. Each record includes the raw email text along with its corresponding label, making it suitable for preprocessing, feature extraction, and training machine learning or NLP models.

### Approach

#### 1.Data Loading & Cleaning

&#9679; Loaded the email spam dataset using Pandas.

&#9679; Removed unnecessary columns and handled missing values.

&#9679; Renamed columns for better readability (e.g., label, message).

#### 2.Label Encoding

&#9679; Converted categorical labels (spam, ham) into numerical form for model training.

#### 3.Text Preprocessing

&#9679; Converted text to lowercase.

&#9679; Removed special characters and unnecessary symbols.

&#9679; Transformed raw text into numerical features using CountVectorizer / TF-IDF.

#### 4.Train–Test Split

&#9679; Split the dataset into training and testing sets to evaluate model performance.

#### 5.Model Selection

&#9679; Trained multiple classifiers and compared their performance.

&#9679; Multinomial Naive Bayes was selected because it achieved the highest precision score of 1, making it ideal for spam classification where false positives must be minimized.

#### 6.Model Evaluation

&#9679; Evaluated the model using accuracy, precision, recall, and confusion matrix.

&#9679; Precision was given priority due to the nature of spam detection.

# Results

#### Multinomial Naive Bayes

&#9733; Accuracy : 97%                                                                                                                   
&#9733; Precision Score : 1.0

The Multinomial Naive Bayes model achieved a precision score of 1, meaning all emails predicted as spam were truly spam.
This makes the model highly reliable for real-world spam filtering systems.
