from data_clean import *

import time
import math


col = ['time_of_day', '1 AV L BMT', '103 ST 1 IRT',
       '103 ST 6 IRT', '14 ST 123FLM IRT', '14 ST-UNION SQ 456LNQRW IRT',
       '15 ST-PROSPECT FG IND', '2 AV F IND', '21 ST-QNSBRIDGE F IND',
       '23 ST 1 IRT', '23 ST 6 IRT', '23 ST CE IND', '23 ST NRW BMT',
       '28 ST 6 IRT', '3 AV L BMT', '33 ST 6 IRT',
       '34 ST-HERALD SQ BDFMNQRW BMT', '34 ST-HUDSON YD 7 IRT',
       '34 ST-PENN STA 123 IRT', '4 AV-9 ST DFGMNR IND',
       '42 ST-BRYANT PK BDFM7 IND', '47-50 STS ROCK BDFM IND',
       '49 ST NQRW BMT', '5 AV/53 ST EM IND', '5 AV/59 ST NQRW BMT',
       '5 AVE 7BDFM IRT', '50 ST 1 IRT', '50 ST CE IND', '51 ST 6 IRT',
       '57 ST-7 AV NQRW BMT', '59 ST COLUMBUS 1ABCD IRT', '6 AV FLM123 BMT',
       '7 AV FG IND', '72 ST 123 IRT', '77 ST 6 IRT', '8 AV ACEL BMT',
       '8 ST-NYU NRW BMT', '86 ST 1 IRT', '86 ST BC IND', '96 ST 123 IRT',
       '96 ST 6 IRT', '96 ST BC IND', '9TH STREET 1 PTH',
       'ATL AV-BARCLAY 2345BDNQR IRT', 'B\'WAY-LAFAYETTE BDFQ6 IND',
       'BEDFORD AV L BMT', 'BEDFORD-NOSTRAN G IND', 'BERGEN ST 23 IRT',
       'BLEECKER ST 6DF IRT', 'BOROUGH HALL 2345R IRT',
       'BOROUGH HALL R2345 BMT', 'BOWERY JZ BMT', 'BOWLING GREEN 45 IRT',
       'CANAL ST ACE IND', 'CARROLL ST FG IND', 'CATHEDRAL PKWY 1 IRT',
       'CHAMBERS ST 123 IRT', 'CHRISTOPHER ST 1 IRT', 'CHRISTOPHER ST 1 PTH',
       'CITY / BUS 1 PTH', 'CLARK ST 23 IRT', 'CLASSON AV G IND',
       'CLINTON-WASH AV C IND', 'CORTLANDT ST RNW BMT', 'COURT SQ 7 IRT',
       'DEKALB AV BDNQR BMT', 'EAST BROADWAY F IND', 'FLUSHING AV G IND',
       'FRANKLIN AV 2345S IRT', 'FRANKLIN ST 1 IRT', 'GRAHAM AV L BMT',
       'GRAND ARMY PLAZ 23 IRT', 'GRAND ST BD IND', 'GRAND ST L BMT',
       'GRD CNTRL-42 ST 4567S IRT', 'GREENPOINT AV G IND', 'HIGH ST AC IND',
       'HOYT-SCHER ACG IND', 'KINGSTON-THROOP C IND',
       'LEXINGTON AV/53 EM6 IND', 'LEXINGTON AV/63 F IND', 'MONTROSE AV L BMT',
       'MYRTLE AV JMZ BMT', 'MYRTLE-WILLOUGH G IND', 'NEVINS ST 2345 IRT',
       'PRESIDENT ST 25 IRT', 'PRINCE ST NRW BMT', 'QUEENSBORO PLZ 7NQW IRT',
       'SMITH-9 ST FG IND', 'SPRING ST 6 IRT', 'SPRING ST CE IND',
       'UNION ST R BMT', 'VERNON-JACKSON 7 IRT', 'WALL ST 23 IRT']
col = [ 'time_of_day', 'DELTA', '1 AV L BMT',
       '103 ST 1 IRT', '103 ST 6 IRT', '14 ST 123FLM IRT',
       '14 ST-UNION SQ 456LNQRW IRT', '15 ST-PROSPECT FG IND', '2 AV F IND',
       '21 ST-QNSBRIDGE F IND', '23 ST 1 IRT', '23 ST 6 IRT', '23 ST CE IND',
       '23 ST NRW BMT', '28 ST 6 IRT', '3 AV L BMT', '33 ST 6 IRT',
       '34 ST-HERALD SQ BDFMNQRW BMT', '34 ST-HUDSON YD 7 IRT',
       '34 ST-PENN STA 123 IRT', '4 AV-9 ST DFGMNR IND',
       '42 ST-BRYANT PK BDFM7 IND', '47-50 STS ROCK BDFM IND',
       '49 ST NQRW BMT', '5 AV/53 ST EM IND', '5 AV/59 ST NQRW BMT',
       '5 AVE 7BDFM IRT', '50 ST 1 IRT', '50 ST CE IND', '51 ST 6 IRT',
       '57 ST-7 AV NQRW BMT', '59 ST COLUMBUS 1ABCD IRT', '6 AV FLM123 BMT',
       '7 AV FG IND', '72 ST 123 IRT', '77 ST 6 IRT', '8 AV ACEL BMT',
       '8 ST-NYU NRW BMT', '86 ST 1 IRT', '86 ST BC IND', '96 ST 123 IRT',
       '96 ST 6 IRT', '96 ST BC IND', '9TH STREET 1 PTH',
       'ATL AV-BARCLAY 2345BDNQR IRT', 'B\'WAY-LAFAYETTE BDFQ6 IND',
       'BEDFORD AV L BMT', 'BEDFORD-NOSTRAN G IND', 'BERGEN ST 23 IRT',
       'BLEECKER ST 6DF IRT', 'BOROUGH HALL 2345R IRT',
       'BOROUGH HALL R2345 BMT', 'BOWERY JZ BMT', 'BOWLING GREEN 45 IRT',
       'CANAL ST ACE IND', 'CARROLL ST FG IND', 'CATHEDRAL PKWY 1 IRT',
       'CHAMBERS ST 123 IRT', 'CHRISTOPHER ST 1 IRT', 'CHRISTOPHER ST 1 PTH',
       'CITY / BUS 1 PTH', 'CLARK ST 23 IRT', 'CLASSON AV G IND',
       'CLINTON-WASH AV C IND', 'CORTLANDT ST RNW BMT', 'COURT SQ 7 IRT',
       'DEKALB AV BDNQR BMT', 'EAST BROADWAY F IND', 'FLUSHING AV G IND',
       'FRANKLIN AV 2345S IRT', 'FRANKLIN ST 1 IRT', 'GRAHAM AV L BMT',
       'GRAND ARMY PLAZ 23 IRT', 'GRAND ST BD IND', 'GRAND ST L BMT',
       'GRD CNTRL-42 ST 4567S IRT', 'GREENPOINT AV G IND', 'HIGH ST AC IND',
       'HOYT-SCHER ACG IND', 'KINGSTON-THROOP C IND',
       'LEXINGTON AV/53 EM6 IND', 'LEXINGTON AV/63 F IND', 'MONTROSE AV L BMT',
       'MYRTLE AV JMZ BMT', 'MYRTLE-WILLOUGH G IND', 'NEVINS ST 2345 IRT',
       'PRESIDENT ST 25 IRT', 'PRINCE ST NRW BMT', 'QUEENSBORO PLZ 7NQW IRT',
       'SMITH-9 ST FG IND', 'SPRING ST 6 IRT', 'SPRING ST CE IND',
       'UNION ST R BMT', 'VERNON-JACKSON 7 IRT', 'WALL ST 23 IRT']


def clean_data():
    print("Reading Data ...")
    mta_df = pd.read_csv("data/mta_turnstile/turnstile_170107.txt")
    mta_df = mta_df.append(pd.read_csv("data/mta_turnstile/turnstile_170114.txt"))
    mta_df = mta_df.append(pd.read_csv("data/mta_turnstile/turnstile_170121.txt"))
    mta_df = mta_df.append(pd.read_csv("data/mta_turnstile/turnstile_170128.txt"))

    bike_df = pd.read_csv("data/201701-citibike-tripdata.csv.zip")

    mta_loc = load_pickle('storage/mta_loc.pckl')

    print("Cleaning MTA Data...")
    mta_df = clean_mta(mta_df, mta_loc)
    print("Cleaning citibike Data...")
    bike_df = clean_citibike(bike_df)

    store_pickle('storage/bike_df.pckl', bike_df)
    store_pickle('storage/mta_df.pckl', mta_df)

def dummify(df):
    dummies = pd.get_dummies(df['zone'])
    df[dummies.columns] = dummies
    return df

def feature_engineering():
    bike_df = load_pickle('storage/test_bike.pckl')
    mta_df = load_pickle('storage/test_mta.pckl')

    agg_mta = mta_df.groupby(['zone', 'DATE', 'time_of_day'])['DELTA'].sum().reset_index()

    data = pd.merge(bike_df, mta_df, on=['zone', 'DATE', 'time_of_day'])
    grp = data.groupby(['zone', 'DATE', 'time_of_day'])

    df = grp['Bike ID'].count().reset_index()
    df = pd.merge(df, agg_mta, on=['zone', 'DATE', 'time_of_day'])
    df = dummify(df)

    return df

def randomforestmodel(df):
    print("Running Model...")
    df = df.sort_values('DATE')

    rows = df.shape[0]

    train = df.head(int(rows*0.8))
    test = df.tail(int(rows*0.2))

    rfrmodel = RandomForestRegressor(n_estimators=20, n_jobs=-1)
    reg = rfrmodel.fit(train[col], train['Bike ID'])

    training_accuracy = reg.score(train[col], train['Bike ID'])
    test_accuracy = reg.score(test[col], test['Bike ID'])

    log_error = mean_squared_log_error(test['Bike ID'], rfrmodel.predict(test[col]))

    print("############# based on standard predict ################")
    print("R^2 on training data: %0.4f" % (training_accuracy))
    print("R^2 on test data:     %0.4f" % (test_accuracy))
    print("log on test data:     %0.4f" % (log_error))

    y_test = test['Bike ID']
    y_pred = rfrmodel.predict(test[col])

    percent_error = (abs(y_pred - y_test + 1))/abs(y_test + 1)
    print(np.mean(percent_error))

    avg_error = (abs(y_pred - y_test + 1))
    print(np.mean(avg_error))

    return (percent_error, avg_error, test)

if __name__ == '__main__':
    start = time.time()

    # get_mta_loc()
    # clean_data()

    df = feature_engineering()
    randomforestmodel(df)

    print()
    print("Time:", time.time() - start)


