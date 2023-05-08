import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

# import matplotlib.ticker as mtick


# set plot style
plt.style.use(['science', 'grid', 'no-latex'])

# create numerical sequences
t = np.linspace(1, 2, 11)
c = np.linspace(10, 15, 6)
a = np.linspace(100, 200, 11)
r = np.array([0, 0.02, 0.03, 0.05, 0.07, 0.1, 0.17, 0.25, 0.35, 0.5, 0.7])
b0 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
b1 = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

# create meshgrid from the numerical sequences for all combinations of values
T, R, B0, B1, C, A = np.meshgrid(t, r, b0, b1, c, a, indexing='ij')

# define condition and euqation
condition = B1 > B0
# equation: quantity of firm M minus firm L
equation = B0 * (A - C - T) - B1 * (A - C - C * R) + 3 * (C * R - T)

# The impact of b1 on the equilibrium quantity gap
b1_gap = np.where(condition, equation, np.nan)
b1_abs_dict = {}
for b1_val in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    b1_arr = b1_gap[B1 == b1_val]
    b1_abs = np.where(b1_arr > 0, 1, np.where(b1_arr < 0, 0, np.nan))
    b1_abs_dict[b1_val] = b1_abs
b1_mean = np.array([np.nanmean(b1_abs_dict[b1_val]) for b1_val in b1_abs_dict])

# The impact of a on the equilibrium quantity gap
a_gap = np.where(condition, equation, np.nan)
a_abs_dict = {}
for a_val in [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]:
    a_arr = a_gap[A == a_val]
    a_abs = np.where(a_arr > 0, 1, np.where(a_arr < 0, 0, np.nan))
    a_abs_dict[a_val] = a_abs
a_mean = np.array([np.nanmean(a_abs_dict[a_val]) for a_val in a_abs_dict])

r_gap = np.where(condition, equation, np.nan)
r_abs_dict = {}
for r_val in [0, 0.02, 0.03, 0.05, 0.07, 0.1, 0.17, 0.25, 0.35, 0.5, 0.7]:
    r_arr = r_gap[R == r_val]
    r_abs = np.where(r_arr > 0, 1, np.where(r_arr < 0, 0, np.nan))
    r_abs_dict[r_val] = r_abs
r_mean = np.array([np.nanmean(r_abs_dict[r_val]) for r_val in r_abs_dict])


# create a figure and axis object for the plot
fig, (ax1, ax2, ax3) = plt.subplots(figsize=(11, 3.5), ncols=3)
# set transparency
fig.patch.set_alpha(0)

# plot of ax1 about b1 and b1_mean
ax1.plot(
    b1, b1_mean, linestyle='--', marker='D', color='black', markerfacecolor='white'
)
# ax1.plot(b1, b1_mean, '#81b8df', alpha=0.618)
ax1.set_title("(i)海南规模不经济的变化", fontproperties="Simsun")
ax1.set_xlabel(r'$b_{1}$', size=12)
ax1.set_ylabel(r'$P\left \{ q ̃_m^*>q ̃_l^* \right \} $')
ax1.patch.set_alpha(0)
ax1.grid(linestyle='-.')
ax1.tick_params(labelsize=12)
# ax1.fill_between(b1, 0, b1_mean, facecolor='#81b8df', alpha=0.618)
ax1.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
# ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

# plot of ax2 about b2 and b2_mean
ax2.plot(a, a_mean, linestyle="--", marker='D', color="black", markerfacecolor='white')
# ax2.plot(a, a_mean, '#81b8df', alpha=0.618)
ax2.set_title("(ii)市场规模的变化", fontproperties="Simsun")
ax2.set_xlabel(r'$\alpha$', size=12)
ax2.patch.set_alpha(0)
ax2.grid(linestyle='-.')
ax2.tick_params(labelsize=12)
# ax2.fill_between(a, 0, a_mean, facecolor='#81b8df', alpha=0.618)
ax2.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
# ax2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

# plot of ax2 about b2 and b2_mean
ax3.plot(r, r_mean, linestyle="--", marker='D', color="black", markerfacecolor='white')
# ax3.plot(r, r_mean, '#81b8df', alpha=0.618)
ax3.set_title("(iii)关税税率的变化", fontproperties="Simsun")
ax3.set_xlabel(r'$r$', size=12)
ax3.patch.set_alpha(0)
ax3.grid(linestyle='-.')
ax3.tick_params(labelsize=12)
# ax3.fill_between(r, 0, r_mean, facecolor='#81b8df', alpha=0.618)
ax3.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
# ax3.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

# show plot
fig.tight_layout()
plt.show()
