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
## 🧪 Generación de Datos

El dataset utilizado en este proyecto fue generado mediante un **script en Python** a partir de un prompt de diseño que define reglas realistas de negocio para datos de Recursos Humanos.

### Prompt utilizado

Se solicitó a ChatGPT generar un script que cumpliera con:

- 8.950 registros
- Distribución de género:
  - 46% Female
  - 54% Male
- Ubicación por estados y ciudades predefinidas
- Fechas de contratación (2015–2024) con probabilidades personalizadas
- Departamentos con pesos específicos
- Cargos dependientes del departamento
- Nivel educacional según el cargo
- Evaluación de desempeño con probabilidades
- Horas extra (30% Yes, 70% No)
- Salarios por rango según cargo y departamento
- Fecha de nacimiento coherente con edad y cargo
- 11.2% de empleados con fecha de término (>= 6 meses después de contratación)
- Cálculo de salario ajustado según:
  - género
  - nivel educacional
  - edad

---

### Script de generación

El archivo generate_hr_dataset.py implementa toda esta lógica utilizando:

- `pandas`
- `numpy`
- `faker`
- distribuciones probabilísticas
- reglas condicionales por cargo

### Variables principales generadas

- employee_id  
- first_name / last_name  
- gender  
- state / city  
- hiredate  
- department  
- job_title  
- education_level  
- performance_rating  
- overtime  
- birthdate  
- termdate  
- salary (ajustado dinámicamente)

---

### Ejecución

Para generar el archivo CSV:

```bash
python scripts/generate_hr_dataset.py

## Créditos

Este proyecto fue inspirado en el tutorial:

**A Complete HR Tableau Practice Project End-to-End**  
Video de *Data With Baraa*  
👉 https://www.youtube.com/watch?v=UcGF09Awm4Y

Gracias por la referencia y la explicación que sirvieron como base para la estructura y los análisis.



