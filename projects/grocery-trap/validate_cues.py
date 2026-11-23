import csv

def main():
    words = {}
    for r in csv.DictReader(open("WORDS.tsv", encoding="utf-8"), delimiter="\t"):
        key = f"{r['line']}.{r['i']}"
        words[key] = float(r["start"])

    # Count words per line
    line_word_counts = {}
    for r in csv.DictReader(open("WORDS.tsv", encoding="utf-8"), delimiter="\t"):
        ln = r['line']
        line_word_counts[ln] = max(line_word_counts.get(ln, 0), int(r['i']) + 1)

    scenes = [r for r in csv.reader(open("SCENES.tsv", encoding="utf-8"), delimiter="\t") if r and not r[0].startswith("#") and r[0] != "cue"]

    bad = []
    for r in scenes:
        cue = r[0].strip().lstrip("+")
        if cue not in words:
            ln, _, idx = cue.partition(".")
            max_idx = line_word_counts.get(ln, 0)
            bad.append((r[0], f"line {ln} has {max_idx} words (indices 0..{max_idx-1})"))
            
    if bad:
        print(f"Found {len(bad)} invalid cues:")
        for b, note in bad:
            print(f"  {b} -> {note}")
    else:
        print("All cues in SCENES.tsv are 100% valid!")

if __name__ == "__main__":
    main()
