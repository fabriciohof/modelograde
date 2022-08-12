


import pandas as pd

grade = {'Segunda':['OC1','OC1','OC1','INTERVALO -','MAT','MAT','MAT','//'],
         'Terça':['MAT','MAT','//','INTERVALO -','RD1','RD1','RD1','RD1'],
         'Quarta':['ICG','ICG','ICG','INTERVALO -','//','LEI','LEI','//'],
         'Quinta':['//','CEL','CEL','INTERVALO -','RD1','//','ICG','ICG'],
         'Sexta':['//','//','//','INTERVALO','//','OC1','OC1','OC1']}

g  = pd.DataFrame(data=grade)
df = pd.DataFrame(grade, index = ["7:00-7:45","7:45-8:30","8:30-9:15","9:15-9:30","9:30-10:15","10:15-11:00","11:00-11:45","11:45-12:30"])
df

