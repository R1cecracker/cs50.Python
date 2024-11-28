# splits up each word in input
response = input().strip().split()

# joins each word back in the input with "..." in between each word
result = "...".join(response)

# prints new output
print(result)