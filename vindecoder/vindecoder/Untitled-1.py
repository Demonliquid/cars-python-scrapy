# %%
import pandas as pd

# %%
diccionario = pd.read_csv(r"F:\Trabajo\Promotive\Parametros_Tablas_LimpezaBases.csv", sep=";")


# %%
diccionario
# %% MOTOR SEGUN CILINDRADA DICCIONARIO
pais = pd.merge(pais, diccionario, left_on="CILINDRADA", right_on="CILINDRADA CC", how="left")

condicion = pais["MOTOR"].isna()
condicion2 = pais["CILINDRADA LTS"].notna()

pais.loc[condicion & condicion2, "MOTOR"] = pais.loc[condicion & condicion2, "CILINDRADA CC"]


# %% WMI - VIN
listamarcasvin = list(dict(diccionario["MARCA VIN"].value_counts()))
pais["WMI"] = None

for marca in listamarcasvin:
    condicion = pais["MARCA"] == f"{marca}"


    condiciondiccionario = diccionario["MARCA VIN"] == f"{marca}"
    cantidaddeletras = diccionario.loc[condiciondiccionario, "PRIMEROS DIGITOS VIN"][0]
    cantidaddeletras = cantidaddeletras - 1

    pais.loc[condicion, "WMI"] = pais.loc[condicion, "NUMERO DE CHASIS/VIN"].str[0:f"{cantidaddeletras}"]
    condicion = None
    condiciondiccionario = None
    cantidaddeletras = None





# %%


# %%


# %%

pais["NUMERO DE CHASIS/VIN"].str[0:]


