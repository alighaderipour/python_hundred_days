import matplotlib.pyplot as plt
import numpy as np


# معادله اول: 2u + v + w = 5
def plane1(u, v):
    return 5 - 2 * u - v


# معادله دوم: 4u - 6v = -2 -> w مستقل نیست، صفحه دوم فقط در محورهای u و v است
# برای نمایش بهتر صفحه w = 0 در نظر گرفته می‌شود
def plane2(u, v):
    return 0  # این معادله به w وابسته نیست


# معادله سوم: -2u + 7v + 2w = 9
def plane3(u, v):
    return (9 + 2 * u - 7 * v) / 2


# تولید نقاط
u_vals = np.linspace(-10, 10, 100)
v_vals = np.linspace(-10, 10, 100)
u, v = np.meshgrid(u_vals, v_vals)

# محاسبه مقادیر w برای هر صفحه
w1 = plane1(u, v)
# برای معادله دوم، صفحه‌ای که مقدار w برای آن صفر است را در نظر می‌گیریم
w2 = np.zeros_like(u)
w3 = plane3(u, v)
# رسم نمودار اصلاح‌شده
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

# رسم صفحات
ax.plot_surface(
    u, v, w1, color="blue", alpha=0.5, rstride=100, cstride=100, label="2u + v + w = 5"
)
ax.plot_surface(
    u, v, w2, color="green", alpha=0.5, rstride=100, cstride=100, label="4u - 6v = -2"
)
ax.plot_surface(
    u,
    v,
    w3,
    color="red",
    alpha=0.5,
    rstride=100,
    cstride=100,
    label="-2u + 7v + 2w = 9",
)

# تنظیمات نمودار
ax.set_xlabel("u axis")
ax.set_ylabel("v axis")
ax.set_zlabel("w axis")
ax.set_title("Intersection of Planes Representing the System of Equations")

# نمایش
plt.show()
