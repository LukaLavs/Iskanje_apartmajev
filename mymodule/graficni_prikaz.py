import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Izračun povprečij za številčne stolpce    
def povprecje_stevil_glede_na_sobe(df):
    
    numeric_columns = ['Skupna cena', 'Cena na noč', 'Morje', 'Plaža', 'Center', 'Trgovina', 'Restavracija']
    df = df.groupby('Soba')[numeric_columns].mean().reset_index()
    return df



def porazdelitev_cen(df):
    
    plt.figure(figsize=(12, 8))
    df["Cena na noč"].hist(bins=20, edgecolor="black")
    plt.title("Porazdelitev cen na noč")
    plt.xlabel("Cena na noč")
    plt.ylabel("Število sob")
    plt.grid(False)
    plt.savefig('grafi_in_tabele/porazdelitev_cen.png', dpi=150)
    plt.close()
    
    

def cena_glede_na_tip_sobe(df_povprecji):

    plt.figure(figsize=(12, 8))
    sns.barplot(x='Soba', y='Cena na noč', data=df_povprecji)
    plt.title('Povprečna cena na noč glede na tip sobe')
    plt.ylabel('Povprečna cena na noč')
    plt.xlabel('Tip sobe')
    plt.xticks(rotation=90, fontsize=10)
    plt.savefig('grafi_in_tabele/cena_glede_na_tip_sobe.png', dpi=150)
    plt.close()


def razdalje_glede_na_tip_sobe(df_povprecji):
    
    plt.figure(figsize=(12, 8))
    melted_avg_prices = df_povprecji.melt(id_vars='Soba', value_vars=['Morje', 'Plaža', 'Center', 'Trgovina', 'Restavracija'], var_name='Lokacija', value_name='Razdalja')
    sns.barplot(x='Lokacija', y='Razdalja', hue='Soba', data=melted_avg_prices)
    plt.title('Povprečne razdalje glede na tip sobe')
    plt.ylabel('Povprečna razdalja (v metrih)')
    plt.xlabel('Lokacija')
    plt.legend(title='Tip sobe')
    plt.savefig('grafi_in_tabele/razdalje_glede_na_tip_sobe.png', dpi=150)
    plt.close()
    
    
    
def matrika_korelacij(df):
    
    stolpci_stevil = ['Skupna cena', 'Cena na noč', 'Morje', 'Plaža', 'Center', 'Trgovina', 'Restavracija']
    matrika = df[stolpci_stevil].corr()
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(matrika, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Korelacija med cenami in razdaljami')
    plt.savefig('grafi_in_tabele/matrika_korelacij.png', dpi=150)
    plt.close()
    
    
    
def izrisi_grafe(df):
    
    df.replace("Ni podatka", pd.NA, inplace=True)
    df = df.dropna()
    
    a = povprecje_stevil_glede_na_sobe(df)
    porazdelitev_cen(df)
    cena_glede_na_tip_sobe(a)
    razdalje_glede_na_tip_sobe(a)
    matrika_korelacij(df)
    