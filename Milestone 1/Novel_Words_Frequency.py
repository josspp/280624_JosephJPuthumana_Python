import pandas as pd
from collections import Counter
import re

# Step 1: Read the CSV file (assuming it has a column 'text' containing the novel's content)
file_path = "D:\Training\280624_JosephJPuthumana_Python\Milestone\Novel_Text.csv"  # Change this to your file path
df = pd.read_csv(file_path)

# Step 2: Extract the text column (assuming the text is in a column named 'text')
text = " ".join(df['text'].dropna().astype(str))  # Combine all rows in 'text' column into a single string

# Step 3: Preprocess the text
# Convert the text to lowercase, remove punctuation, and split into words
text_cleaned = re.sub(r'[^\w\s]', '', text.lower())  # Remove punctuation and convert to lowercase
words = text_cleaned.split()  # Split the text into words

# Step 4: Count word frequencies using Counter
word_counts = Counter(words)

# Step 5: Create a DataFrame from the word counts
word_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])

# Step 6: Sort the DataFrame by frequency (optional)
word_df = word_df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)

# Step 7: Display the DataFrame
print(word_df)