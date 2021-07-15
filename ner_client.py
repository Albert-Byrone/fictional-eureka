import spacy

class NamedEntityClient:
    def __init__(self, model):
        self.model = model
        
    def get_entity(self, sentence):
        doc = self.model(sentence)
        entities = [{ 'ent': ent.text, 'label': self.map_label( ent.label_)} for ent in doc.ents]
        return { 'ents': entities, 'html': ''}
    @staticmethod
    def  map_label(label):
        label_map = {
            'PERSON': 'Person'
        }
        return label_map.get(label)