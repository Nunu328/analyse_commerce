# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/white/OneDrive/Documents/GitHub/analyse_commerce/SuperStoreOrders.csv')
print(df.head())
df.info()#sales - object
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

#chercher des values manquants
print("Missing values in each column:")
print(df.isnull().sum())

#Les 10 premiers pays utilisateurs et les 10 premiers produits

nb_country = df['country'].value_counts(sort=True)
top10_country = nb_country.head(10).reset_index()
top10_country.columns = ['Value', 'Count']
print(top10_country)


nb_sub_categorie = df['sub_category'].value_counts(sort=True)
top10_sub_cate = nb_sub_categorie.head(10)
print(top10_sub_cate)

# Année
annee = df['year'].value_counts(sort=True)
print(annee)

#segment

nb_segment = df['segment'].value_counts(sort=True)
print(nb_segment)

#Ventes et remises par catégorie de produits
df_produit = df.groupby(['year','sub_category']).agg({'sales': 'sum', 'discount': 'sum'}).reset_index()
trier_df = df_produit.sort_values(by=['year', 'sales'], ascending=[True, False]).reset_index(drop=True)
trier_df.columns = ['Annee','Produit', 'Total ventes', 'Total remises']
print(trier_df)


#graphique

data_2011 = trier_df[trier_df['Annee'] == 2011]
data_2011.info()

top5_produits2011 = data_2011.groupby('Produit')['Total ventes'].sum().nlargest(5).reset_index()

plt.figure(figsize=(12, 8))
plt.bar(top5_produits2011['Produit'], top5_produits2011['Total ventes'], color='skyblue', label='Total Ventes')
plt.xlabel('Produit')
plt.ylabel('Total Ventes')
plt.title('Total Ventes par Produit en 2011')
plt.legend()
plt.show()

#2014
data_2014 = trier_df[trier_df['Annee'] == 2014]
data_2014.info()

top5_produits2014 = data_2014.groupby('Produit')['Total ventes'].sum().nlargest(5).reset_index()

plt.figure(figsize=(12, 8))
plt.bar(top5_produits2014['Produit'], top5_produits2014['Total ventes'], color='orange', label='Total Ventes')
plt.xlabel('Produit')
plt.ylabel('Total Ventes')
plt.title('Total Ventes par Produit en 2014')
plt.legend()
plt.show()

# graphique à barres en 2013

data_2013 = trier_df[trier_df['Annee'] == 2013]

# selecter top5 produits en 2013
top5_produits2013 = data_2013.groupby('Produit').agg({'Total ventes': 'sum', 'Total remises': 'sum'}).nlargest(5, 'Total ventes').reset_index()

# créer une graphique
plt.figure(figsize=(12, 8))  # changer des tailles

# Graphique à barres montrant les ventes
plt.bar(top5_produits2013['Produit'], top5_produits2013['Total ventes'], color='skyblue', label='Total ventes', alpha=0.7)

#Graphique linéaire montrant les remises     
plt.plot(top5_produits2013['Produit'], top5_produits2013['Total remises'], color='red', marker='o', label='Total remises', linewidth=2)

# titre 
plt.xlabel('Produit')
plt.ylabel('Value')
plt.title('Top 5 Produits sur ventes en 2013')
plt.xticks(rotation=45, ha='right')  # pour montrer le nom de produit
plt.legend()
plt.tight_layout()  

plt.show()

