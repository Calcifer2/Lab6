sorted_map_file = 'text.txt.map.sorted'
final_file = 'final.txt'

try:
    in_file = open(sorted_map_file, 'r', encoding='utf-8')
    out_file = open(final_file, 'w', encoding='utf-8')
    prev_key = ''
    val_counter = 0
    for line in in_file:
        key, val = line.split('\t')
        if key == prev_key:
            val_counter += 1
        else:
            out_file.write(f'{prev_key}\t{val_counter}\n')
            val_counter = 1 
            prev_key = key




except IOError:
    print(0)