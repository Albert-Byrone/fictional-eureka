# from _typeshed import Self
import unittest
from unittest import result
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble
class TestNerClient(unittest.TestCase):

    # tes to return a dictionary given an empty string
    def test_empty_string(self):
        model = NerModelTestDouble('eng')
        model.return_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_entity("")
        self.assertIsInstance(ents, dict) 


    def test_when_given_non_string(self):
        model = NerModelTestDouble('eng')
        model.return_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_entity("Albert is my name")
        self.assertIsInstance(ents, dict) 

    def test_get_ent_given_spacy_PERSON_is_returned_seriliaze_to_person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{ 'text': 'Albert Byrone', 'label_': 'PERSON'}]
        model.return_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_entity("Pass some string")
        expected_results ={ 'ents': [ { 'text': 'Albert Byrone', 'label': 'PERSON'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_results['ents'])

    
