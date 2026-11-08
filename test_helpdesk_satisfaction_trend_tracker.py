import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import trend

def row(d, a, r):
    return {"date": d, "agent": a, "rating": str(r)}

class TestSatisfactionTrend(unittest.TestCase):
    def test_weekly_average(self):
        r = trend([row("2026-11-02", "ali", 4), row("2026-11-03", "sara", 5)])
        self.assertEqual(r[0][1], 4.5)
        self.assertEqual(r[0][2], 2)
    def test_trend_up(self):
        r = trend([row("2026-10-26", "ali", 3), row("2026-11-02", "ali", 5)])
        self.assertEqual(r[1][3], "UP")
    def test_trend_down(self):
        r = trend([row("2026-10-26", "ali", 5), row("2026-11-02", "ali", 3)])
        self.assertEqual(r[1][3], "DOWN")
    def test_small_change_is_flat(self):
        r = trend([row("2026-10-26", "ali", 4), row("2026-10-27", "ali", 4),
                   row("2026-11-02", "ali", 4), row("2026-11-03", "ali", 4)])
        self.assertEqual(r[1][3], "FLAT")
    def test_first_week_has_no_trend(self):
        r = trend([row("2026-11-02", "ali", 4)])
        self.assertEqual(r[0][3], "—")
    def test_empty_input(self):
        self.assertEqual(trend([]), [])
