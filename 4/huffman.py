import copy
import sys

def make_leaf(symbol, weight):
    return (symbol, weight)

def is_leaf(x):
    return isinstance(x, tuple) and \
            len(x) == 2 and \
            isinstance(x[0], str) and \
            isinstance(x[1], int)

def get_leaf_symbol(leaf):
    return leaf[0]

def get_leaf_freq(leaf):
    return leaf[1]

def get_left_branch(huff_tree):
    return huff_tree[0]

def get_right_branch(huff_tree):
    return huff_tree[1]

def get_symbols(huff_tree):
    if is_leaf(huff_tree):
        return [get_leaf_symbol(huff_tree)]
    else:
        return huff_tree[2]

def get_freq(huff_tree):
    if is_leaf(huff_tree):
        return get_leaf_freq(huff_tree)
    else:
        return huff_tree[3]

def make_huffman_tree(left_branch, right_branch):
    return [left_branch,
            right_branch,
            get_symbols(left_branch) + get_symbols(right_branch),
            get_freq(left_branch) + get_freq(right_branch)]

## leaves
def make_assigned_huffman_tree():
    E_1 = make_leaf('E', 1)
    F_1 = make_leaf('F', 1)

    G_1 = make_leaf('G', 1)
    H_1 = make_leaf('H', 1)

    C_1 = make_leaf('C', 1)
    D_1 = make_leaf('D', 1)

    B_3 = make_leaf('B', 3)
    A_8 = make_leaf('A', 8)

    EF_2 = make_huffman_tree(E_1, F_1)
    GH_2 = make_huffman_tree(G_1, make_leaf('H', 1))
    EFGH_4 = make_huffman_tree(EF_2, GH_2)

    CD_2 = make_huffman_tree(C_1, D_1)
    BCD_5 = make_huffman_tree(B_3, CD_2)

    BCDEFGH_9 = make_huffman_tree(BCD_5, EFGH_4)

    ABCDEFGH_17 = make_huffman_tree(A_8, BCDEFGH_9)

    return ABCDEFGH_17

def get_code(char, huffman_tree):
    code = []
    if(is_leaf(huffman_tree[0])):
        if(get_leaf_symbol(huffman_tree[0]) == char):
            return [0]
    else: 
        temp = get_code(char, huffman_tree[0])
        if(temp != None):
            code.extend(temp)
            code.append(0)
            return code

    if(is_leaf(huffman_tree[1])):
        if(get_leaf_symbol(huffman_tree[1]) == char):
            return [1]

    else:
        temp = get_code(char, huffman_tree[1])
        if(temp != None):
            code.extend(temp)
            code.append(1)     
            return code  

def huffman_encode(symbols, huffman_tree):
    Dict = set(get_symbols(huffman_tree))
    if(Dict.intersection(symbols) == set(symbols)):
        code = [];
        for char in symbols:
            code.extend(reversed(get_code(char, huffman_tree)))
        return code
    else:
        return "Symbols not found in Huffman Tree"

def huffman_decode(inputcode, huffman_tree):
    message = []
    code = copy.deepcopy(inputcode)
    tree = copy.deepcopy(huffman_tree)
    while(len(code) > 0):
        var = code.pop(0)
        if(is_leaf(tree[int(var)])):
            message.extend(get_leaf_symbol(tree[int(var)]))
            tree = copy.deepcopy(huffman_tree)
        else:
            tree = tree[int(var)]
    return message





            
            
            

