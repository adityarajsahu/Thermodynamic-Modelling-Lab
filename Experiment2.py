from scipy.integrate import quad

freezing_point = 933
latent_heat_at_freezing_point = 387.4

temp = float(input("Enter the temperature: "))
def func(x):
    return (0.4103) - (4.856 * (10 ** (-4))) * x

latent_heat_at_given_temp = latent_heat_at_freezing_point - quad(func, temp, freezing_point)[0]

print("Latent Heat at {} K = {} kJ".format(temp, latent_heat_at_given_temp))