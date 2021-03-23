import numpy as np

def sor_solver(A, b, omega, initial_guess, convergence_criteria,T,k):
  """
  This is an implementation of the pseduo-code provided in the Wikipedia article.
  Inputs:
    A: nxn numpy matrix
    b: n dimensional numpy vector
    omega: relaxation factor
    initial_guess: An initial solution guess for the solver to start with
  Returns:
    phi: solution vector of dimension n
  """
  count = 0
  phi = initial_guess[:]
  residual = np.linalg.norm(np.matmul(A, phi) - b) #Initial residual
      
  while residual > convergence_criteria and count<=k:
        for i in range(A.shape[0]):
          sigma = 0
          for j in range(A.shape[1]):
            if j != i:
              sigma += A[i][j] * phi[j]
              T[i][j] = sigma
          phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma)
          
        print('Iteración:{0}'.format(count))
        print(T)
        residual = np.linalg.norm(np.matmul(A, phi) - b)
        print('{0}'.format(phi))
        print('Error: {0:10.9g}\n'.format(residual))
        count+=1
         
  return phi

#An example case that mirrors the one in the Wikipedia article
residual_convergence = 1e-8
omega = 1.456 #Relaxation factor

A = np.ones((3, 3))
A[0][0] = 4
A[0][1] = -1
A[0][2] = 1

A[1][0] = 1
A[1][1] = 3
A[1][2] = -2

A[2][0] = 1
A[2][1] = 1
A[2][2] = -7

b = np.ones(3)
b[0] = 27.3
b[1] = 18.666
b[2] = np.pi

initial_guess = np.zeros(3)
T = np.ones((3,3))
phi = sor_solver(A, b, omega, initial_guess, residual_convergence,T,100)
print(phi)