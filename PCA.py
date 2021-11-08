import numpy as np
 
def PCA(X , num_components):
     
    #Subtract the mean of each variable from the dataset
    X_meaned = X - np.mean(X , axis = 0)
     
    #Calculate the Covariance Matrix
    cov_mat = np.cov(X_meaned , rowvar = False)
     
    #Compute the Eigenvalues and Eigenvectors
    eigen_values , eigen_vectors = np.linalg.eigh(cov_mat)
     
    #Sort Eigenvalues in descending order
    sorted_index = np.argsort(eigen_values)[::-1]
    sorted_eigenvalue = eigen_values[sorted_index]
    sorted_eigenvectors = eigen_vectors[:,sorted_index]
     
    #Select a subset from the rearranged Eigenvalue matrix
    eigenvector_subset = sorted_eigenvectors[:,0:num_components]
     
    #Transform the data
    X_reduced = np.dot(eigenvector_subset.transpose() , X_meaned.transpose() ).transpose()
     
    return X_reduced
