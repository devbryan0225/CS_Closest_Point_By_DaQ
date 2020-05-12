
axis = 0

def merge(list_A, list_B):

    index_A = 0
    index_B = 0

    merged_list = []
    is_sorted = False
    
    while (is_sorted == False):

        end_of_list_A = index_A == len(list_A)
        end_of_list_B = index_B == len(list_B)

        if(end_of_list_A and end_of_list_B):
            is_sorted = True
            continue

        if( end_of_list_A ):
            merged_list.append(list_B[index_B])
            index_B += 1
            continue
        elif( end_of_list_B ):
            merged_list.append(list_A[index_A])
            index_A += 1
            continue

        if( list_A[index_A][0] < list_B[index_B][0] ):
            merged_list.append(list_A[index_A])
            index_A += 1
            
        else:
            merged_list.append(list_B[index_B])
            index_B += 1            
            
    #print('Merged into',merged_list)
    return merged_list


def divide_and_merge(unsorted_list):

    half = int(len(unsorted_list)/2)
    list_A = unsorted_list[:half]
    list_B = unsorted_list[half:]
    
    #print('Split into',list_A, list_B)

    # split if subarray contains more than 1 item
    if(len(list_A) >= 2):
        list_A = divide_and_merge(list_A)        

    if(len(list_B) >= 2):
        list_B = divide_and_merge(list_B)

    return merge(list_A, list_B)


def merge_sort(unsorted_list, axis_choice):
    if( axis_choice == 'x'):
        axis = 0
    elif( axis_choice == 'y'):
        axis = 1
    
    return divide_and_merge(unsorted_list)




