def diff_sensor (sensor_a, sensor_b, size):

    diff = 0

    for i in range(size):

        diff += abs(sensor_a[i] - sensor_b[i])
    
    return diff

def diff_sensor_dispatcher (sensor_a, sensor_b, size):

    if size == 0: return 0
    
    last_diff = abs(sensor_a[size - 1] - sensor_b[size - 1])

    diff = last_diff + diff_sensor_dispatcher (sensor_a, sensor_b, size - 1)

    return diff

# Test Zone

sa = [15, -4, 56, 10, -23]
sb = [14, -9, 56, 14, -23]
s = 5
print("The difference in sensor reading is: " + str(diff_sensor_dispatcher(sa, sb, s)))