# Salary-vs-Experiance
An ML model that predicts your salary based on how many years of experience you have. This is my first ML model using linear regression, I hope you like it :). 

Blue line = predicted values 
Red Dots = actual values

The more data you add into the csv file (the easiest way to do this is on your prefered ide) the more accurate the blue line will be. The more data you remove the less accurate the blue line will be. 

To remove data you can either just delete it on the csv file, or change the row vaules in lines 8 and 9. 
To change the row vals change the first parameter in .iloc[] function. Ex: dataset.iloc[0:3,:]. This will give you rows from 0 to 2 (since last val is exclusive).

**Do not change the last parmeter in the .iloc[] function, this will mess up the model.**

Thanks! 
