# graph for Execution time vs number of slots (y vs x)
# x -> y
# num_slots -> ET

# import matplotlib.pyplot as plt

# x = [27182, 54302, 81411, 108521, 122131]
# y = [0.0740, 0.1723, 0.2653, 0.2956, 0.3728]

# plt.plot(x,y)
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
# y = [0.3980, 0.3770, 0.3285, 0.3622, 0.3283, 0.3596]

# plt.plot(x,y)
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

import matplotlib.pyplot as plt

x = [0.124, 0.138, 0.230, 0.304, 0.469]
y = [0.1210, 0.1204, 0.1144, 0.1272, 0.1141]

plt.plot(x,y)
plt.xlabel('zipf factor')
plt.ylabel('ET')
plt.title('Graph for ET vs Zipf Factor')
plt.show()