def type_infer(df,thresh=8):
    '''
    Try to make a guess on if columns/fields/features are numerical or categorical 
    
    Parameters:
    -----------
    df: pandas DataFrame
    thresh: int, used as cutoff value
    
    Returns:
    --------
    dict,
    like
    
    {'x1': 'Categorical',
     'x2': 'Categorical',
     'x3': 'Numerical',
     'x4': 'Numerical'}
    
    '''
    result = (df.dtypes == object) | ((df.dtypes == np.int) & (df.agg(lambda x: len(x.unique()))<=thresh))
    return dict(result.map(lambda val: 'Categorical' if val else 'Numerical'))
