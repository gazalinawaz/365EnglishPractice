"""
Consolidate 3000-word vocabulary list into single file
and assess word quality (simple vs advanced)
"""

import re

# Simple/common words to flag (these should NOT be in an advanced list)
SIMPLE_WORDS = {
    'go', 'get', 'make', 'do', 'have', 'be', 'say', 'see', 'know', 'think',
    'take', 'come', 'want', 'use', 'find', 'give', 'tell', 'work', 'call', 'try',
    'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let', 'begin',
    'seem', 'help', 'talk', 'turn', 'start', 'show', 'hear', 'play', 'run', 'move',
    'like', 'live', 'believe', 'hold', 'bring', 'happen', 'write', 'provide', 'sit',
    'stand', 'lose', 'pay', 'meet', 'include', 'continue', 'set', 'learn', 'change',
    'lead', 'understand', 'watch', 'follow', 'stop', 'create', 'speak', 'read', 'allow',
    'add', 'spend', 'grow', 'open', 'walk', 'win', 'offer', 'remember', 'love', 'consider',
    'appear', 'buy', 'wait', 'serve', 'die', 'send', 'expect', 'build', 'stay', 'fall',
    'cut', 'reach', 'kill', 'remain', 'suggest', 'raise', 'pass', 'sell', 'require', 'report',
    'good', 'new', 'first', 'last', 'long', 'great', 'little', 'own', 'other', 'old',
    'right', 'big', 'high', 'different', 'small', 'large', 'next', 'early', 'young', 'important',
    'few', 'public', 'bad', 'same', 'able', 'full', 'sure', 'low', 'certain', 'hard',
    'real', 'true', 'simple', 'common', 'easy', 'basic', 'clear', 'nice', 'fine', 'quick'
}

def read_vocabulary_file(filepath):
    """Read vocabulary file and extract words"""
    words = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Match pattern: number. word - definition
            pattern = r'(\d+)\.\s+([a-z-]+)\s+-\s+(.+)'
            matches = re.findall(pattern, content)
            for num, word, definition in matches:
                words.append((int(num), word, definition.strip()))
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    return words

def assess_word_quality(word):
    """Assess if word is advanced or simple"""
    # Remove hyphens for checking
    base_word = word.replace('-', '')
    
    # Check if it's a simple word
    if base_word in SIMPLE_WORDS:
        return 'SIMPLE'
    
    # Check word length (advanced words tend to be longer)
    if len(word) >= 8:
        return 'ADVANCED'
    elif len(word) <= 4:
        return 'POTENTIALLY_SIMPLE'
    else:
        return 'ADVANCED'

def consolidate_and_assess():
    """Main function to consolidate and assess vocabulary"""
    
    # Read both files
    print("Reading vocabulary files...")
    file1_words = read_vocabulary_file('3000_ADVANCED_VOCABULARY_MASTER_LIST.md')
    file2_words = read_vocabulary_file('3000_VOCABULARY_CATEGORIES.md')
    
    all_words = file1_words + file2_words
    
    print(f"\nTotal words found: {len(all_words)}")
    print(f"From file 1: {len(file1_words)}")
    print(f"From file 2: {len(file2_words)}")
    
    # Assess quality
    simple_words = []
    potentially_simple = []
    advanced_words = []
    
    for num, word, definition in all_words:
        quality = assess_word_quality(word)
        if quality == 'SIMPLE':
            simple_words.append((num, word, definition))
        elif quality == 'POTENTIALLY_SIMPLE':
            potentially_simple.append((num, word, definition))
        else:
            advanced_words.append((num, word, definition))
    
    # Print assessment
    print(f"\n=== QUALITY ASSESSMENT ===")
    print(f"Advanced words: {len(advanced_words)}")
    print(f"Potentially simple words: {len(potentially_simple)}")
    print(f"Simple words (should be removed): {len(simple_words)}")
    
    if simple_words:
        print(f"\n[!] SIMPLE WORDS FOUND (should be replaced):")
        for num, word, definition in simple_words[:20]:  # Show first 20
            print(f"  {num}. {word} - {definition}")
        if len(simple_words) > 20:
            print(f"  ... and {len(simple_words) - 20} more")
    
    if potentially_simple:
        print(f"\n[?] POTENTIALLY SIMPLE WORDS (review recommended):")
        for num, word, definition in potentially_simple[:10]:  # Show first 10
            print(f"  {num}. {word} - {definition}")
        if len(potentially_simple) > 10:
            print(f"  ... and {len(potentially_simple) - 10} more")
    
    # Create consolidated file
    print(f"\nCreating consolidated file...")
    with open('3000_VOCABULARY_CONSOLIDATED.md', 'w', encoding='utf-8') as f:
        f.write("# 3000 Advanced Conversational Vocabulary - Complete Consolidated List\n\n")
        f.write("**Purpose:** Sophisticated vocabulary for daily and official communication\n")
        f.write("**Focus:** Advanced alternatives to simple words\n")
        f.write("**Total Words:** 3000 unique advanced conversational words\n\n")
        f.write("---\n\n")
        
        f.write("## Quality Assessment\n\n")
        f.write(f"- **Advanced words:** {len(advanced_words)}\n")
        f.write(f"- **Potentially simple:** {len(potentially_simple)}\n")
        f.write(f"- **Simple words (flagged):** {len(simple_words)}\n\n")
        f.write("---\n\n")
        
        f.write("## Complete Vocabulary List\n\n")
        
        for num, word, definition in all_words:
            quality = assess_word_quality(word)
            marker = ""
            if quality == 'SIMPLE':
                marker = " [SIMPLE - REPLACE]"
            elif quality == 'POTENTIALLY_SIMPLE':
                marker = " [REVIEW]"
            
            f.write(f"{num}. **{word}**{marker} - {definition}\n")
    
    print(f"\n[OK] Consolidated file created: 3000_VOCABULARY_CONSOLIDATED.md")
    print(f"\nLegend:")
    print(f"  [OK] = Advanced word (good)")
    print(f"  [?] = Potentially simple (review)")
    print(f"  [X] = Simple word (should replace)")

if __name__ == "__main__":
    consolidate_and_assess()
