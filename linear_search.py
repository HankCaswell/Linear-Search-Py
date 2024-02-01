def linear_search(value_to_find, array_to_search_through):
    # your code here
    for index, letter in enumerate(array_to_search_through):
        if letter == value_to_find:
            return index 
     
   

def linear_search_global(value_to_find, array_to_search_through):
    answer = []
    for index, letter in enumerate(array_to_search_through):
        if letter == value_to_find:
            answer.append(index)
    return answer 
    
    
    

