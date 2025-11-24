import pandas as pd
import matplotlib
matplotlib.use("Agg")  # evita usar Tkinter
import matplotlib.pyplot as plt

# Cargar archivo
df = pd.read_csv('C:/Users/Lenovo/Desktop/4 GIB/PRACTICAS HOSPI/GIT/semana2/pysynthea/src/pysynthea/plot/conditions.csv')

# Diccionario de mapeo para clasificar enfermedades
mapping = {
    'diabetes': ['diabetes'],
    'pancreatitis aguda': ['acute pancreatitis'],
    'pancreatitis crónica': ['chronic pancreatitis'],
    'MCN': ['mucinous cystic neoplasm'],
    'IPMN': ['intraductal papillary mucinous'],
    'PanIN': ['pancreatic intraepithelial neoplasia']
}

# Función para clasificar descripciones
def classify(desc):
    d = desc.lower()
    for k, kws in mapping.items():
        for kw in kws:
            if kw in d:
                return k
    return None

# Crear columna con la clasificación
df['disease'] = df['DESCRIPTION'].apply(classify)

# Calcular porcentajes
counts = df['disease'].value_counts(dropna=True)
percent = counts / counts.sum() * 100

# Gráfica
plt.figure(figsize=(10, 5))
ax = percent.plot(kind='bar')
plt.ylabel("Porcentaje (%)")
plt.title("Porcentaje por enfermedad")
plt.xticks(rotation=45, ha='right')

for i, (count, perc) in enumerate(zip(counts, percent)):
    ax.text(i, perc + 0.5, f"{perc:.2f}%\n({count} personas)", ha='center', va='bottom')


plt.tight_layout()

# Guardar la imagen (no usa Tkinter)
plt.savefig("porcentajes_enfermedades_numero.png", dpi=300)
print("Plot guardado como enfermedades.png")




