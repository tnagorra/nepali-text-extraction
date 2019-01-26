import unittest
import ttf2utf
import glob
import os


class Test_all_vectors(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName=methodName)
        self.all_rules = ttf2utf.load_rules('rules/')

    def load_vectors(self, vector_file):
        vectors = []
        with open(vector_file, encoding='utf-8') as in_file:
            for line in in_file:
                vector = line.split('\t')
                vectors.append((vector[0], vector[1].rstrip('\r\n')))

    def test(self):
        for vfilename in glob.glob('vectors/*.vector'):
            newkey = os.path.splitext(os.path.basename(vfilename))[0].lower()
            rule = self.all_rules[newkey]
            with open(vfilename, encoding='utf-8') as v_file:
                print('Testing', newkey)
                for line in v_file:
                    vec = line.split('\t')
                    vec[1] = vec[1].rstrip('\r\n')
                    converted = ttf2utf.convert_word(vec[0], rule)
                    self.assertEqual(converted, vec[1],
                             'got {0} expected {1} for {2} in {3}'.format(converted, vec[1], vec[0], vfilename))



if __name__ == "__main__":
    unittest.main()
