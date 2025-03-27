import pandas as pd

def calculate_demographic_data(print_data=True):
    """
    Analisa um conjunto de dados demográficos e calcula estatísticas relevantes.

    Retorna:
        dict: Um dicionário contendo estatísticas como:
            - Quantidade de pessoas por raça
            - Média de idade dos homens
            - Percentual de pessoas com ensino superior
            - Percentual de pessoas com e sem ensino superior que ganham >50K
            - Menor carga horária semanal trabalhada
            - Percentual de pessoas que ganham >50K entre os que trabalham menos horas
            - País com maior percentual de pessoas que ganham >50K
            - Ocupação mais comum entre indianos que ganham >50K
    """
    
    # Carrega os dados do arquivo CSV
    df = pd.read_csv('adult.data.csv')

    # Conta a quantidade de pessoas de cada raça presente no conjunto de dados
    race_count = df['race'].value_counts()

    # Calcula a idade média dos homens, arredondada para uma casa decimal
    age_men = df[df['sex'] == 'Male']
    average_age_men = round(age_men['age'].mean(), 1)

    # Calcula a porcentagem de pessoas com diploma de bacharel
    bachelors = (df['education'] == 'Bachelors')
    percentage_bachelors = round(bachelors.mean() * 100, 1)


    # Cria uma máscara para pessoas com ensino superior (Bacharelado, Mestrado ou Doutorado)
    mask = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    advanced_education = df[mask]
    salary = advanced_education['salary'] == '>50K'
    percentage = round(salary.mean() * 100)

    # Calcula o percentual de pessoas sem ensino superior que ganham mais de 50K
    not_ad_education = df[~mask]
    salary_2 = not_ad_education['salary'] == '>50K'
    percentage_2 = round(salary_2.mean() * 100)

    # Separa os grupos de pessoas com e sem ensino superior
    higher_education = df[mask]
    lower_education = df[~mask]

    # Calcula o percentual de pessoas que ganham >50K em cada grupo educacional (com ensino superior e sem, respectivamente)
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # Determina o menor número de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # Calcula o percentual de pessoas que trabalham o mínimo de horas e ganham >50K
    num_min_mask = (df['hours-per-week'] == df['hours-per-week'].min())
    num_min = df[num_min_mask]
    num_min_workers = (num_min['salary'] == '>50K')
    
    rich_percentage = round(num_min_workers.mean() * 100)

    # Determina o país com a maior porcentagem de pessoas que ganham >50K
    fifth_k = (df[df['salary'] == '>50K'])
    per = ((fifth_k['native-country'].value_counts() / df['native-country'].value_counts()) * 100)
    highest_earning_country = per.idxmax()
    highest_earning_country_percentage = round(per.max(), 1)

    # Identifica a ocupação mais comum entre os indianos que ganham >50K
    india = fifth_k[fifth_k['native-country'] == 'India']
    top_IN_occupation = india['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }