# TODO: import ...
import numpy as np
import matplotlib.pyplot as plt

def generate_random_matrix(m,n):
    matrix=np.random.randint(0,2,(m,n))
    return matrix
def save_matrix(matrix,picture_name):
    plt.imshow(matrix)
    plt.savefig(picture_name)    
if __name__=="__main__":
    matrix=generate_random_matrix(10,10)
    save_matrix(matrix,"example.jpg")