def calculatePercentage(total, value):
    # Pass and Fail rate = 100 x failed or passed / totalTests
    return round (((100 * value) / total), 2)

print(calculatePercentage(375, 5))