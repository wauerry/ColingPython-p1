class Tagger:

    def __init__(self):
        pass

    def fit(self, x, y):
        pass

    def predict(self, token):
        tag = None
        return tag


print(__name__)

x, y = ["Плавать", "Бегать", "Яблоко", "Тарелки"], ["VERB", "VERB", "NOUN", "NOUN"]

print(x, y)
model = Tagger()
# model.fit(x, y)
# model.predict("Прыгать") # <-- "VERB", {"VERB": 0.7, "NOUN": 0.3}
# model.eval(x_test, y_test)
