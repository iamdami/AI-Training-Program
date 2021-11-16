result = [f"{inner}X{outer}={inner*outer}" for outer in range(2, 10) for inner in range(2, 10)]
print(result)