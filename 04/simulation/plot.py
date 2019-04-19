import numpy as np
import matplotlib.pyplot as plt

qs = np.load("angle_qs.npz.npy")

lme = np.load("length_me.npz.npy")
lmv = np.load("length_mv.npz.npy")
lms = np.sqrt(lmv) / lme

ame = np.load("angle_me.npz.npy")
amv = np.load("angle_mv.npz.npy")
ams = np.sqrt(amv) / ame

f = plt.figure(figsize=(6.4, 3.2))
plt.subplot(311)
plt.plot(qs, lme, "k")
plt.ylabel("E [m2]")
plt.subplot(312)
plt.plot(qs, lmv, "k")
plt.ylabel("V [m4]")
plt.subplot(313)
plt.plot(qs, lms, "k")
plt.ylabel("S / E [-]")
plt.xlabel("q2 [deg]")
f.subplots_adjust(left=0.18,
                  bottom=0.15,
                  top=0.99,
                  right=0.90,
                  wspace=0.20,
                  hspace=0.58)
f.savefig("length_plots.pdf")

f = plt.figure(figsize=(6.4, 3.2))
plt.subplot(311)
plt.plot(qs, ame, "k")
plt.ylabel("E [m2]")
plt.subplot(312)
plt.plot(qs, amv, "k")
plt.ylabel("V [m4]")
plt.subplot(313)
plt.plot(qs, ams, "k")
plt.ylabel("S / E [-]")
plt.xlabel("q2 [deg]")
f.subplots_adjust(left=0.18,
                  bottom=0.15,
                  top=0.99,
                  right=0.90,
                  wspace=0.20,
                  hspace=0.58)
f.savefig("angle_plots.pdf")

plt.show()
