import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('rezultat.csv')

plt.figure(figsize=(10, 6))
plt.bar(data['time_interval_formatted'], data['interaction_count'], color='skyblue')
plt.xlabel('Vremenski interval')
plt.ylabel('Broj interakcija')
plt.title('Broj interakcija u vremenskim intervalima od 15 sekundi')
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()

plt.savefig('graf-prikaz.png', dpi=1000)

plt.show()
