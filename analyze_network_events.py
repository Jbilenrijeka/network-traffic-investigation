import csv
import sys
from collections import Counter
from pathlib import Path

TRAINING_WATCHLIST = {"updates-example.invalid", "login-example.invalid"}

def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/network_events.csv")
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"Events analyzed: {len(rows)}")
    domains = Counter(r.get("query_or_domain", "").lower() for r in rows if r.get("event_type") == "dns")
    print("\nDNS query counts:")
    for domain, count in domains.most_common():
        print(f"  {domain}: {count}")
    print("\nTraining watchlist matches:")
    matches = sorted({r.get("query_or_domain", "").lower() for r in rows} & TRAINING_WATCHLIST)
    print("\n".join(f"  {x}" for x in matches) if matches else "  None")
    print("\nA match only indicates a local training-list hit; validate reputation and context independently.")

if __name__ == "__main__":
    main()
