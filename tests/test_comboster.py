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

        with self.subTest("Should contain 'ca'"):
            self.assertIn('ca', out)

        with self.subTest("Should not contain 'a', 'b', and 'c'"):
            self.assertNotIn('a', out)
            self.assertNotIn('b', out)
            self.assertNotIn('c', out)

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

    @unittest.skip("")
    def test_random_unique(self):
        seed = 1

        for seq in self.seqs:
            combos = []
            for combo in comboster.random_unique(seq, seed=seed):
                combos.append(combo)

            with self.subTest(seq = seq):
                ncombos = len(list(comboster.all(seq)))
                self.assertEqual(len(combos), ncombos)

if __name__ == '__main__':
    unittest.main()
