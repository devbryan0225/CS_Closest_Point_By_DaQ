import importlib

sort = importlib.import_module('Merge_Sort_Coordinates')



def euclidean_distance(point_1,point_2):
    return ((point_2[0]-point_1[0])**2 + (point_2[1]-point_1[1])**2)**0.5

def brute_force_distance(subarray_list):
    shorter_distance = euclidean_distance(subarray_list[0], subarray_list[1])
    shorter_points = [subarray_list[0], subarray_list[1]]
    
    for i in range(len(subarray_list)-1):
        for j in range(i+1,len(subarray_list)):
                                    
            distance = euclidean_distance(subarray_list[i], subarray_list[j])            
            
            if(distance < shorter_distance):
                shorter_distance = distance
                shorter_points = [subarray_list[i], subarray_list[j]]

    return shorter_distance, shorter_points

def mid_region_distance(subarray_list, cur_shortest):
    shorter_distance = euclidean_distance(subarray_list[0], subarray_list[1])
    shorter_points = [subarray_list[0], subarray_list[1]]

    for i in range(len(subarray_list)-1):
        for j in range(i+1,len(subarray_list)):

            if(abs(subarray_list[i][0] - subarray_list[j][0]) > cur_shortest/(2**0.5)):
                continue
            distance = euclidean_distance(subarray_list[i], subarray_list[j])            
            
            if(distance < shorter_distance):
                shorter_distance = distance
                shorter_points = [subarray_list[i], subarray_list[j]]

    return shorter_distance, shorter_points
    

def divide_and_conquer(coordinates_array):
    half = int(len(coordinates_array)/2)
    left = coordinates_array[:half]
    right = coordinates_array[half:]
    distance_and_points = []
    
    if(len(left) > 4):        
        distance_and_points.append( divide_and_conquer(left) )
    else:        
        distance_and_points.append( brute_force_distance(left) )

    if(len(right) > 4):        
        distance_and_points.append( divide_and_conquer(right) )
    else:        
        distance_and_points.append( brute_force_distance(right) )

    # get min. of left, right and middle
    temp_min = distance_and_points[0]
    for item in distance_and_points:
        if(item[0] < temp_min[0]):
            temp_min = item

    # use shortest distance to find points between left and right sections
    # 1. get subarray between -d and +d
    midpoint = (right[0][0] - left[len(left)-1][0])/2
    mid_array = []
    for coordinates in coordinates_array:
        if( (coordinates[0] > (midpoint - temp_min[0])) and (coordinates[0] > (midpoint + temp_min[0])) ):
             mid_array.append(coordinates)
    mid_array = sort.merge_sort(mid_array,'y')    
    
    # 2. ignore points where x dist > x/sqrt 2    
    mid_shortest = mid_region_distance(mid_array,temp_min[0])
             
    # 3. compare current min. with middle
    if(mid_shortest[0] < temp_min[0]):
        temp_min = mid_shortest
    
    # return distance and coordinates
    return temp_min


points = [(350,150),(500,250),(150,150),(50,400),(200,100)]

sorted_points = sort.merge_sort(points,'x')
print(sorted_points)

result = divide_and_conquer(sorted_points)
print(result)
    
