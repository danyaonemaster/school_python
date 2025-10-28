from task import Restaurant

restaurant = Restaurant("Goha", "Chinese")

def test_describe_restaurant(capsys):

    restaurant.describe_restaurant()

    res = capsys.readouterr().out.strip()

    assert res == "Name: Goha, Cuisine type: Chinese"


def test_open_restaurant(capsys):

    restaurant.open_restaurant()

    res = capsys.readouterr().out.strip() #takes the output of the last print

    assert res == "The restaurant \"Goha\" is open"
