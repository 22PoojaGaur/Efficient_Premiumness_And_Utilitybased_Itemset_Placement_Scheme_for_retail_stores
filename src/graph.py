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

# import matplotlib.pyplot as plt

# x1 = [4000,5000,6000,7000,8000,9000,10000]
# y1 = [443.599,488.733,529.833,650.999,781.100,993.966,1032.933]

# plt.plot(x1, y1, label = "0 slot")

# x2 = [4000,5000,6000,7000,8000,9000,10000]
# y2 = [409.666,429.666,573.499,512.933,635.733,618.266,706.933]
# plt.plot(x2, y2, label = "1 slot") 

# x3 = [4000,5000,6000,7000,8000,9000,10000]
# y3 = [317.833,340.299,444.433,485.000,455.266,475.399,494.966]

# plt.plot(x3, y3, label = "2 slot") 
# plt.yticks([300,600,900,1100])


# plt.xlabel('Number of Slots')
# plt.ylabel('slots wise revenue')
# plt.title('diverse revenue based')
# plt.legend() 
# plt.show()

#------------------------------------------------------------------------------------
# import matplotlib.pyplot as plt

# x1 = [1500,1600,1700,1800,1900,2000]
# y1 = [14411.11,14827.43,15518.28,17286.35,17004.69,18272.57]

# plt.plot(x1, y1, label = "Frequency Based") 

# x2 = [1500,1600,1700,1800,1900,2000]
# y2 = [4765.78,4984.58,5708.86,6181.04,6566.33,7073.84]
# plt.plot(x2, y2, label = "price(revenue) Based")

# x3 = [1500,1600,1700,1800,1900,2000]
# y3 = [17125.70,18928.82,19476.33,20418.97,22092.55,22481.40]
# plt.plot(x3, y3, label = "Net Revenue")

# x4 = [1500,1600,1700,1800,1900,2000]
# y4 = [2057.16,2164.92,2164.92,2550.95,2722.38,2837.16]

# plt.plot(x4, y4, label = "Diversity Based") 

# x5 = [1500,1600,1700,1800,1900,2000]
# y5 = [18800.94,19366.30,19366.30,21164.57,21981.86,22374.83]
# plt.plot(x5, y5, label = "Diverse Revenue Based")

# plt.xlabel('Number of Slots')
# plt.ylabel('Total Revenue')
# plt.legend() 
# plt.show()

# -------------------------------------------------------------------- hybrid approach with drank threshold ---------------
# itemset ratio 0.5
# drank threshold >2

# import matplotlib.pyplot as plt

# x1 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
# y1 = [1004.21, 2648.11, 3417.73, 4538.60, 6603.24, 7743.29, 9222.90, 9867.55, 10722.16, 11535.46, 12693.88]

# plt.plot(x1, y1, label = "Frequency Based") 

# x2 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
# y2 = [113.0, 348.0, 534.16, 762.66, 1202.82, 1523.90, 2058.66, 2414.12, 2943.81, 3278.70, 3740.85]
# plt.plot(x2, y2, label = "price(revenue) Based")

# x3 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
# y3 = [1457.65, 3542.83, 4335.81, 5847.90, 7970.10, 9418.92, 11115.50, 11986.80, 13028.39, 13938.02, 15437.04]
# plt.plot(x3, y3, label = "Net Revenue")

# x4 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
# y4 = [47.43, 168.36, 227.89, 344.98, 503.60, 670.71, 883.80, 1024.67, 1182.86, 1359.27, 1544.04]

# plt.plot(x4, y4, label = "Diversity Based") 

# x5 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
# y5 = [953.88, 2273.37, 2710.64, 3545.08, 4647.98, 5389.17, 6238.41,6659.36, 7149.85, 7598.45, 8323.03]
# plt.plot(x5, y5, label = "Diverse Revenue Based")

# plt.xlabel('Number of Slots')
# plt.ylabel('Total Revenue')
# plt.legend() 
# plt.show()

# ----------------------- drank threshold >=2 -------------
import matplotlib.pyplot as plt

x1 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
y1 = [1004.21, 2648.11, 3417.73, 4538.60, 6603.24, 7743.29, 9222.90, 9867.55, 10722.16, 11535.46, 12693.88]

plt.plot(x1, y1, label = "Frequency Based") 

x2 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
y2 = [113.0, 348.0, 534.16, 762.66, 1202.82, 1523.90, 2058.66, 2414.12, 2943.81, 3278.70, 3740.85]
plt.plot(x2, y2, label = "price(revenue) Based")

x3 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
y3 = [1457.65, 3542.83, 4335.81, 5847.90, 7970.10, 9418.92, 11115.50, 11986.80, 13028.39, 13938.02, 15437.04]
plt.plot(x3, y3, label = "Net Revenue")

x4 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
y4 = [47.43, 168.36, 227.89, 344.98, 503.60, 670.71, 883.80, 1024.67, 1182.86, 1359.27, 1544.04]

plt.plot(x4, y4, label = "Diversity Based") 

x5 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
y5 = [1364.21, 3265.88, 3913.05, 5101.45, 6801.64, 7961.08, 9298.81, 9982.19, 10796.14, 11494.26, 12666.86  ]
plt.plot(x5, y5, label = "Diverse Revenue Based")

plt.xlabel('Number of Slots')
plt.ylabel('Total Revenue')
plt.legend() 
plt.show()