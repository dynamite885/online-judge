import sys ,re
inp = sys.stdin.readline

next=inp()
while next != '':
    word_counts = {}
    line = inp().strip()
    while line != 'EndOfText':
        words = re.split(r'[^a-z]+', line.lower())
        for w in words:
            word_counts[w] = word_counts.get(w,0)+1
        line = inp().strip()
        
    result = [str for str, count in word_counts.items() if count == int(next)]
    print('\n'.join(sorted(result)) if len(result) != 0 else 'There is no such word.')
    next=inp()
    if next != '':
        print()