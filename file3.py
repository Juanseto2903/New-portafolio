import pandas as pd
import random

random.seed(40)

dic = {

    'Name': ['Juan', 'Maria', 'xd'],
    'Age': [random.randint(18,30) for _ in range(3)]
}

df = pd.DataFrame(dic)
print(df)

# Random con seed.