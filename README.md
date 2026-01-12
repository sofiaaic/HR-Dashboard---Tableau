# HR Dashboard (Recursos Humanos) 📊

Dashboard interactivo para análisis de Recursos Humanos con:
- **Slide 1:** Vista ejecutiva (Overview, Demographics, Departments, Location, Income)
- **Slide 2:** Vista de detalle (Employee List)

Incluye un **script en Python** para generar un dataset sintético realista de **8.950 empleados**.

---

## 🎯 Objetivo
Permitir a un/a HR Manager:
- Analizar métricas globales de personal  
- Entender la composición demográfica  
- Evaluar patrones salariales  
- Explorar registros individuales con filtros dinámicos  

---

## 📊 Slides del Dashboard

## 🟢 Slide 1 – Overview

<img width="2032" alt="overview" src="https://github.com/user-attachments/assets/03dcccc8-4a9a-4b14-aa22-58a9afa3f44a" />

Este slide entrega una **visión estratégica** del estado de la organización e integra:

### 🔹 Overview
- Total de empleados:
  - Contratados
  - Activos
  - Desvinculados
- Evolución anual de:
  - Contrataciones (Hired)
  - Desvinculaciones (Terminated)

### 🔹 Demographics
- Distribución por **género**
- Cruce entre:
  - Grupos etarios
  - Nivel educacional
- Relación entre:
  - Educación
  - Performance rating

### 🔹 Departments
- Ranking de empleados por:
  - Operations
  - Sales
  - Customer Service
  - IT
  - Marketing
  - Finance
  - HR
- Comparación entre:
  - Hired vs Terminated

### 🔹 Location
- Mapa interactivo por estado:
  - New York (HQ)
  - Michigan
  - Illinois
  - Ohio
  - Pennsylvania
  - West Virginia
  - North Carolina
- Comparación:
  - Headquarters vs Branches

### 🔹 Income
- Comparación salarial por:
  - Nivel educacional
  - Género
- Relación:
  - Edad vs salario
  - Cargo

---

## 🔵 Slide 2 – Details (Employee List)

<img width="2048" alt="details" src="https://github.com/user-attachments/assets/9b550538-247c-4677-96d1-02f3f197f3f6" />

Este slide permite un **análisis a nivel empleado**.

### Información mostrada
- Employee ID  
- Nombre completo  
- Género  
- Edad  
- Nivel educacional  
- Departamento  
- Cargo  
- Ciudad y estado  
- Salario  
- Estado laboral  
- Antigüedad  

### Filtros disponibles
- ID
- Nombre
- Género
- Grupo etario
- Nivel educacional
- Departamento
- Cargo
- Ubicación (estado / ciudad)
- Rango salarial
- Estado laboral
- Año de contratación
- Año de desvinculación
- Antigüedad

Permite realizar **búsquedas, segmentaciones y análisis individuales**.

---

## 🧪 Generación de datos
Script en Python que genera un dataset sintético con:
- Distribuciones realistas  
- Reglas de negocio  
- Consistencia temporal  

```bash
python scripts/generate_hr_dataset.py --output data/hr_dataset.csv

