import re
# Put sentences in chemu_input_sentence.txt together.
file_name = 'chemu_input_sentence.txt'
file = open(file_name)
lines = file.readlines()
cleaned = []
for i in lines:
    i = i.replace("\n","")
    me = i[i.rindex('|')+1:]
    cleaned.append(me)

filename = ('chemu_input_sentence_cleaned.txt')
f=open(filename,'w')
for line in cleaned:
    f.write(line + "\n")
f.close()
text = open('chemu_input_sentence_cleaned.txt').read()

# Remove all serial numbers from the SCILK output file.
file_name = 'SciLK_Annotations.txt'
file = open(file_name)
lines = file.readlines()
cleaned = []

for i in lines:
    i = i.replace("\n","")
    me = i[i.rindex('|')+1:]
    cleaned.append(me)

# Find the index of every word in the cleaned input file.
def getLineNumber(file_name, string_to_search):
    line_number = 0
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if line.count(string_to_search)>0:
                count = line.count(string_to_search)
                list_of_results.extend([line_number] * count)
    return list_of_results

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

unique_cleaned = []
for x in cleaned:
    if x not in unique_cleaned:
        unique_cleaned.append(x)

n = 1
brat_format_lines = []
for i in unique_cleaned:
    line_number = getLineNumber('chemu_input_sentence_cleaned.txt',i)
    length = len(i)
    n_str=str(n)
    start_indexes = list(find_all(text, i))
    for x, number in zip(start_indexes, line_number):
        t = n
        t_str = str(t)
        start_postition = x+number-1
        end_position = x+number+length-1
        T = "T"+t_str+'\t' + 'Chemical' +' '+ str(start_postition) +' '+ str(end_position) + '\t' + i
        t = t + 1
        n = n + 1
        brat_format_lines.append(T)

f=open('chemu_input_sentence_cleaned.ann','w')
for line in brat_format_lines:
    f.write(line + "\n")
