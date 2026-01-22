import pandas as pd

def run_etl():
    
    #Leer datos
    df = pd.read_csv('data/citas_clinica.csv')
    
    #Normalización de texto
    df["paciente"] = df["paciente"].str.title()
    df["especialidad"] = df["especialidad"].str.upper()
    
    #Validación de fechas
    df["fecha_cita"] = df["fecha_cita"].str.replace("/", "-", regex=False)
    df["fecha_cita"] = pd.to_datetime(df["fecha_cita"],errors="coerce")


    #Reglas del negocio
    df = df[df["estado"] == "CONFIRMADA"]
    df = df[df["costo"] > 0]
    
    #Teléfonos nulos
    df["telefono"] = df["telefono"].fillna("NO REGISTRA")
    df.to_csv('data/output.csv', index=False)


if __name__ == "__main__":
    run_etl()
