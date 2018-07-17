from csv import reader
from collections import defaultdict

def summarize(input_file):
    a1 = 0
    a2 = 0
    num_prescriber, total_cost = 'num_prescriber', 'total_cost'
    cache = defaultdict(lambda:{num_prescriber:set(), total_cost: 0})
    # a) read each line and map into dictionary
    # footnote below on reading large txt files
    with open(input_file) as f:
        header_line = next(f)
        for line in f:
            prescriber_last_name, prescriber_first_name, drug_name, drug_cost = next(reader([line]))[-4:]
            cache[drug_name][num_prescriber].add(prescriber_last_name + prescriber_first_name)
            cache[drug_name][total_cost] += float(drug_cost)

    # b) iterate through dictionary and write onto output txt file
    output_file = open('./output/top_cost_drug.txt','w')
    output_file.write("drug_name,num_prescriber,total_cost\n")
    for k,v in cache.iteritems():
        a1 = len(v['num_prescriber'])
        a2 += v['total_cost']
        # use double quotations for drug_name if the data contains embedded delimiters -- this maintains format integrity of source data
        drug_name = '"' + k + '"' if (',' in k) else k
        output_file.write('{0},{1},{2}\n'.format(drug_name, len(v[num_prescriber]), v[total_cost]))
    output_file.close()
    return a1, a2
