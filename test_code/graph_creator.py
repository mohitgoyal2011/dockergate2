import sys,os
import subprocess
import logging
import json
import graphviz as gv

def dfs_search(binary, call_graph, binary_set, executable):
    print('Adding ' + binary)
    binary_set.add(binary)
    if executable:
        call_graph.node(binary, binary, color = 'blue')
    else:
        call_graph.node(binary, binary, color = 'white')
    complete_path = os.path.realpath(binary)
    try:
        ldd_output = subprocess.check_output('ldd ' + complete_path, shell=True, universal_newlines=True).split('\n')
    except Exception as e:
        print('This sounds statically linked ' + str(e) )
        return   
    linked_libraries_list = []
    for lib in ldd_output:
        try:
            lib = lib.split("=>")[1].split('(')[0].strip()
        except:
            lib =  lib.split(" ")[0].strip()
        if os.path.islink(lib):
            realpath = os.readlink(lib)
            lib = os.path.dirname(lib) + '/' + realpath
            if not os.path.exists(lib):
                lib = '/' + realpath
        if not os.path.exists(lib) or not os.path.isfile(lib):
            continue
        if lib not in binary_set:
            dfs_search(lib, call_graph, binary_set, False)
        call_graph.edge(binary, lib)
    return

rootDir = '/'
call_graph = gv.Digraph(format='dot')
binary_set = set()
for dirName, subdirList, filelist in os.walk(rootDir):
    for fname in filelist:
        filename = dirName + '/' + fname
        if os.path.isfile(filename) and os.access(filename, os.X_OK):
            if filename not in binary_set:
                dfs_search(filename, call_graph, binary_set, True)
f= open('/test_code/test.dot','w')
f.write(call_graph.source)
