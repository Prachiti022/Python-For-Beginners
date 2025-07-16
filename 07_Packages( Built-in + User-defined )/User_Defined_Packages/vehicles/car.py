class Car:
    def __init__(self):
        self.models = ["Sedan", "SUV", "Hatchback"]

    def show_models(self):
        print("Available Car Models:")
        for model in self.models:
            print("\t", model)
