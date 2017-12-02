import re

sentences = []
words = []
len_words = []
len_sentences = []

filename1 = "data/paragraph_1.txt"
file1 = open(filename1, 'r')
content1 = file1.read()
#print(content1)
sentence1 = re.split(r' *[\.\?!][\'"\)\]]* *', content1)
for line in sentence1:
    sentences.append(line)
    count1 = len(re.findall(r'\w+', line))
    len_sentences.append(count1)
del sentences[-1]
words1 = content1.split()
#print(words1)
for w in words1:
    words.append(w)
    number_letters1 = len(w)
    len_words.append(number_letters1)

filename2 = "data/paragraph_2.txt"
file2 = open(filename2, 'r')
content2 = file2.read()
#print(content2)
sentence2 = re.split(r' *[\.\?!][\'"\)\]]* *', content2)
for line in sentence2:
    sentences.append(line)
    count2 = len(re.findall(r'\w+', line))
    len_sentences.append(count2)
#print(sentences)
del sentences[-1]
words2 = content2.split()
#print(words2)
for w in words2:
    words.append(w)
    number_letters2 = len(w)
    len_words.append(number_letters2)

number_words = len(words)
#print(number_words)
#print(sentence)
# Q1
print("Approximate Word Count: " + str(number_words))

number_sentences = len(sentences)
#print(number_sentences)
#print(sentences)
# Q2
print("Approximate Sentence Count: " + str(number_sentences))

average_letter_count = sum(len_words)/len(len_words)
#Q3
print("Average Letter Count: " + str(average_letter_count))

new_len_sentences = [x for x in len_sentences if x != 0]
average_sentence_length = sum(new_len_sentences)/len(new_len_sentences)
#Q4
print("Average Sentence Length: " + str(average_sentence_length))

