import matplotlib.pyplot as plt

learning_rate_ALPHA = float(0.0001)
initial_theta_0 = float(0)
initial_theta_1 = float(0)
nombre_iterations = 2000
X=[i for i in range(3000)]
Y=[2*i for i in range(3000)]
M=len(X)

def calc_derivatives(oldtheta_0, oldtheta_1):
    derivtheta_0 = float(0)
    derivtheta_1 = float(0)
    for i in range(0, len(X)):
        derivtheta_0 = float(((oldtheta_0 + (oldtheta_1 * X[i])) - float(Y[i])))
        derivtheta_1 = (((oldtheta_0 + (oldtheta_1 * X[i]))) - float(Y[i])) * float(X[i])  
    derivtheta_0 = (1/M) * derivtheta_0
    derivtheta_1 = (1/M) * derivtheta_1
    return [derivtheta_0, derivtheta_1]

def calc_theta(oldtheta_0, oldtheta_1):
    [derivtheta_0, derivtheta_1] = calc_derivatives(oldtheta_0,oldtheta_1)
    newtheta_0 = oldtheta_0 - (learning_rate_ALPHA * derivtheta_0)
    newtheta_1 = oldtheta_1 - (learning_rate_ALPHA * derivtheta_1)
    return [newtheta_0,newtheta_1]


def gradient_descent():
    theta_00 = initial_theta_0
    theta_11 = initial_theta_1   
    for i in range(nombre_iterations):
        [newtheta_0, newtheta_1] = calc_theta(theta_00, theta_11)
        theta_00 = newtheta_0
        theta_11 = newtheta_1
    return [theta_00, theta_11]         

[final_theta_0, final_theta_1] = gradient_descent()

print ("theta_0 = {0}, theta_1 = {1}".format(final_theta_0, final_theta_1))
Y1=[2*i for i in range(3000)]
for i in range(3000):
    Y1[i]= final_theta_0 + final_theta_1 * X[i]

axes = plt.axes()
axes.grid()
plt.scatter(X,Y1, color = "m")
plt.plot(X, Y, color = "g")
plt.show()
