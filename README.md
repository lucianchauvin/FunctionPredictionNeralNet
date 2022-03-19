# Function Prediction Neural-Net
Generates a predictive keras Neural Net model for any mathmatical function on a given interval. This was my first real interaction with neural nets and machine learning. 
It works by generating data from the given function, mapping it to a scaled sigmoid function, and then train the keras sequential model from this data. I learned a lot from this project from normalizing data before training, using activation layers, and just generally how neural nets work. 

# Issues
One major problem that is still inculded in this code is that func(min) and func(max) should return the ABSOLUTE MAXIMUM of the function used on the inputed interval. This could be fixed by finding the ABSOLUTE min and max of this function using calculs instead of assuming where they are. 
