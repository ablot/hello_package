import bootcamp.main

data = [1, 2, 3, 4, 5]
results = []
for d in data:
    results.append(bootcamp.main.complex_analysis(d, 3))

# Here we should save the result to a file, but for now we will just print it
print(results)