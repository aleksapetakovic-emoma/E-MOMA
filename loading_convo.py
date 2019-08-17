import re

path_to_movie_lines = './movie_lines.txt'
path_to_movie_conversations = './movie_conversations.txt'
path_to_new_lines = './AddedDiag.txt'

# Maximum number of samples to pre-process (Cornell)
MAX_SAMPLES = 50000


def preprocess_sentence(sentence):
    sentence = sentence.lower().strip()
    # creating a space between a word and the punctuation following it
    # eg: "he is a boy." => "he is a boy ."
    sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
    sentence = re.sub(r'[" "]+', " ", sentence)
    # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
    sentence = re.sub(r"[^a-zA-Z]+", " ", sentence)
    sentence = sentence.strip()
    return sentence


# Load cornell dialogues
def load_conversations():
    # dictionary of line id to text
    id2line = {}
    with open(path_to_movie_lines, errors='ignore') as file:
        lines = file.readlines()
    for line in lines:
        parts = line.replace('\n', '').split(' +++$+++ ')
        id2line[parts[0]] = parts[4]

    inputsC, outputsC = [], []
    with open(path_to_movie_conversations, 'r') as file:
        lines = file.readlines()
    for line in lines:
        parts = line.replace('\n', '').split(' +++$+++ ')
        # get conversation in a list of line ID
        conversation = [line[1:-1] for line in parts[3][1:-1].split(', ')]
        for i in range(len(conversation) - 1):
            inputsC.append(preprocess_sentence(id2line[conversation[i]]))
            outputsC.append(preprocess_sentence(id2line[conversation[i + 1]]))
      #      format_movie(preprocess_sentence(id2line[conversation[i]]))
            if len(inputsC) >= MAX_SAMPLES:
                return inputsC, outputsC
    return inputsC, outputsC


# Load reddit comments and pre-process them
def load_reddit():
    input, output = [], []
    file_q = open('test.from', "r")
    file_a = open('test.to', "r")
    line_q = file_q.readlines()
    line_a = file_a.readlines()

    assert len(line_q) == len(line_a)

    for i in range(len(line_q)):

        line_q[i].replace('\n', '')
        line_a[i].replace('\n', '')

        input.append(preprocess_sentence(line_q[i]))
        output.append(preprocess_sentence(line_a[i]))

    print(input)
    print(output)
    return input, output

# Load the AddedDiag.txt file and pre-process it
def load_addedDiag():
    input, output = [], []
    with open(path_to_new_lines, errors='ignore') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i].replace('\n', '')
        if i % 2 == 0:
            input.append(preprocess_sentence(lines[i]))
        else:
            output.append(preprocess_sentence(lines[i]))
    print(input)
    print(output)
    return input, output


# Add input and desired output for the TF model
def add_new(q, a):
    #
    # to be replace with a bash command when running on linux to avoid memory issues
    #
    addedFile = open(path_to_new_lines, "a")
    addedFile.write(q + "\n")
    addedFile.write(a + "\n")
