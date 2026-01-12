"""
HR Synthetic Dataset Generator
--------------------------------
Genera un dataset sintético de Recursos Humanos (8.950 registros)
"""

import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# =========================
# CONFIGURACIÓN
# =========================

fake = Faker('en_US')
Faker.seed(42)
np.random.seed(42)
random.seed(42)

num_records = 8950

# =========================
# ESTADOS Y CIUDADES
# =========================

states_cities = {
    'New York': ['New York City', 'Buffalo', 'Rochester'],
    'Virginia': ['Virginia Beach', 'Norfolk', 'Richmond'],
    'Florida': ['Miami', 'Orlando', 'Tampa'],
    'Illinois': ['Chicago', 'Aurora', 'Naperville'],
    'Pennsylvania': ['Philadelphia', 'Pittsburgh', 'Allentown'],
    'Ohio': ['Columbus', 'Cleveland', 'Cincinnati'],
    'North Carolina': ['Charlotte', 'Raleigh', 'Greensboro'],
    'Michigan': ['Detroit', 'Grand Rapids', 'Warren']
}

states = list(states_cities.keys())
state_prob = [0.7, 0.02, 0.01, 0.03, 0.05, 0.03, 0.05, 0.11]

# =========================
# DEPARTAMENTOS Y CARGOS
# =========================

departments = ['HR', 'IT', 'Sales', 'Marketing', 'Finance', 'Operations', 'Customer Service']
departments_prob = [0.02, 0.15, 0.21, 0.08, 0.05, 0.30, 0.19]

jobtitles = {
    'HR': ['HR Manager', 'HR Coordinator', 'Recruiter', 'HR Assistant'],
    'IT': ['IT Manager', 'Software Developer', 'System Administrator', 'IT Support Specialist'],
    'Sales': ['Sales Manager', 'Sales Consultant', 'Sales Specialist', 'Sales Representative'],
    'Marketing': ['Marketing Manager', 'SEO Specialist', 'Content Creator', 'Marketing Coordinator'],
    'Finance': ['Finance Manager', 'Accountant', 'Financial Analyst', 'Accounts Payable Specialist'],
    'Operations': ['Operations Manager', 'Operations Analyst', 'Logistics Coordinator', 'Inventory Specialist'],
    'Customer Service': ['Customer Service Manager', 'Customer Service Representative', 'Support Specialist', 'Help Desk Technician']
}

jobtitles_prob = {
    'HR': [0.03, 0.3, 0.47, 0.2],
    'IT': [0.02, 0.47, 0.2, 0.31],
    'Sales': [0.03, 0.25, 0.32, 0.4],
    'Marketing': [0.04, 0.25, 0.41, 0.3],
    'Finance': [0.03, 0.37, 0.4, 0.2],
    'Operations': [0.02, 0.2, 0.4, 0.38],
    'Customer Service': [0.04, 0.3, 0.38, 0.28]
}

# =========================
# EDUCACIÓN
# =========================

education_mapping = {
    'HR Manager': ["Master", "PhD"],
    'HR Coordinator': ["Bachelor", "Master"],
    'Recruiter': ["High School", "Bachelor"],
    'HR Assistant': ["High School", "Bachelor"],
    'IT Manager': ["PhD", "Master"],
    'Software Developer': ["Bachelor", "Master"],
    'System Administrator': ["Bachelor", "Master"],
    'IT Support Specialist': ["High School", "Bachelor"],
    'Sales Manager': ["Master","PhD"],
    'Sales Consultant': ["Bachelor", "Master", "PhD"],
    'Sales Specialist': ["Bachelor", "Master", "PhD"],
    'Sales Representative': ["Bachelor"],
    'Marketing Manager': ["Bachelor", "Master","PhD"],
    'SEO Specialist': ["High School", "Bachelor"],
    'Content Creator': ["High School", "Bachelor"],
    'Marketing Coordinator': ["Bachelor"],
    'Finance Manager': ["Master", "PhD"],
    'Accountant': ["Bachelor"],
    'Financial Analyst': ["Bachelor", "Master", "PhD"],
    'Accounts Payable Specialist': ["Bachelor"],
    'Operations Manager': ["Bachelor", "Master"],
    'Operations Analyst': ["Bachelor", "Master"],
    'Logistics Coordinator': ["Bachelor"],
    'Inventory Specialist': ["High School", "Bachelor"],
    'Customer Service Manager': ["Bachelor", "Master", "PhD"],
    'Customer Service Representative': ["High School", "Bachelor"],
    'Support Specialist': ["High School", "Bachelor"],
    'Help Desk Technician': ["High School", "Bachelor"]
}

# =========================
# FECHA DE CONTRATACIÓN
# =========================

year_weights = {
    2015: 5, 2016: 8, 2017: 17, 2018: 9, 2019: 10,
    2020: 11, 2021: 5, 2022: 12, 2023: 14, 2024: 9
}

def generate_custom_date(year_weights):
    year = random.choices(list(year_weights.keys()),
                           weights=list(year_weights.values()))[0]
    return fake.date_time_between(
        start_date=datetime(year, 1, 1),
        end_date=datetime(year, 12, 31)
    )

# =========================
# SALARIO BASE
# =========================

def generate_salary(department, job_title):
    salary_dict = {
        'HR': {'HR Manager': np.random.randint(60000, 90000),
               'HR Coordinator': np.random.randint(50000, 60000),
               'Recruiter': np.random.randint(50000, 70000),
               'HR Assistant': np.random.randint(50000, 60000)},
        'IT': {'IT Manager': np.random.randint(80000, 120000),
               'Software Developer': np.random.randint(70000, 95000),
               'System Administrator': np.random.randint(60000, 90000),
               'IT Support Specialist': np.random.randint(50000, 60000)},
        'Sales': {'Sales Manager': np.random.randint(70000, 110000),
                  'Sales Consultant': np.random.randint(60000, 90000),
                  'Sales Specialist': np.random.randint(50000, 80000),
                  'Sales Representative': np.random.randint(50000, 70000)},
        'Marketing': {'Marketing Manager': np.random.randint(70000, 100000),
                      'SEO Specialist': np.random.randint(50000, 80000),
                      'Content Creator': np.random.randint(50000, 60000),
                      'Marketing Coordinator': np.random.randint(50000, 70000)},
        'Finance': {'Finance Manager': np.random.randint(80000, 120000),
                    'Accountant': np.random.randint(50000, 80000),
                    'Financial Analyst': np.random.randint(60000, 90000),
                    'Accounts Payable Specialist': np.random.randint(50000, 60000)},
        'Operations': {'Operations Manager': np.random.randint(70000, 100000),
                       'Operations Analyst': np.random.randint(50000, 80000),
                       'Logistics Coordinator': np.random.randint(50000, 60000),
                       'Inventory Specialist': np.random.randint(50000, 60000)},
        'Customer Service': {'Customer Service Manager': np.random.randint(60000, 90000),
                             'Customer Service Representative': np.random.randint(50000, 60000),
                             'Support Specialist': np.random.randint(50000, 60000),
                             'Help Desk Technician': np.random.randint(50000, 80000)}
    }
    return salary_dict[department][job_title]

# =========================
# GENERACIÓN DATASET
# =========================

data = []

for _ in range(num_records):

    employee_id = f"00-{random.randint(10000000, 99999999)}"
    first_name = fake.first_name()
    last_name = fake.last_name()
    gender = np.random.choice(['Female', 'Male'], p=[0.46, 0.54])

    state = np.random.choice(states, p=state_prob)
    city = np.random.choice(states_cities[state])

    hiredate = generate_custom_date(year_weights)

    department = np.random.choice(departments, p=departments_prob)
    job_title = np.random.choice(jobtitles[department], p=jobtitles_prob[department])
    education_level = np.random.choice(education_mapping[job_title])

    performance_rating = np.random.choice(
        ['Excellent', 'Good', 'Satisfactory', 'Needs Improvement'],
        p=[0.12, 0.5, 0.3, 0.08]
    )

    overtime = np.random.choice(['Yes', 'No'], p=[0.3, 0.7])
    salary = generate_salary(department, job_title)

    data.append([
        employee_id, first_name, last_name, gender,
        state, city, hiredate, department,
        job_title, education_level, salary,
        performance_rating, overtime
    ])

columns = [
    'employee_id','first_name','last_name','gender',
    'state','city','hiredate','department',
    'job_title','education_level','salary',
    'performance_rating','overtime'
]

df = pd.DataFrame(data, columns=columns)

# =========================
# BIRTHDATE
# =========================

def generate_birthdate(row):
    if 'Manager' in row['job_title']:
        age = np.random.randint(30, 65)
    elif row['education_level'] == 'PhD':
        age = np.random.randint(27, 65)
    else:
        age = np.random.randint(20, 65)

    return fake.date_of_birth(minimum_age=age, maximum_age=age)

df['birthdate'] = df.apply(generate_birthdate, axis=1)

# =========================
# TERMINACIONES
# =========================

termination_percentage = 0.112
total_terminated = int(num_records * termination_percentage)

terminated_indices = df.index[:total_terminated]
for i in terminated_indices:
    df.at[i, 'termdate'] = df.at[i, 'hiredate'] + timedelta(days=random.randint(180, 900))

df['termdate'] = df['termdate'].where(df['termdate'].notnull(), None)

# =========================
# SALARIO AJUSTADO
# =========================

education_multiplier = {
    'High School': {'Male': 1.03, 'Female': 1.0},
    "Bachelor": {'Male': 1.115, 'Female': 1.0},
    "Master": {'Male': 1.0, 'Female': 1.07},
    'PhD': {'Male': 1.0, 'Female': 1.17}
}

def calculate_age(birthdate):
    today = pd.Timestamp('today')
    return today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )

def calculate_adjusted_salary(row):
    base = row['salary']
    age = calculate_age(row['birthdate'])
    mult = education_multiplier[row['education_level']][row['gender']]
    adj = base * mult
    adj *= 1 + np.random.uniform(0.001, 0.003) * age
    return round(max(adj, base))

df['salary'] = df.apply(calculate_adjusted_salary, axis=1)

# =========================
# FORMATO Y GUARDADO
# =========================

df['hiredate'] = pd.to_datetime(df['hiredate']).dt.date
df['birthdate'] = pd.to_datetime(df['birthdate']).dt.date
df['termdate'] = pd.to_datetime(df['termdate']).dt.date

df.to_csv('HumanResources.csv', index=False)

print("Archivo generado: HumanResources.csv")
