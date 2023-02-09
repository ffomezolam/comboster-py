from context import comboster

import unittest

class Testcomboster(unittest.TestCase):
    def setUp(self):
        self.seqs = ['ahoy', 'ambling', 'ambitious', 'abracadabra']

    def test_all(self):
        out = list(comboster.all('abc'))

        with self.subTest("Size should equal all possible combos"):
            self.assertEqual(len(out), 12)

        with self.subTest("Should contain 'bac'"):
            self.assertIn('bac', out)

        with self.subTest("Should contain 'cba'"):
            self.assertIn('cba', out)

        with self.subTest("Should contain 'ca'"):
            self.assertIn('ca', out)

        with self.subTest("Should not contain 'a', 'b', and 'c'"):
            self.assertNotIn('a', out)
            self.assertNotIn('b', out)
            self.assertNotIn('c', out)

        with self.subTest("4 item input should have 72 combos"):
            self.assertEqual(len(list(comboster.all('ahoy'))), 72)

    def test_seq_all(self):
        for seq in self.seqs:
            out = list(comboster.seq_all(seq))
            for combo in out:
                with self.subTest(combo = combo, seq = seq):
                    self.assertIn(combo, seq)

            with self.subTest(seq = seq, out = out):
                self.assertIn(seq[-2:], out)
                self.assertIn(seq[-4:-2], out)
                self.assertIn(seq[1:4], out)

    def test_seq_to_end(self):
        for seq in self.seqs:
            out = list(comboster.seq_to_end(seq))
            for combo in out:
                with self.subTest(combo = combo, seq = seq):
                    self.assertIn(combo, seq)

            with self.subTest(seq = seq, out = out):
                self.assertNotIn(seq[-4:-2], out)
                self.assertIn(seq[-3:], out)
                self.assertNotIn(seq[0:3], out)
                self.assertIn(seq[0:], out)

    def test_none(self):
        for seq in self.seqs:
            out = list(comboster.none(seq))

            with self.subTest(seq = seq, out = out):
                self.assertEqual(len(out), 1)
                self.assertEqual(out[0], seq)

    def test_random_unique(self):
        seed = 1

        for seq in self.seqs[:2]:
            combos = list(comboster.random_unique(seq, seed=seed))

            with self.subTest("Should have same length as all combos", seq = seq):
                ncombos = len(list(comboster.all(seq)))
                self.assertEqual(len(list(combos)), ncombos)

        for seq in self.seqs[2:]:
            with self.subTest("Should have maximum length of 282240", seq = seq):
                count = 0
                for combo in comboster.random_unique(seq, seed=seed):
                    count += 1

                self.assertEqual(count, 100_000)

if __name__ == '__main__':
    unittest.main()
