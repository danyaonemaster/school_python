from objects_classes.task_01_01_restaurant.task import Restaurant

gohas_restaurant = Restaurant('goha', 'Asia')
jones_restaurant = Restaurant('jone', 'Asia')
garys_restaurant = Restaurant('gary', 'Asia')

def test_gohas_restaurant(capsys):

    gohas_restaurant.describe_restaurant()

    res = capsys.readouterr().out.strip()

    assert res == "Name: goha, Cuisine type: Asia"

def test_jones_restaurant(capsys):

    jones_restaurant.describe_restaurant()

    res = capsys.readouterr().out.strip()

    assert res == "Name: jone, Cuisine type: Asia"

def test_garys_restaurant(capsys):

    garys_restaurant.describe_restaurant()

    res = capsys.readouterr().out.strip()

    assert res == "Name: gary, Cuisine type: Asia"