def outliers(df, name):

    Q1 = df[name].quantile(0.25)
    Q3 = df[name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR


    outliers = df[(df[name] < lower_bound) | (df[name] > upper_bound)]

    print(f'Number of outliers in {name} column was {len(outliers)}')

    df = df[(df[name] >= lower_bound) & (df[name] <= upper_bound)]

    return df


def num_isnull(df):
    return df.isnull().sum()
