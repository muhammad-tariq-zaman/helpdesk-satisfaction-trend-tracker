# helpdesk-satisfaction-trend-tracker

Track weekly helpdesk satisfaction ratings from a CSV: average rating and response count per ISO week, with the trend against the previous week — UP, DOWN or FLAT (changes under 0.1 count as FLAT).

## How to run

```sh
python3 main.py ratings.csv
```

## Example output

```
2026-W44: 3.00 avg (2 rating(s)), trend —
2026-W45: 4.50 avg (2 rating(s)), trend UP
```

Standard library only. Run the tests with `python3 -m unittest discover`.
