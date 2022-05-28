import matplotlib.pyplot as plt
import re
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import word_tokenize, sent_tokenize
from nlp_utils import get_sample_Santo_Graal

# Split the script into lines: lines
holy_grail = get_sample_Santo_Graal()
lines = sent_tokenize(holy_grail)

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, " ", l) for l in lines]
lines = holy_grail.split("\n")
#print(lines)

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s, pattern=r"\w+") for s in lines]
print(tokenized_lines[0])

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]
print(line_num_words)
# Plot a histogram of the line lengths
plt.hist(line_num_words)

# Show the plot
plt.show()