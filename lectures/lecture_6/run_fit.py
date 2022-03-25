from tagger import Tagger
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    ## script to read data ##

    x, y = ["Плавать", "Бегать", "Яблоко", "Тарелки"], ["VERB", "VERB", "NOUN", "NOUN"]
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)
    print(X_train, X_test, y_train, y_test)
    model = Tagger()
    model.fit(x, y)
    model.predict("Прыгать") # <-- "VERB", {"VERB": 0.7, "NOUN": 0.3}
    model.eval(x_test, y_test)
