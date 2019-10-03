import importlib
import numpy.testing as npt

country = importlib.import_module('.03_country-subset', 'notebooks')

processed_data = "../data/processed/2019-10-03-winemag_Chile.csv"

def test_get_mean_price():
    mean_price = country.get_mean_price(processed_data)
    assert mean_price == 20.7865
    npt.assert_allclose(country.get_mean_price(processed_data), 20.787, rtol = 0.01)
    
#20.7865 is the correct answer so have to figure this out beforehand 
#npt used to make 'fluffier' and add tolerance to 0.01 decimal places

