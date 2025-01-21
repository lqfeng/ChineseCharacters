pre_id = ""
pre_simplified = ""
traditional_list = []
variant_list = []

idx_char_map = {}

def print_str(pre_id,pre_simplified,traditional_list,variant_list):
    traditional_str = ""
    sum_len = sum([len(x) for x in traditional_list])
    #print(sum_len)
    if len(traditional_list) and sum_len:
        traditional_str = "("+"|".join(traditional_list)+")"

    variant_str = ""
    sum_len = sum([len(x) for x in variant_list])
    #print(sum_len)
    if len(variant_list) and sum_len:
        variant_str = "["+"|".join(variant_list)+"]"

    idx_char_map[pre_id] = traditional_str + "\t" + variant_str
    #print(pre_id,pre_simplified,traditional_str,variant_str,sep="\t")

for line in open("规范字与繁体字、异体字对照表.txt",encoding='utf-8'):
    idx, simplified, traditional, variant = line.split("\t")
    if pre_id != idx and idx!="〃":
        if pre_id!="":
            print_str(pre_id,pre_simplified,traditional_list,variant_list)

        pre_id = idx
        pre_simplified = simplified
        traditional_list = []
        variant_list = []

    if traditional == "～":
        traditional=simplified
    elif "(" in traditional:
        traditional = traditional.replace("(","").replace(")","")


    variant = variant.strip()
    if "[" in variant:
        variant = variant.replace("[","").replace("]","")

    if traditional!="" or variant!="":
        traditional_list.append(traditional)
        variant_list.append(variant)

print_str(pre_id,pre_simplified,traditional_list,variant_list)

for line in open("通用规范汉字表(2013)全部(8105字).txt",encoding='utf-8'):
    idx = line.strip().split("\t")[0]
    print(line.strip(), idx_char_map.get(idx,"\t"), sep="\t")
