from fixerio import Fixerio
import pandas as pd

fxrio = Fixerio(access_key='3401cd052e4ac3a55a8a9ea215b1ea8d')
ok = fxrio.latest()
currency = pd.DataFrame(ok)
currency.to_csv('currency.csv')
