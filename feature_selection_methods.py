def find_high_correlation_features(m,thresh=0.95):
    '''
    Parameters: 
    ------------
    m: 2D array
    thresh: float, remove features with correlation coefficients higher than thresh
    
    Returns:
    --------
    numpy array: index of columns needed to remove
   
    '''
    # Create correlation matrix
    corr_matrix = np.corrcoef(m,rowvar=False)
    # Select upper triangle of correlation matrix
    upper = np.triu(m,k=1)
    # Find index of feature columns with correlation greater than thresh value
    return np.where(upper.__abs__().__gt__(thresh).any(axis=0))
