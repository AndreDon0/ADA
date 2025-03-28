import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import RobustScaler
from sklearn.impute import SimpleImputer
from tqdm import tqdm
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

class GroupRobustScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.scalers = {}
        self.group_imputer = SimpleImputer(strategy='median')

    def fit(self, X, y=None):
        self.scalers = {}
        groups = X['subject_id']
        features = X.drop(columns=['subject_id', 'timestamp'])
        
        # Импутация и масштабирование для каждой группы
        for group in tqdm(groups.unique(), desc='Scaling groups'):
            mask = (groups == group)
            group_data = self.group_imputer.fit_transform(features[mask])
            scaler = RobustScaler().fit(group_data)
            self.scalers[group] = (scaler, self.group_imputer)
        return self

    def transform(self, X):
        groups = X['subject_id']
        features = X.drop(columns=['subject_id', 'timestamp'])
        transformed = features.copy()
        
        for group in tqdm(groups.unique(), desc='Transforming groups'):
            mask = (groups == group)
            if group in self.scalers:
                scaler, imputer = self.scalers[group]
                imputed_data = imputer.transform(features[mask])
                scaled_data = scaler.transform(imputed_data)
                transformed.loc[mask] = scaled_data
        return transformed.dropna()

def process_data(df):
    pipeline = Pipeline([
        ('group_scaler', GroupRobustScaler()),
        ('final_imputer', SimpleImputer(strategy='median')),
        ('pca', PCA(n_components=0.95, random_state=42)),
        ('cluster', KMeans(n_clusters=5, n_init='auto', random_state=42))
    ])

    with tqdm(total=4, desc='Processing pipeline') as pbar:
        # Полная обработка данных
        clean_df = df.dropna(subset=df.columns.difference(['subject_id', 'timestamp']))
        pipeline.fit(clean_df)
        pbar.update(1)
        
        # Получение преобразованных данных
        processed_data = pipeline[:-1].transform(clean_df)
        pbar.update(1)
        
        # Проверка на NaN
        assert not np.isnan(processed_data).any(), "NaN values detected after transformation"
        pbar.update(1)
        
        # Кластеризация
        labels = pipeline.named_steps['cluster'].fit_predict(processed_data)
        pbar.update(1)
    
    return pipeline, processed_data, labels