import pandas as pd
from collections import Counter
import re

#CSV file assuming it has a column 'text' containing the novel content
file_path = r"D:\Training\280624_JosephJPuthumana_Python\Milestone 1\Novel_Text.csv"  # Change this to your file path
df = pd.read_csv(file_path)

#Extract the text column assuming the text is in a column named 'text'
text = " ".join(df['text'].dropna().astype(str))  # Combine all rows in 'text' column into a single string

text_cleaned = re.sub(r'[^\w\s]', '', text.lower())  # Remove punctuation and convert to lowercase
words = text_cleaned.split()  # Split the text into words

word_counts = Counter(words)

word_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])

word_df = word_df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)

print(word_df)