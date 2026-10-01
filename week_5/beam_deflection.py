def deflection(length, load, modulus_elasticity, moment_inertia):
    return (load * length ** 3) / (3 * modulus_elasticity * moment_inertia)