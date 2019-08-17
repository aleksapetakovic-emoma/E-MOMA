from db_commands import Database
import markovify
import random
# import transformer_chatbot as tc
import spacy_analyse


def markov(input_message):
    message = ''
    with open("test.to", encoding="utf8") as f:
        reddit_sample = f.readlines()

    check_subject = spacy_analyse.give_subject(input_message)
    check_pobject = spacy_analyse.give_pobject(input_message)
    check_root = spacy_analyse.give_root(input_message)
    print(check_subject)
    print(check_pobject)
    print(check_root)
    db = Database()
    messages = db.get_items()
    messages = messages + reddit_sample
    model = markovify.Text(messages)

    #insert options for hey hi and so on or train a model for those ones
    # should be moved and turned into methods to avoid redundancies 
    if check_pobject is not None:
        try:
            first_word = check_pobject
            if first_word == ("you" or "You" or "Ya" or "ya"):
                try:
                    first_word = "I"
                    message = model.make_sentence_with_start(first_word, max_chars=80)
                    print("pobj I")
                except:
                    first_word = "i"
                    message = model.make_sentence_with_start(first_word, max_chars=80)
                    print("pobj i")
            else:
                # make_sentence_with_start was modified from the original package to include a character limit
                message = model.make_sentence_with_start(first_word, max_chars=80)
                print("pobj")

        except:
            message = give_neutral()
    elif check_subject is not None and check_subject != "you":
        try:
            first_word = check_subject
            # make_sentence_with_start was modified from the original package to include a character limit
            message = model.make_sentence_with_start(first_word, max_chars=80)
            print("subj")
        except:
            message = give_neutral()
    elif check_subject == ("you" or "You" or "Ya" or "ya"):
        try:
            first_word = "I"
            message = model.make_sentence_with_start(first_word, max_chars=80)
        except:
            first_word = "i"
            message = model.make_sentence_with_start(first_word, max_chars=80)

        print("nsubj I or i")
    elif check_root is not None:
        try:
            first_word = check_root
            message = model.make_sentence_with_start(first_word, max_chars=80)
            print("root")
        except:
            message = give_neutral()


# If it cannot construct a sentence using the specified first word, it will attempt to use the transformer model
    if message is not None:
        return message
    else:
        try:
            # return tc.predict(input_message) until the transformer model is not adequately
            return give_neutral()
        except:
            return "I am not sure"


def give_neutral():
    neutral_answers = ["I am not sure", "I really don't know", "Whatever", "Dunno", "Hmmm", "I'm not sure", "Don't know"]
    return random.choice(neutral_answers)