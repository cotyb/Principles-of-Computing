"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    result = []
    result_final = []
    for dummy_count in range(len(line)):
        result.append(0)
        result_final.append(0)
    index = 0
    for dummy_ele in line:
        if dummy_ele != 0:
            result[index] = dummy_ele
            index += 1
    
    for dummy_count in range(len(result)-1):
        if result[dummy_count] == result[dummy_count+1]:
            result[dummy_count] = 2 * result[dummy_count]
            result[dummy_count+1] = 0
    index = 0        
    for dummy_ele in result:
        if dummy_ele != 0:
            result_final[index] = dummy_ele
            index += 1
            
    return result_final
