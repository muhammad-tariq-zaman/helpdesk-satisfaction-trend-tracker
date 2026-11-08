"""Track weekly helpdesk satisfaction ratings and their trend.

Usage: python3 main.py ratings.csv
CSV columns: date (ISO),agent,rating (1-5).
Per ISO week: average rating, response count, and the trend
against the previous week — UP, DOWN or FLAT (a change under
0.1 counts as FLAT). Weeks in chronological order.
"""
import argparse, csv, sys
from collections import defaultdict
from datetime import date

def trend(rows):
    per_week = defaultdict(list)
    for row in rows:
        week = date.fromisoformat(row["date"].strip()).isocalendar()[:2]
        per_week[week].append(int(row["rating"]))
    out = []
    previous_avg = None
    for week in sorted(per_week):
        ratings = per_week[week]
        avg = round(sum(ratings) / len(ratings), 2)
        if previous_avg is None:
            direction = "—"
        elif avg - previous_avg >= 0.1:
            direction = "UP"
        elif previous_avg - avg >= 0.1:
            direction = "DOWN"
        else:
            direction = "FLAT"
        out.append((f"{week[0]}-W{week[1]:02d}", avg, len(ratings), direction))
        previous_avg = avg
    return out

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for week, avg, count, direction in trend(list(csv.DictReader(f))):
            print(f"{week}: {avg:.2f} avg ({count} rating(s)), trend {direction}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
