import matplotlib.pyplot as plt
import pandas as pd
d = pd.read_csv('dis.csv').dropna(how='all', axis=1).dropna(how='all', axis=0)
plt.figure(figsize=(9,5),)
plt.plot(d.Year, d['Diesel / litre'], linewidth=2, marker='o', label='Diesel')
plt.plot(d.Year, d['Petrol / litre'], linewidth=2, marker='s', label='Petrol')
plt.title('Petrol Vs Diesel Price in India (2003 - 2025)', pad=20, fontdict={'fontweight': 'bold'})
plt.xlabel('Years (2003 to 2025)', labelpad=15, fontdict={'fontsize':10, 'fontweight':'bold'})
plt.ylabel('Price/ litre (in Rs.)', fontdict={'fontsize':10, 'fontweight':'bold'})
plt.annotate(
    '2020: Diesel (₹79.88) > Petrol (₹79.76)',
    xy=(2020, 79.88),
    xytext=(2007, 80),
    arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
    fontsize=10,
    fontweight='bold',
    bbox=dict(boxstyle='round,pad=0.4', facecolor='#ababab', edgecolor='gray')
)
plt.subplots_adjust(left=0.10, right=0.96, top=0.88, bottom=0.18)
plt.figtext(
    0.0,
    0.02,
    'Prices are for Delhi IOCL outlets | Source: PPAC / Ministry of Petroleum & Natural Gas',
    ha='left',
    fontsize=8,
    style='italic',
    color='#555555',
)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.legend()
plt.savefig('fuelcomp.png', dpi=300)
print(d)
plt.show()
