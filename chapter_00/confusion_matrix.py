# Calculating the different binomial confusion matrices.
# This only works when we know the total population, population positive rate, sensitivity, and specifity)

class ConfusionMatrix:

    def __init__(self, page, total_population, population_positive_rate, sensitivity, specificity):
        self.page = page
        self.total_population = total_population
        self.population_positive_rate = population_positive_rate
        self.sensitivity = sensitivity
        self.specificity = specificity

    def population_positive(self):
        return self.total_population * self.population_positive_rate

    def population_negative(self):
        return self.total_population * (1 - self.population_positive_rate)

    def true_positive(self):
        return self.population_positive() * self.sensitivity

    def false_negative(self):
        return self.population_positive() * (1 - self.sensitivity)

    def false_positive(self):
        return self.population_negative() * (1 - self.specificity)

    def true_negative(self):
        return self.population_negative() * self.specificity

    def chance_if_tested_positive_of_actually_being_positive(self):
        return 100 * self.true_positive() / (self.true_positive() + self.false_positive())

    def chance_if_tested_negative_of_actually_being_negative(self):
        return 100 * self.true_negative() / (self.true_negative() + self.false_negative())

    def print_details(self):
        citpoabp = self.chance_if_tested_positive_of_actually_being_positive()
        citnoabn = self.chance_if_tested_negative_of_actually_being_negative()

        print(f"This confusion matrix on page {self.page} has a population of {self.total_population}")
        print(f"Positive rate of {self.population_positive_rate * 100}%")
        print(f"Sensitivity rate of {self.sensitivity * 100}%")
        print(f"Specificity rate of {self.specificity * 100}%")
        print(f"Confusion Matrix:")
        print(f"True Positives: {self.true_positive():.0f}")
        print(f"False Positives: {self.false_positive():.0f}")
        print(f"False Negatives: {self.false_negative():.0f}")
        print(f"True Negatives: {self.true_negative():.0f}")
        print(f"The chance of testing positive and actually being positive is {citpoabp:.2f}%.")
        print(f"The chance of testing negative and actually being negative is {citnoabn:.2f}%.")
        print("")


# First one on page 8.
confusion_matrix_1 = ConfusionMatrix("8 (First one)", 100000.0, 0.01, 0.80, 0.90)
confusion_matrix_1.print_details()

# Second one on page 8.
confusion_matrix_2 = ConfusionMatrix("8 (Second one)", 100000.0, 0.10, 0.80, 0.90)
confusion_matrix_2.print_details()

# Page 11.
confusion_matrix_3 = ConfusionMatrix("11", 1000000.0, 0.03, 0.95, 0.95)
confusion_matrix_3.print_details()

# Page 13.
confusion_matrix_4 = ConfusionMatrix("13", 1000000.0, 0.001, 0.99, 0.99)
confusion_matrix_4.print_details()