import pandas as pd
from collections import Counter
import re

#Read the CSV file assuming it has a column 'text' containing the novel's content
file_path = r"D:\Training\280624_JosephJPuthumana_Python\Milestone 1\Novel_Text.csv"  # Change this to your file path
df = pd.read_csv(file_path)

#Extract the text column assuming the text is in a column named 'text'
text = " ".join(df['text'].dropna().astype(str))  # Combine all rows in 'text' column into a single string

#Convert the text to lowercase, remove punctuation, and split into words
text_cleaned = re.sub(r'[^\w\s]', '', text.lower())  # Remove punctuation and convert to lowercase
words = text_cleaned.split()  # Split the text into words

#Count word frequencies using Counter
word_counts = Counter(words)

#Create a DataFrame from the word counts
word_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])

#Sort the DataFrame by frequency (optional)
word_df = word_df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)

print(word_df)