import unittest
from src.algorithms import linear_search, binary_search, build_hash_index, hash_search

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.records = [{"summons_number":"003"},{"summons_number":"001"},{"summons_number":"002"}]
        self.sorted_records = sorted(self.records, key=lambda r:r["summons_number"])
    def test_linear_found(self):
        self.assertEqual(linear_search(self.records,"002")[0]["summons_number"],"002")
    def test_linear_missing(self):
        self.assertIsNone(linear_search(self.records,"999")[0])
    def test_binary_found(self):
        self.assertEqual(binary_search(self.sorted_records,"003")[0]["summons_number"],"003")
    def test_binary_missing(self):
        self.assertIsNone(binary_search(self.sorted_records,"999")[0])
    def test_hash_found(self):
        self.assertEqual(hash_search(build_hash_index(self.records),"001")[0]["summons_number"],"001")
    def test_hash_missing(self):
        self.assertIsNone(hash_search(build_hash_index(self.records),"999")[0])

if __name__ == "__main__":
    unittest.main()
