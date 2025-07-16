class Bike:
    def __init__(self):
        self.models = ["Sports", "Cruiser", "Electric"]

    def show_models(self):
        print("Available Bike Models:")
        for model in self.models:
            print("\t", model)
