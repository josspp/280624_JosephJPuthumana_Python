import pandas as pd
import re

# Read the CSV file
file_path = r"D:\Training\280624_JosephJPuthumana_Python\Milestone 1\Novel_Text.csv"
df = pd.read_csv(file_path)

# Combine all rows in 'text' column into a single string, drop NaN, and convert to lowercase
text = " ".join(df['text'].dropna().astype(str)).lower()

# Remove punctuation using regular expressions
text_cleaned = re.sub(r'[^\w\s]', '', text)  # Remove punctuation

# Split the cleaned text into words
words = text_cleaned.split()

# Initialize an empty dictionary to store word counts
word_counts = {}

# Loop over the words and count frequencies
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Convert the dictionary to a DataFrame
word_df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Frequency'])

# Sort by frequency
word_df = word_df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)

# Display the result
print(word_df)