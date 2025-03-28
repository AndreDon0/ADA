import pandas as pd


def normalize_cluster_labels(cluster_series, column_name):
    cluster_series[column_name] = pd.Series(pd.factorize(cluster_series[column_name])[0] + 1)
    return cluster_series


def fulling_indexes(df):
    # Создаем полный диапазон индексов от минимального до максимального
    min_idx = df['Index'].min()
    max_idx = df['Index'].max()
    full_index = pd.DataFrame({'Index': range(min_idx, max_idx + 1)})
    
    # Объединяем с исходными данными, чтобы добавить отсутствующие индексы
    df_filled = full_index.merge(df, on='Index', how='left')
    
    # Заполняем пропуски в `activityID` значением 1 и преобразуем к целому типу
    df_filled['activityID'] = df_filled['activityID'].fillna(1).astype(int)
    
    return df_filled

if __name__ == "__main__":
    # Пример входных данных
    data = {
        'Index': [1, 2, 3, 4, 5, 7],
        'activityID': [5, 2, 5, 4, 2, 3]
    }

    # Создание DataFrame
    df = pd.DataFrame(data)

    # Преобразование кластеров
    df = normalize_cluster_labels(df, "activityID")
    df = fulling_indexes(df)

    # Вывод результата
    print(df)