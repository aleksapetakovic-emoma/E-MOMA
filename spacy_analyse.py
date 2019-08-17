import spacy


nlp = spacy.load('en')


def give_subject(sentence):
    parsed_text = nlp(u""+sentence)
    for text in parsed_text:
        # subject would be
        if text.dep_ == "nsubj":
            subject = text.orth_
            return subject


def give_dobject(sentence):
    parsed_text = nlp(u""+sentence)
    for text in parsed_text:
        # subject would be
        if text.dep_ == "dobj":
            subject = text.orth_
            return subject


def give_iobject(sentence):
    parsed_text = nlp(u""+sentence)
    for text in parsed_text:
        # subject would be
        if text.dep_ == "iobj":
            subject = text.orth_
            return subject


def give_pobject(sentence):
    parsed_text = nlp(u""+sentence)
    for text in parsed_text:
        # subject would be
        if text.dep_ == "pobj":
            subject = text.orth_
            return subject


def give_root(sentence):
    parsed_text = nlp(u""+sentence)
    for text in parsed_text:
        # subject would be
        if text.dep_ == "ROOT":
            subject = text.orth_
            return subject


def analyse_sentence(nlp_text):
    for token in nlp_text:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)


