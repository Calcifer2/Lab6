import pandas
world_file = 'world.csv'
region_file = 'region.map'


try:
    in_file = pandas.read_csv(world_file)
    out_file = open(region_file, 'w', encoding='utf-8')
    for name in in_file['Region']:
        out_file.write(name + "\t1\n")


except IOError:
    print ('loser')