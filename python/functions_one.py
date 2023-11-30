def rep_cat(x, y):
    
    x_str = str(x) * 10
    y_str = str(y) * 5
    
    
    result = x_str + y_str
    return result


x = 12
y = 34

result = rep_cat(x, y)
print(result)