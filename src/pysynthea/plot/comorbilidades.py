import pandas as pd
import matplotlib
matplotlib.use("Agg")
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
    d = str(desc).lower()
    for k, kws in mapping.items():
        for kw in kws:
            if kw in d:
                return k
    return None

# Crear columna con la clasificación
df['disease'] = df['DESCRIPTION'].apply(classify)

# Eliminar filas sin enfermedad reconocida
df_clean = df.dropna(subset=['disease'])

# Contar cuántas enfermedades distintas tiene cada paciente
disease_counts = df_clean.groupby('PATIENT')['disease'].nunique()

# Contar cuántos pacientes tienen 1, 2, 3, 4 ... enfermedades
counts = disease_counts.value_counts().sort_index()
percent = counts / counts.sum() * 100

# Gráfica
plt.figure(figsize=(8, 5))
ax = counts.plot(kind='bar', color='lightcoral')
plt.ylabel("Número de pacientes")
plt.xlabel("Número de enfermedades distintas")
plt.title("Distribución de comorbilidades")

# Añadir porcentaje y número absoluto sobre cada barra
for i, (count, perc) in enumerate(zip(counts, percent)):
    ax.text(i, count + 2, f"{count} pacientes\n({perc:.1f}%)", ha='center', va='bottom')

plt.tight_layout()
plt.savefig("comorbilidades.png", dpi=300)
print("Plot guardado como comorbilidades.png")


