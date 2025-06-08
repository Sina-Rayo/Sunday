import json
from Functions import *

main_node = 0
cur_node = 0
check_exist = False
dic_list = {}

func_dic = {
    'say' : say,
    'search' : search,
    'run' : run_cmd
}

def do(text):
    funcl = text.split()
    try:
        function = func_dic[funcl[0]]
        funcl.pop(0)

        function(funcl)
    except KeyError:
        say("function doesn't Exist")

def check_children(nd , word):
    global cur_node , check_exist , dic_list
    cur_node = nd

    for node in dic_list[cur_node]["children"]:
            if dic_list[node]["tag"] == word:
                cur_node = node
                check_exist = True
    # if(not check_exist):
    #     return "not in children"

def get_func(txt):
    global main_node , cur_node , check_exist , dic_list

    txtl = txt.split()
    txt = txtl.pop(0)
    
    with open('Data\Resp.json' , 'r') as jfile:
        dic_list = json.load(jfile)
        main_node = dic_list[0]
        cur_node = main_node
        # txtl = txt.split()
        # word = txtl[0]
        # txtl.pop(0)
        # txt = ' '.join(txtl)

        func = "Not in path err"
        check_children(cur_node , txt)
        while(not check_exist):
            if(dic_list[cur_node]["tag"] == "ROOT"):
                func = "Not in path err"
                break

            cur_node = dic_list[cur_node]["parent"]
            check_children(cur_node, txt)

        if(check_exist):
            func = dic_list[cur_node]["function"]
            main_node = cur_node
            check_exist = False
            dic_list[0] = cur_node
            with open('Data\Resp.json' , 'w') as jfile:
                add_func = json.dumps(dic_list, indent=4)
                jfile.write(add_func)

        txt = " ".join(txtl)
        func += " " +'"' + txt + '"'
        try:
            if dic_list[cur_node]['listen_after']:
                func += '1'
            else:
                func += '0'
        except:
            func += '0'

        dic_list = {}
        jfile.close()
    
    return func



def add_function(tag , func , add_here , listen_after):
    with open("Data\Resp.json" , 'r') as jfile:
        dic_list = json.load(jfile)
        main_node = dic_list[0]
    jfile.close()

    if(not add_here):
        main_node = 1
        dic_list[0] = 1

    ind = len(dic_list)
    add_dic = {
        "ind" : ind,
        "tag" : tag,
        "function" : func,
        "children" : [],
        "parent" : main_node
    }

    if(listen_after):
        add_dic["listen_after"] = True

    dic_list[main_node]['children'].append(ind)
    dic_list.append(add_dic)
    with open("Data\Resp.json" , 'w') as jfile:
        jdic = json.dumps(dic_list , indent=4)
        jfile.write(jdic)


