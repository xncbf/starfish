from settings import ACCESS_TOKEN, SECRET_KEY
from coinone.account import Account
from pprint import pprint

if __name__ == "__main__":
    my = Account(ACCESS_TOKEN, SECRET_KEY)

    # query account informations
    pprint(my.info())
    pprint(my.balance())
    pprint(my.daily_balance())
    # pprint(my.deposit_address())
    # pprint(my.virtual_account())

    #  complete orders
    # pprint(my.complete_orders())       # query for BTC by default
    pprint(my.complete_orders('XRP'))  # query for ETH
    # try:
    #     pprint(my.complete_orders('bbb'))  # will raise error
    # except Exception as e:
    #     print(e.args)

    # make some insane orders, and cancel them
    # will throw error if you have not enough balance
    my.buy(price=100, qty=1.000, currency='XRP')
    my.buy(price=100, qty=2.000, currency='XRP')
    my.sell(price=1000, qty=3.000, currency='XRP')

    print('made 3 orders')
    orders = my.orders()
    pprint(orders)
    my.cancel(**orders[-1])  # cancel the last one
    print('canceled last one')
    pprint(my.orders())
    my.cancel()              # will cancel all orders by default
    print('canceled remaining')
    pprint(my.orders())
