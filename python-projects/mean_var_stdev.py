import numpy as np
from statistics import variance, stdev

def calculate(list):
    overall_mean = np.mean(list)
    overall_var = np.var(list)
    overall_st_dev = np.std(list)
    overall_maximum_value = np.max(list)
    overall_minimum_value = np.min(list)
    overall_sum_of_numbers = np.sum(list)
    
    row_mean =np.mean(list, axis = 1).tolist()
    row_var = [variance(row) for row in list]
    row_st_dev = [stdev(row) for row in list]
    row_max = np.max(list, axis = 1).tolist()
    row_min = np.min(list, axis = 1).tolist()
    row_sum = np.sum(list, axis = 1).tolist()

    col_mean = np.mean(list, axis = 0).tolist()
    col_var = [variance(list[:, i]) for i in range(list.shape[1])]
    col_st_dev = [stdev(list[:, i]) for i in range(list.shape[1])]
    col_max = np.max(list, axis = 0).tolist()
    col_min = np.min(list, axis = 0).tolist()
    col_sum = np.sum(list, axis = 0).tolist()

    calculations = {'mean' : [row_mean, col_mean, overall_mean],'variance' : [row_var, col_var, overall_var], 'standard deviation' : [row_st_dev, col_st_dev, overall_st_dev], 'max' : [row_max, col_max, overall_maximum_value], 'min' : [row_min, col_min, overall_minimum_value], 'sum' : [row_sum, col_sum, overall_sum_of_numbers]}
    
    return calculations

numbers = np.array([0,1,2,3,4,5,6,7,8]).reshape(3,3)
print(calculate(numbers))