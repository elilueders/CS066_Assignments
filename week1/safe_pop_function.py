def safe_pop(a_list):
    if len(a_list) > 0: #if list has more than 0 items go ahead and pop the last item 
        return a_list.pop(len(a_list)-1) # to find the last index i got the length of list and then take 1 off
    return None # i'm sure there is another way to do this in which you need to change this line but it fit with the way i could think to do it