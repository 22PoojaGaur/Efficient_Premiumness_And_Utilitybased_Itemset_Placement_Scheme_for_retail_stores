# graph for Execution time vs number of slots (y vs x)
# x -> y
# num_slots -> ET

# import matplotlib.pyplot as plt

# x = [27182, 54302, 81411, 108521, 122131]
# y = [6.0740, 6.1723, 6.2653, 6.2956, 6.3728]

# plt.plot(x,y)
# plt.yticks([5,6,7])
# plt.xlabel('num_slots')
# plt.ylabel('ET')
# plt.title('Graph for Execution time vs Number of slots')
# plt.show()
#-----------------------------------------------------------------------------------------------------------------

# graph for Number of patterns vs number of slots (y vs x)
# x -> y
# num_slots -> num_patterns

# import matplotlib.pyplot as plt

# x = [27182, 54302, 81411, 108521, 122131]
# y = [27180, 54302, 81410, 108519, 122131]

# plt.plot(x,y)
# plt.xlabel('num_slots')
# plt.ylabel('num_patterns')
# plt.title('Graph for Number of patterns vs Number of slots')
# plt.show()
#--------------------------------------------------------------------------------------------------------------

# graph for Total Revenue vs number of slots (y vs x)
# x -> y
# num_slots -> total_revenue


# import matplotlib.pyplot as plt

# x = [27182, 54302, 81411, 108521, 122131]
# y = [129887, 322622, 580888, 791285, 898228]

# plt.plot(x,y)
# plt.xlabel('num_slots')
# plt.ylabel('total_revenue')
# plt.title('Graph for Total Revenue vs Number of slots')
# plt.show()

#--------------------------------------------------------------------------------------------------------------

# graph for Execution time vs slot types (y vs x)
# slot_types -> ET

# import matplotlib.pyplot as plt

# x = [3,6,9,12,15,18]
# y = [6.3980, 6.3770, 6.3285, 6.3622, 6.3283, 6.3596]

# plt.plot(x,y)
# plt.yticks([5,6,7])
# plt.xlabel('slot_types')
# plt.ylabel('ET')
# plt.title('Graph for Execution time vs Slot Types')
# plt.show()

#--------------------------------------------------------------------------------------------------------------

# graph for Total Revenue vs zipf factor (y vs x)
# zipf factor -> total_revenue

# import matplotlib.pyplot as plt

# x = [0.124, 0.138, 0.230, 0.304, 0.469]
# y = [333904, 316462, 302654, 294853, 282086]

# plt.plot(x,y)
# plt.xlabel('zipf factor')
# plt.ylabel('total_revenue')
# plt.title('Graph for Total Revenue vs Zipf Factor')
# plt.show()

#--------------------------------------------------------------------------------------------------------------

# graph for ET vs zipf factor (y vs x)
# zipf factor -> ET

# import matplotlib.pyplot as plt

# x = [0.124, 0.138, 0.230, 0.304, 0.469]
# y = [6.1210, 6.1204, 6.1144, 6.1272, 6.1141]

# plt.plot(x,y)
# plt.yticks([5,6,7])
# plt.xlabel('zipf factor')
# plt.ylabel('ET')
# plt.title('Graph for ET vs Zipf Factor')
# plt.show()

#------------------------------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt

# x1 = [4000,5000,6000,7000,8000,9000,10000]
# y1 = [524.350,647.144,783.766,899.116,1022.716,1159.811,1285.316]

# plt.plot(x1, y1, label = "Revenue Based") 

# x2 = [4000,5000,6000,7000,8000,9000,10000]
# y2 = [524.616,649.788,782.783,899.844,1023.344,1157.161,1285.316]
# plt.plot(x2, y2, label = "Diversity Based") 

# x3 = [4000,5000,6000,7000,8000,9000,10000]
# y3 = [754.377,817.000,964.727,1069.133,1250.722,1461.566,1551.388]

# plt.plot(x3, y3, label = "Diverse Revenue Based") 
# plt.yticks([500,800,1000,1200,1400,1600])


# plt.xlabel('Number of Slots')
# plt.ylabel('Total Revenue')
# plt.title('Diverse Total Revenue')
# plt.legend() 
# plt.show()

#----------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt

# x1 = [4000,5000,6000,7000,8000,9000,10000]
# y1 = [6.013,6.027,6.0341,6.037,6.038,6.046,6.035]

# plt.plot(x1, y1, label = "Revenue Based")

# x2 = [4000,5000,6000,7000,8000,9000,10000]
# y2 = [6.020,6.024,6.029,6.034,6.039,6.046,6.053]
# plt.plot(x2, y2, label = "Diversity Based") 

# x3 = [4000,5000,6000,7000,8000,9000,10000]
# y3 = [6.015,6.018,6.030,6.034,6.040,6.046,6.052]

# plt.plot(x3, y3, label = "Diverse Revenue Based") 
# plt.yticks([5,6,7])


# plt.xlabel('Number of Slots')
# plt.ylabel('ET')
# plt.title('diverse revenue execution time')
# plt.legend() 
# plt.show()


#--------------------------------------------------------------------------------

# import matplotlib.pyplot as plt

# x1 = [4000,5000,6000,7000,8000,9000,10000]
# y1 = [292.633,359.199,424.966,496.799,576.133,647.866,728.166]

# plt.plot(x1, y1, label = "0 slot")

# x2 = [4000,5000,6000,7000,8000,9000,10000]
# y2 = [280.633,365.666,424.933,471.566,540.233,646.733,681.966]
# plt.plot(x2, y2, label = "1 slot") 

# x3 = [4000,5000,6000,7000,8000,9000,10000]
# y3 = [274.199,315.333,438.999,499.599,529.399,565.733,648.500]

# plt.plot(x3, y3, label = "2 slot") 
# plt.yticks([200,400,600,800])


# plt.xlabel('Number of Slots')
# plt.ylabel('slots wise revenue')
# plt.title('revenue based')
# plt.legend() 
# plt.show()

#------------------------------------------------------------------------

# import matplotlib.pyplot as plt

# x1 = [4000,5000,6000,7000,8000,9000,10000]
# y1 = [292.833,360.533,424.266,497.566,576.533, 646.366,728.166]

# plt.plot(x1, y1, label = "0 slot")

# x2 = [4000,5000,6000,7000,8000,9000,10000]
# y2 = [280.633,367.933,425.033,470.799,540.799,645.633,681.966]
# plt.plot(x2, y2, label = "1 slot") 

# x3 = [4000,5000,6000,7000,8000,9000,10000]
# y3 = [274.399,315.866,437.999,500.633,529.233,563.933,648.500]

# plt.plot(x3, y3, label = "2 slot") 
# plt.yticks([200,400,600,800])


# plt.xlabel('Number of Slots')
# plt.ylabel('slots wise revenue')
# plt.title('diversity based')
# plt.legend() 
# plt.show()

#------------------------------------------------------------------------------

import matplotlib.pyplot as plt

x1 = [4000,5000,6000,7000,8000,9000,10000]
y1 = [443.599,488.733,529.833,650.999,781.100,993.966,1032.933]

plt.plot(x1, y1, label = "0 slot")

x2 = [4000,5000,6000,7000,8000,9000,10000]
y2 = [409.666,429.666,573.499,512.933,635.733,618.266,706.933]
plt.plot(x2, y2, label = "1 slot") 

x3 = [4000,5000,6000,7000,8000,9000,10000]
y3 = [317.833,340.299,444.433,485.000,455.266,475.399,494.966]

plt.plot(x3, y3, label = "2 slot") 
plt.yticks([300,600,900,1100])


plt.xlabel('Number of Slots')
plt.ylabel('slots wise revenue')
plt.title('diverse revenue based')
plt.legend() 
plt.show()