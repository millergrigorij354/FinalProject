import pandas as pd
import matplotlib.pyplot as plt

# возраст - давление, профессия - ур.стресса, качество - продолжительность, распределение профессий.
def distribution_of_professions(df): pass



def analize_vocation(filename):
    try:
        an=pd.read_csv(filename)
    except Exception as e:
        print(f"шибка чтения файла: {e}")
        return
    make_diag1(an)


def make_diag1(an):
    df=an[['Age', 'Blood Pressure']]
    df['Age']=df.apply(lambda row: int(row['Age']), axis=1)
    df['Blood Pressure']=df.apply(lambda row: int(row['Blood Pressure'][0:3]),axis=1)
    df=df.groupby('Age').mean()
    print(df)
    df.plot(kind='line')
    plt.title(f"Отношение давления к возрасту")
    plt.xlabel('Age')
    plt.ylabel('Blood Pressure')
    plt.show()

analize_vocation('Sleep_health_and_lifestyle_dataset.csv')