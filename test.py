import unittest
import diseases
import diagnost


class MyTestCase(unittest.TestCase):
    def test_base(self):
        self.assertEqual(True, True)  # add assertion here

    def test_dict_equal(self):
        self.assertDictEqual({"type": "soma", "headache": False, "cough": True, "loose_smell": False},
                             diseases.cold.symptoms)

    def test_default_disease(self):
        t = diagnost.Therapist()
        t.symptoms = {"type":None}
        self.assertEqual(t.diagnose(), diseases.default)

    def test_default_disease_harder(self):
        t = diagnost.Therapist()
        t.symptoms = {"type": "soma", "headache": False, "cough": False, "loose_smell": False}
        self.assertEqual(t.diagnose(), diseases.default)

    def test_false_psycho_disease(self):
        t = diagnost.Therapist()
        t.symptoms = {"type":"psycho", "hal": "False"}


if __name__ == '__main__':
    unittest.main()
