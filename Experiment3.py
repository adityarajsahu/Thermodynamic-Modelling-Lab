from scipy.integrate import quad 

standard_enthalpy_Al = 1
standard_enthalpy_CO = 1
standard_enthalpy_Al2O3 = 1
standard_enthalpy_C = 1

temp = float(input("Enter the temperature of the reaction: "))
specific_heat_capacity_Al = float(input("Enter the Specific Heat Capacity of Aluminium: "))
specific_heat_capacity_CO = float(input("Enter the Specific Heat Capacity of Carbon Monoxide: "))
specific_heat_capacity_Al2O3 = float(input("Enter the Specific Heat Capacity of Aluminium Oxide: "))
specific_heat_capacity_C = float(input("Enter the Specific Heat Capacity of Carbon: "))

def func(x):
    return (2 * specific_heat_capacity_Al) + (3 * specific_heat_capacity_CO) - (specific_heat_capacity_Al2O3) - (3 * specific_heat_capacity_C)

latent_heat = (2 * standard_enthalpy_Al) + (3 * standard_enthalpy_CO) - (standard_enthalpy_Al2O3) - (3 * standard_enthalpy_C) + quad(func, 298, temp)[0]
print("Latent heat of Aluminium at {} K = {}".format(temp, latent_heat))
