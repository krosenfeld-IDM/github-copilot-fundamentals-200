public class SIRModel
{
    private double susceptible;
    private double infected;
    private double recovered;
    private double totalPopulation;
    private double beta;
    private double gamma;

    public SIRModel(double totalPopulation, double initialInfected, double initialRecovered, double beta, double gamma)
    {
        this.totalPopulation = totalPopulation;
        this.infected = initialInfected;
        this.recovered = initialRecovered;
        this.susceptible = totalPopulation - initialInfected - initialRecovered;
        this.beta = beta;
        this.gamma = gamma;
    }

    public void Calculate(double timeStep, int steps)
    {
        for (int i = 0; i < steps; i++)
        {
            double newInfected = timeStep * beta * susceptible * infected / totalPopulation;
            double newRecovered = timeStep * gamma * infected;

            susceptible -= newInfected;
            infected += newInfected - newRecovered;
            recovered += newRecovered;

            Console.WriteLine($"Step {i}: Susceptible = {susceptible}, Infected = {infected}, Recovered = {recovered}");
        }
    }
}
