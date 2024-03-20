class SIRModel:
    def __init__(self, total_population, initial_infected, initial_recovered, beta, gamma):
        self.total_population = total_population
        self.infected = initial_infected
        self.recovered = initial_recovered
        self.susceptible = total_population - initial_infected - initial_recovered
        self.beta = beta
        self.gamma = gamma

    def calculate(self, time_step, steps):
        for i in range(steps):
            new_infected = time_step * self.beta * self.susceptible * self.infected / self.total_population
            new_recovered = time_step * self.gamma * self.infected

            self.susceptible -= new_infected
            self.infected += new_infected - new_recovered
            self.recovered += new_recovered

            print(f"Step {i}: Susceptible = {self.susceptible}, Infected = {self.infected}, Recovered = {self.recovered}")