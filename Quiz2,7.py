import pandas
import pandasql

def filter_by_regular(filename):

    turnstile_data = pandas.read_csv(filename)

    a = """ SELECT * FROM turnstile_data WHERE DESCn ='REGULAR' """

    #removed q.low() as the value in the tables are upper case; Unless we transform all of them to lower case
    turnstile_data = pandasql.sqldf(q, locals())
    turnstile_data = pandas.read_csv(filename)

    a = """ SELECT * FROM turnstile_data WHERE DESCn ='REGULAR' """

    turnstile_data = pandasql.sqldf(a, locals())

    return turnstile_data
