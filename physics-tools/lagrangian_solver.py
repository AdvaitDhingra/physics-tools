import sympy as sp 

class lagrangian:
    def __init__(self, kinetic_energy, potential_energy):
        x, t, m, v = sp.symbols("x t m v")
        self.ekin = kinetic_energy
        self.epot = potential_energy
        self.lagrangian = f"{kinetic_energy} - {potential_energy}"
        left_side = str(sp.Derivative(self.lagrangian, v).doit()).replace("v", "a")
        self.law_of_motion = f"{left_side} = {sp.Derivative(self.lagrangian, x).doit()}"
    def return_law_of_motion(self):
        return self.law_of_motion


# Classical Example

l = lagrangian("0.5*m*v^2", "m*9.8*x")
print(l.return_law_of_motion())

