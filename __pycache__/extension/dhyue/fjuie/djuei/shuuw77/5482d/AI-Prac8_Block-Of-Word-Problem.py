ini_state = ['1', '2', '3', '5', '6', '0', '8', '9', '7']
go_state  = ['1', '2', '3', '7', '6', '0', '9', '8', '5']

# Initialize lists with the same length or copy them directly
num1 = list(ini_state)
num2 = list(go_state)
num3 = [''] * len(ini_state)

for i in range(len(ini_state)):
    if num1[i] == num2[i]:
        continue
    else:
        num3[i] = num1[i]
        num1[i] = num2[i]
        num2[i] = num3[i]

# Example output to check results
print("Modified num1:", num1)
print("Modified num2:", num2)
