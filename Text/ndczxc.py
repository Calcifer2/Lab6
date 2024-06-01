import re

# remove any non-words and split lines into separate words
# finally, convert all words to lowercase
def splitter(line):
    line = re.sub(r'^\W+|\W+$', '', line)
    return map(str.lower, re.split(r'\W+', line))
    
input_file = 'text.txt'
map_file = 'text.txt.map'

# Implement our mapping function
sums = {}
try:
    in_file = open(input_file, 'r', encoding='utf-8')
    out_file = open(map_file, 'w', encoding='utf-8')

    for line in in_file:
        for word in splitter(line):
            out_file.write(word.lower() + "\t1\n")
            
    in_file.close()
    out_file.close()

except IOError:
    print("error performing file operation")