# Open the input text file
with open('input.txt', 'r') as file:
    text = file.read()

# Split the text into sentences
import re
sentences = re.split(r'(?<=[^.?!])\s+', text)

# Format the sentences
formatted_text = []
for sentence in sentences:
    if sentence.endswith('.'):
        formatted_text.append(sentence)
    else:
        if formatted_text and not formatted_text[-1].endswith('.'):
            formatted_text[-1] += ' ' + sentence
        else:
            formatted_text.append(sentence)

# Write the formatted text to a new file
with open('output.txt', 'w') as file:
    file.write('\n'.join(formatted_text))