import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def reduce_dimensions(data, n_components=2):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(scaled_data)
    
    return pd.DataFrame(pca_result, columns=[f'PC{i+1}' for i in range(n_components)])
