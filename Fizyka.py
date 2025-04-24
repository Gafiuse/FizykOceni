import numpy as np
import matplotlib.pyplot as plt

# Wprowadzanie danych z walidacją
def get_positive_float(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value <= 0:
                print("Błąd: Wartości muszą być większe od zera. Spróbuj ponownie.")
            else:
                return value
        except ValueError:
            print("Błąd: Podaj poprawne liczby.")



# Wartości
omega = get_positive_float("Wprowadź prędkość kątową ω (rad/s²):")
A = get_positive_float("Wprowadź amplitudę A (m): ")
k = get_positive_float("Wprowadź współczynnik sztywności k (N/m): ")



# Obliczenia
f = omega / (2 * np.pi)       
T = 1 / f                     
E = 0.5 * k * A**2            



# Wyniki 
print("\n----- Wyniki -----")
print(f"Częstotliwość: {f:.3f} Hz")
print(f"Okres: {T:.3f} s")
print(f"Energia całkowita: {E:.3f} J")



# Obliczenia 
t = np.linspace(0, 2*T, 1000)
x = A * np.sin(omega * t)
v = A * omega * np.cos(omega * t)
a = -A * omega**2 * np.sin(omega * t)



# Wykresy
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle(f"Pełna analiza ruchu harmonicznego (ω = {omega:.2f} rad/s², A = {A:.2f} m)", fontsize=16)

# 1. x(t)
axs[0, 0].plot(t, x, color='blue')
axs[0, 0].set_title("Położenie x(t)")
axs[0, 0].set_xlabel("Czas t [s]")
axs[0, 0].set_ylabel("Położenie x [m]")
axs[0, 0].grid(True)

# 2. v(t)
axs[0, 1].plot(t, v, color='green')
axs[0, 1].set_title("Prędkość v(t)")
axs[0, 1].set_xlabel("Czas t [s]")
axs[0, 1].set_ylabel("Prędkość v [m/s]")
axs[0, 1].grid(True)

# 3. a(t)
axs[0, 2].plot(t, a, color='red')
axs[0, 2].set_title("Przyspieszenie a(t)")
axs[0, 2].set_xlabel("Czas t [s]")
axs[0, 2].set_ylabel("Przyspieszenie a [m/s²]")
axs[0, 2].grid(True)

# 4. v(x)
axs[1, 0].plot(x, v, color='purple')
axs[1, 0].set_title("Prędkość od polożenia v(x)")
axs[1, 0].set_xlabel("Położenie x [m]")
axs[1, 0].set_ylabel("Prędkość v [m/s]")
axs[1, 0].grid(True)

# 5. a(x)
axs[1, 1].plot(x, a, color='orange')
axs[1, 1].set_title("Przyspieszenie od polożenia a(x)")
axs[1, 1].set_xlabel("Położenie x [m]")
axs[1, 1].set_ylabel("Przyspieszenie a [m/s²]")
axs[1, 1].grid(True)

# 6. a(v)
axs[1, 2].plot(v, a, color='teal')
axs[1, 2].set_title("Przyspieszenie od prędkości a(v)")
axs[1, 2].set_xlabel("Prędkość v [m/s]")
axs[1, 2].set_ylabel("Przyspieszenie a [m/s²]")
axs[1, 2].grid(True)

# Wykresy
plt.tight_layout()
plt.show()
