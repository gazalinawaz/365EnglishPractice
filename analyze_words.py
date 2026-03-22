import re

# Read the word list
with open('word_count_analysis.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Split by commas and whitespace
words = [w.strip().lower() for w in re.split(r'[,\s]+', text) if w.strip()]

# Get unique words
unique_words = set(words)

# Find duplicates
duplicates = {w: words.count(w) for w in unique_words if words.count(w) > 1}

# Print results
print(f'Total words (including duplicates): {len(words)}')
print(f'Unique words: {len(unique_words)}')
print(f'Number of duplicated words: {len(duplicates)}')
print(f'\nMost frequent duplicates:')

for w, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f'  "{w}": {count} times')

print(f'\n=== SUMMARY ===')
print(f'The list contains {len(unique_words)} unique words, NOT 5000.')
print(f'There are {len(duplicates)} words that appear multiple times.')
print(f'Total word count (with duplicates): {len(words)}')
