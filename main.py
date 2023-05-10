import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def func(d_M_1_z, d_M_3_z, d_f_1_z, d_f_3_z):
    m = 225
    I = 12.5
    # 1:
    T = 20
    # L = math.sqrt(I/m)
    L = 0.1
    # L = 10
    # L = 1
    f_1_z = 20
    # 2:
    f_2_z = 0
    # 3:
    f_3_z = -20

    f_z_max = 4



    # обезразмеривание данных

    f_z_max_dimensionless = f_z_max/(m*L) * T**2

    f_1_z_dimensionless = f_1_z/(m*L) * T**2
    f_2_z_dimensionless = f_2_z/(m*L) * T**2
    f_3_z_dimensionless = f_3_z/(m*L) * T**2


    d_f_1_z_dimensionless = d_f_1_z/(m*L) * T**2
    d_f_3_z_dimensionless = d_f_3_z/(m*L) * T**2


    d_M_1_z_dimensionless = d_M_1_z/I * T**2
    d_M_3_z_dimensionless = d_M_3_z/I * T**2


    T = 20/T

    q_0 = [0 for i in range(6)]
    q_1 = [0 for i in range(6)]
    q_2 = [0 for i in range(6)]
    q_3 = [0 for i in range(6)]

    q_1[2] = -f_z_max_dimensionless/2*T**2 + q_0[3]*T**1 + q_0[2]
    q_1[3] = -f_z_max_dimensionless*T**1 + q_0[3]

    q_2[2] = -f_z_max_dimensionless/2*T**2 + q_1[3]*T**1 + q_1[2]
    q_2[3] = -f_z_max_dimensionless*T**1 + q_1[3]

    q_3[2] = -f_z_max_dimensionless/2*T**2 + q_2[3]*T**1 + q_2[2]
    q_3[3] = -f_z_max_dimensionless*T**1 + q_2[3]

    print(q_3)

    s_0 = [0 for i in range(6)]


    s_1 = [d_f_1_z_dimensionless/2*T**2 + s_0[1]*T**1 + s_0[0],
           d_f_1_z_dimensionless*T**1 + s_0[1],
           -f_1_z_dimensionless  * (d_M_1_z_dimensionless/24*T**4 + s_0[
               5]/6*T**3 + s_0[4]/2*T**2 + s_0[3]*T**1 + s_0[2]),
           -f_1_z_dimensionless  * (d_M_1_z_dimensionless/6*T**3 + s_0[5]/2*T**2 +
                                   s_0[4]*T**1+ s_0[3]),
           d_M_1_z_dimensionless/2*T**2 + s_0[5]*T**1 + s_0[4],
           d_M_1_z_dimensionless*T**1 + s_0[5]
           ]
    # print(s_1)
    s_2 = [0/2*T**2 + s_1[1]*T**1 + s_1[0],
           0*T**1 + s_1[1],
           -f_2_z_dimensionless * (0/24*T**4 + s_1[5]/6*T**3 + s_1[
               4]/2*T**2 + s_1[3]*T**1 + s_1[2]),
           -f_2_z_dimensionless * (0/6*T**3 + s_1[5]/2*T**2 + s_1[4]*T**1+
           s_1[3]),
           0/2*T**2 + s_1[5]*T**1 + s_1[4],
           0*T**1 + s_1[5]
           ]
    # print(s_2)


    s_3 = [d_f_3_z_dimensionless/2*T**2 + s_2[1]*T**1 + s_2[0],
           d_f_3_z_dimensionless*T**1 + s_2[1],
           -f_3_z_dimensionless  * (d_M_3_z_dimensionless/24*T**4 + s_2[
               5]/6*T**3 +
                                   s_2[
               4]/2*T**2 + s_2[3]*T**1 + s_2[2]),
           -f_3_z_dimensionless  * (d_M_3_z_dimensionless/6*T**3 + s_2[
               5]/2*T**2 +
                                   s_2[4]*T**1+
           s_2[3]),
           d_M_3_z_dimensionless/2*T**2 + s_2[5]*T**1 + s_2[4],
           d_M_3_z_dimensionless*T**1 + s_2[5]
           ]
    # print(s_3)


    RoX = math.sqrt((s_3[2] - q_3[2])**2 + (s_3[0] - q_3[0])**2)

    # print(RoX)
    if (s_3[2] - q_3[2]) * (s_3[2] + q_3[2]) < 0:
        Ro0 = math.fabs(s_3[0] + q_3[0])
    else:
        Ro0 = math.sqrt((s_3[2] + q_3[2])**2 + (s_3[0] + q_3[0])**2)
    # print(Ro0)

    Ro = min(Ro0, RoX)
    # print(Ro)
    return Ro, RoX, s_3[2], q_3[2], s_3[0]


# a)
# d_M_1_z = -0.0005
# d_M_3_z = 0
# d_f_1_z = -0.05
# d_f_3_z = 0

# б)
# d_M_1_z = 0.0005
# d_M_3_z = 0
# d_f_1_z = 0.05
# d_f_3_z = 1


# в)
# d_M_1_z = -0.0005
# d_M_3_z = -0.02
# d_f_1_z = 0.01
# d_f_3_z = -0.1


# г)
# d_M_1_z = 0.0005
# d_M_3_z = -0.002
# d_f_1_z = -0.05
# d_f_3_z = 0.1


Ro_array = []
RoX_array = []
s_2_array = []
s_0_array = []
q_2_array = []
minus_q_2_array = []
Ro, RoX, s_2, q_2, s_0 = func(-0.0005, 0, -0.05, 0)
Ro_array.append(Ro)
RoX_array.append(RoX)
s_2_array.append(s_2)
s_0_array.append(s_0)
q_2_array.append(q_2)
minus_q_2_array.append(-q_2)

Ro, RoX, s_2, q_2, s_0 = func(0.0005, 0, 0.05, 1)
Ro_array.append(Ro)
RoX_array.append(RoX)
s_2_array.append(s_2)
s_0_array.append(s_0)
q_2_array.append(q_2)
minus_q_2_array.append(-q_2)

Ro, RoX, s_2, q_2, s_0 = func(-0.0005, -0.02, 0.01, -0.1)
Ro_array.append(Ro)
RoX_array.append(RoX)
s_2_array.append(s_2)
s_0_array.append(s_0)
q_2_array.append(q_2)
minus_q_2_array.append(-q_2)

Ro, RoX, s_2, q_2, s_0 = func(0.0005, -0.002, -0.05, 0.1)
Ro_array.append(Ro)
RoX_array.append(RoX)
s_2_array.append(s_2)
s_0_array.append(s_0)
q_2_array.append(q_2)
minus_q_2_array.append(-q_2)

r = max(Ro_array)

for i in range(len(Ro_array)):
    if r == Ro_array[i] and ((s_2_array[i] - q_2_array[0]) * (s_2_array[i] +
                                                             q_2_array[0])) < 0:
        X = s_2_array[i]
        break
    else:
        X = q_2_array[0]


Y = 0

t = [math.pi * 0.05]
x = [X + r * math.cos(t[0])]
y = [Y + r * math.sin(t[0])]


for i in range(40):
    t.append(t[-1] + t[0])
    x.append(X + r * math.cos(t[-1]))
    y.append(Y + r * math.sin(t[-1]))


fig, ax = plt.subplots()

ax.plot(x, y, color = 'r', linewidth = 3)

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

#  Добавляем линии основной сетки:
ax.grid(which='major',
        color = 'k')

#  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#  Теперь можем отдельно задавать внешний вид
#  вспомогательной сетки:
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')
fig.set_figwidth(12)
fig.set_figheight(8)


plt.plot(x, y,color='yellow')
plt.plot([-q_2_array[0], q_2_array[0]], [0,0], 'k', color='blue', linewidth = 3)
plt.scatter(s_2_array[0], s_0_array[0], s=50, color='red')
plt.scatter(s_2_array[1], s_0_array[1], s=50, color='red')
plt.scatter(s_2_array[2], s_0_array[2], s=50, color='red')
plt.scatter(s_2_array[3], s_0_array[3], s=50, color='red')


plt.savefig(f"graf")

