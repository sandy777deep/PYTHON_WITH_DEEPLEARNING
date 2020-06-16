import numpy as np

list = np.random.randint(low=1, high=20, size=20)

print(list)
print("-----------Before modification---------\n")

# Reshaping the array to 4 by 5
list = np.reshape(list, (4, 5))
print(list)

print("\n-----------After Modification----------\n")

print('Replacing Max No. by 0 \n',
    np.where(list == np.max(list, axis=1).reshape(-1,1), 0, list))
