import unittest
from update import parse, make_body, validate_budget, DESKTOP_MAX_RULES

class FilterTests(unittest.TestCase):
    def test_normalize_and_preserve(self):
        rules, excluded = parse("[Adblock Plus 2.0]\n! comment\n0.0.0.0 ADS.example.com\n@@||ads.example.com^$domain=test.com\n##.ad\n")
        self.assertEqual(rules, ["||ads.example.com^", "@@||ads.example.com^$domain=test.com", "##.ad"])
        self.assertEqual(excluded, 0)

    def test_remove_unsafe_scripts(self):
        rules, excluded = parse("example.org#%#//scriptlet('trusted-replace-argument', 'x')\nexample.org##+js(foo)\n||ads.example.org^\n")
        self.assertEqual(rules, ["||ads.example.org^"])
        self.assertEqual(excluded, 2)

    def test_dedup(self):
        self.assertEqual(make_body(["a","b"], {"a":(["a","b"],0), "b":(["b","c"],0)}), (["a","b","c"],1))

    def test_bad_input(self):
        for data in ("<html>bad</html>", "!#if ext_ublock\n||ads.example.com^"):
            with self.assertRaises(ValueError):
                parse(data)

    def test_desktop_budget(self):
        validate_budget("desktop", ["r"] * DESKTOP_MAX_RULES, "")
        with self.assertRaisesRegex(ValueError, "budget exceeded"):
            validate_budget("desktop", ["r"] * (DESKTOP_MAX_RULES + 1), "")

    def test_legacy_migration(self):
        old = "! Title: legacy\n" + "r\n" * 92342
        validate_budget("desktop", ["r"] * 1200, old)

    def test_drop_guard_stays_active(self):
        old = "! Policy: supplement-v1\n" + "r\n" * 1200
        with self.assertRaisesRegex(ValueError, "Suspicious"):
            validate_budget("desktop", ["r"] * 800, old)
        with self.assertRaisesRegex(ValueError, "Suspicious"):
            validate_budget("android", ["r"] * 1500, "r\n" * 3000)

if __name__ == "__main__":
    unittest.main()
