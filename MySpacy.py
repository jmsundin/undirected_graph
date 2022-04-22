import spacy
import AsciiDocToHtml

class MySpacy():
    def __init__(self):
        pass

    
    def load_text_into_spacy(self, text: str):
        nlp = spacy.load('en_core_web_md')
        config = {'punct_chars': None}
        nlp.add_pipe('sentencizer', config=config)
        return nlp(text)


    def text_to_noun_chunks(self, doc: spacy.doc.Doc):
        sentences = []
        noun_phrases = []

        for sent in doc.sents:
            sent_noun_chunks = list(sent.noun_chunks)
            if sent_noun_chunks:
                sentences.append(sent)
                noun_phrases.append(max(sent_noun_chunks))
            sent_vecs = []
            for sent in sentences:
                sent_vecs.append(sent.vector)


if __name__ == "__main__":
    my_text_adoc = 'NLPIA_Ch6_my_section.adoc'
    my_text_html = 'NLPIA_Ch6_my_section.html'

    my_asciiDocToHtml = AsciiDocToHtml(my_text_adoc, my_text_html)
    my_asciiDocToHtml.run_ascii_doc3()
    text = my_asciiDocToHtml.run_beautiful_soup()

    if text != None:
        doc = MySpacy.load_text_into_spacy(text)
        MySpacy.text_to_noun_chunks(doc)
