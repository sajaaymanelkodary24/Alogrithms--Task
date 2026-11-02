from collections import Counter
import heapq
import re

def most_common_words(text, k):
    if k < 1:return []
    counts=Counter(re.findall(r"[a-zA-Z0-9_]+",text.casefold()))
    # Sort by descending frequency, then alphabetically for deterministic ties.
    return sorted(counts.items(),key=lambda pair:(-pair[1],pair[0]))[:k]

if __name__=="__main__":
    sentence=input("Enter text: ")
    try:k=int(input("How many top words? "))
    except ValueError:raise SystemExit("Please enter an integer for k.")
    for word,frequency in most_common_words(sentence,k):
        print(f"{word}: {frequency}")
