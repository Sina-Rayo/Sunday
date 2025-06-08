import json

def make_sentense(txt , v_sen):
    txtl = txt.split()

    with open("Data\Trie.json" , 'r') as jfile:
        dic = json.load(jfile)
        cur_node = 0

        for word in txtl:
            exist = False
            for node in dic[cur_node]["children"]:
                if dic[node]["sentence"] == word:
                    cur_node = node
                    exist = True
            if exist == False:
                siz = len(dic)
                dic[cur_node]["children"].append(siz)
                cur_node = siz
                add_dic = {
                    "ind" : siz,
                    "sentence" : word,
                    "children" : [],
                    "tag" : None
                }
                if(v_sen):
                    add_dic["v_sen"] = True

                dic.append(add_dic)
    jfile.close()
    with open("Data\Trie.json" , 'w') as jfile:
        jdic = json.dumps(dic , indent=4)
        jfile.write(jdic)
    jfile.close()


def realize(txt):
    txt = txt.lower()
    with open("Data\Trie.json" , 'r') as jfile:
        dic = json.load(jfile)
        cur_node = 0
        txtl = txt.split()
        t_var = txt.split()

        for word in txtl:
            exist = False
            for node in dic[cur_node]["children"]:
                if dic[node]["sentence"] == word:
                    cur_node = node
                    exist = True
            if exist == False:
                try:
                    if(dic[cur_node]["v_sen"]):
                        tag = dic[cur_node]["tag"]
                        txt = " ".join(t_var)
                        tag += " " + txt
                        return tag
                except:
                    pass
                return "Not Exist Err"
            t_var.pop(0)
        tag = dic[cur_node]["tag"]
        return tag
    jfile.close()
     
       
def add_tag(txt , tag):
    txt = txt.lower()
    with open("Data\Trie.json" , 'r') as jfile:
        dic = json.load(jfile)
        cur_node = 0
        txtl = txt.split()

        for word in txtl:
            for node in dic[cur_node]["children"]:
                if dic[node]["sentence"] == word:
                    cur_node = node
            
        dic[cur_node]["tag"] = tag
    jfile.close()
    
    with open("Data\Trie.json" , 'w') as jfile:
        jdic = json.dumps(dic , indent=4)
        jfile.write(jdic)
    jfile.close()
