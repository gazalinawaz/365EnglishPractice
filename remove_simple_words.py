"""
Remove simple words from vocabulary list and suggest advanced replacements
"""

import re

# Comprehensive list of simple/common words to remove
SIMPLE_WORDS_TO_REMOVE = {
    # Basic verbs
    'provide', 'offer', 'suggest', 'include', 'meet', 'consider', 'believe', 
    'expect', 'allow', 'build', 'create', 'show', 'give', 'take', 'make',
    'get', 'use', 'find', 'help', 'need', 'want', 'know', 'think', 'see',
    'come', 'go', 'work', 'call', 'try', 'ask', 'turn', 'move', 'live',
    'seem', 'leave', 'talk', 'put', 'mean', 'keep', 'let', 'begin', 'start',
    'hear', 'play', 'run', 'hold', 'bring', 'happen', 'write', 'sit', 'stand',
    'lose', 'pay', 'learn', 'change', 'lead', 'understand', 'watch', 'follow',
    'stop', 'speak', 'read', 'add', 'spend', 'grow', 'open', 'walk', 'win',
    'remember', 'love', 'appear', 'buy', 'wait', 'serve', 'die', 'send',
    'reach', 'kill', 'remain', 'raise', 'pass', 'sell', 'require', 'report',
    'continue', 'set', 'feel', 'become', 'tell',
    
    # Basic adjectives
    'good', 'new', 'bad', 'old', 'great', 'big', 'small', 'high', 'low',
    'long', 'short', 'early', 'late', 'young', 'important', 'little', 'large',
    'next', 'few', 'public', 'same', 'able', 'full', 'sure', 'certain', 'hard',
    'real', 'true', 'simple', 'common', 'easy', 'basic', 'clear', 'nice', 'fine',
    'quick', 'fast', 'slow', 'hot', 'cold', 'warm', 'cool', 'right', 'wrong',
    'different', 'own', 'other', 'main', 'free', 'ready', 'strong', 'weak',
    'heavy', 'light', 'dark', 'bright', 'clean', 'dirty', 'safe', 'dangerous',
    
    # Basic nouns that might appear as verbs/adjectives
    'form', 'plan', 'view', 'link', 'need', 'work', 'place', 'time', 'year',
    'way', 'day', 'thing', 'man', 'world', 'life', 'hand', 'part', 'child',
    'eye', 'woman', 'case', 'point', 'week', 'company', 'system', 'program',
    
    # Borderline simple words
    'solid', 'valid', 'sound', 'firm', 'pure', 'whole', 'total', 'full',
    'complete', 'entire', 'main', 'chief', 'major', 'minor', 'prime',
    'fresh', 'current', 'present', 'past', 'future', 'near', 'far',
    'deep', 'wide', 'broad', 'narrow', 'thick', 'thin', 'rich', 'poor',
}

# Advanced replacements for common simple words
REPLACEMENTS = {
    'provide': 'furnish',
    'offer': 'proffer',
    'suggest': 'propose',
    'include': 'encompass',
    'meet': 'satisfy',
    'consider': 'contemplate',
    'believe': 'presume',
    'expect': 'anticipate',
    'allow': 'permit',
    'build': 'construct',
    'create': 'generate',
    'new': 'novel',
    'basic': 'fundamental',
    'common': 'prevalent',
    'solid': 'robust',
    'valid': 'legitimate',
    'certain': 'definitive',
    'own': 'possess',
    'simple': 'elementary',
    'clear': 'lucid',
    'good': 'exemplary',
    'bad': 'detrimental',
    'big': 'substantial',
    'small': 'negligible',
    'fast': 'expeditious',
    'slow': 'gradual',
    'hard': 'arduous',
    'easy': 'facile',
    'true': 'authentic',
    'false': 'spurious',
    'right': 'correct',
    'wrong': 'erroneous',
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

def is_simple_word(word):
    """Check if word is simple"""
    base_word = word.replace('-', '')
    return base_word in SIMPLE_WORDS_TO_REMOVE

def analyze_and_report():
    """Analyze vocabulary and report simple words"""
    
    # Read both files
    print("Reading vocabulary files...")
    file1_words = read_vocabulary_file('3000_ADVANCED_VOCABULARY_MASTER_LIST.md')
    file2_words = read_vocabulary_file('3000_VOCABULARY_CATEGORIES.md')
    
    all_words = file1_words + file2_words
    
    # Find simple words
    simple_found = []
    for num, word, definition in all_words:
        if is_simple_word(word):
            replacement = REPLACEMENTS.get(word, '[NEEDS REPLACEMENT]')
            simple_found.append((num, word, definition, replacement))
    
    print(f"\n=== SIMPLE WORDS ANALYSIS ===")
    print(f"Total words analyzed: {len(all_words)}")
    print(f"Simple words found: {len(simple_found)}")
    print(f"Percentage simple: {len(simple_found)/len(all_words)*100:.1f}%")
    
    if simple_found:
        print(f"\n=== SIMPLE WORDS TO REMOVE ===")
        print(f"{'#':<6} {'Word':<20} {'Suggested Replacement':<25} {'Original Definition'}")
        print("-" * 100)
        for num, word, definition, replacement in simple_found:
            print(f"{num:<6} {word:<20} {replacement:<25} {definition[:50]}")
    
    # Save report
    with open('SIMPLE_WORDS_REPORT.txt', 'w', encoding='utf-8') as f:
        f.write("=== SIMPLE WORDS TO REMOVE FROM VOCABULARY LIST ===\n\n")
        f.write(f"Total words analyzed: {len(all_words)}\n")
        f.write(f"Simple words found: {len(simple_found)}\n")
        f.write(f"Percentage: {len(simple_found)/len(all_words)*100:.1f}%\n\n")
        
        f.write("List of simple words with suggested replacements:\n")
        f.write("-" * 100 + "\n")
        for num, word, definition, replacement in simple_found:
            f.write(f"{num}. {word} -> {replacement}\n")
            f.write(f"   Original: {definition}\n\n")
    
    print(f"\n[OK] Report saved to: SIMPLE_WORDS_REPORT.txt")
    
    return simple_found

if __name__ == "__main__":
    simple_words = analyze_and_report()
