import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv('japan_population.csv')
#print(df)

df['target'] = None

def state_code(a):
    a = a*1000
    b = str(a).zfill(5) #zfill is used for dataframe with 0 as the head
    #state = (df['コード'] == b)
    #print(df[state])
    return b

def disp_only_state():
    for i in range (1,47):
        j = state_code(i)
        state = (df['コード'] == j)
        df.loc[state, 'target'] = 1
        #print(j)
        #print(df[state])

disp_only_state()
#print(df.head())
allstate = df.dropna() #setting up new dataframe with only state
allstate['総数'] = allstate['総数'].str.replace(',', '').astype(float)
mean = allstate['総数'].mean()
median = allstate['総数'].median()
max = allstate['総数'].max()
min = allstate['総数'].min()
var = allstate['総数'].var()
std = allstate['総数'].std()
mode = allstate['総数'].mode()

print("Average population is: ", end='')
print(mean)
print("Median population is: ", end='')
print(median)
print("Max population is: ", end='')
print(int(max))
print("Min population is: ", end='')
print(int(min))
print("Variance of population is: ", end='')
print(var)
print("Standard variation of population is: ", end='')
print(std)
print("Mode population is: ")
print(mode)


