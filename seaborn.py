import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
birds = pd.read_csv('c:/data_files/birds.csv')
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]
#filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
sns.kdeplot(filteredBirds['MaxBodyMass'],bw_adjust=.2)
plt.show()
