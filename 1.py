import pandas as pd
import matplotlib.pyplot as plt

# распределение профессий.
def analize_vocation(filename):
    try:
        an=pd.read_csv(filename)
    except Exception as e:
        print(f"шибка чтения файла: {e}")
        return
    make_diag_pressureage(an)
    make_diag_occupationStress(an)
    make_diag_Quality_of_SleepSleep_Duration(an)
    make_diag_Occupation(an)


def make_diag_pressureage(an):
    df=an[['Age', 'Blood Pressure']]
    df['Age']=df.apply(lambda row: int(row['Age']), axis=1)
    df['Blood Pressure']=df.apply(lambda row: int(row['Blood Pressure'][0:3]),axis=1)
    df=df.groupby('Age').mean()
    print(df)
    df.plot(kind='line', color='g')
    plt.title(f"Отношение давления к возрасту")
    plt.xlabel('Age')
    plt.ylabel('Blood Pressure')
    plt.show()


def make_diag_occupationStress(an):
    df=an[['Occupation', 'Stress Level']]
    df['Stress Level']=df.apply(lambda row: int(row['Stress Level']), axis=1)
    df=df.groupby('Occupation').mean()
    print(df)
    df.plot(kind='bar', color='r')
    plt.title(f"Отношение стресса к профессии")
    plt.xlabel('Occupation')
    plt.ylabel('Stress Level')
    plt.show()


def make_diag_Quality_of_SleepSleep_Duration(an):
    df=an[['Quality of Sleep', 'Sleep Duration']]
    df['Quality of Sleep']=df.apply(lambda row: int(row['Quality of Sleep']), axis=1)
    df=df.groupby('Sleep Duration').mean()
    print(df)
    df.plot(kind='hist')
    plt.title(f"Отношение качества сна к длине сна")
    plt.xlabel('Quality of Sleep')
    plt.ylabel('Sleep Duration')
    plt.show()


def make_diag_Occupation(an):
    df = an['Occupation'].value_counts()
    print(df)
    df.plot(kind='pie')
    plt.title(f"Распределение профессий")
    plt.show()



analize_vocation('Sleep_health_and_lifestyle_dataset.csv')