
def word_count(content_of_book):
    wc = 0
    for word in content_of_book.split():
        wc += 1
    return wc

def charater_count(content_of_book):
    charaters = {}
    workable_text = content_of_book.lower()
    for chars in workable_text:
        if chars in charaters:
            charaters[chars] += 1
        else:
            charaters[chars] = 1
    return charaters

def processed_dict_report(contents_dict):
    working_dict = contents_dict
    new_list = []
    temp_dict = {}
    for char,num in working_dict.items():
        temp_dict={"char":char, "num":num}
        new_list.append(temp_dict)
        #print(new_list)
    #print(new_list)
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(item):
    return item["num"]
