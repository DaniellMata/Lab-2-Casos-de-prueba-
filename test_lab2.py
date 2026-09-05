import logging
import ecommerce_form

logging.basicConfig(
    level = logging.DEBUG,
    filename = 'test.log',
    filemode = 'w'
)

def test_item_invalid():
    logging.info('TEST CASE 1: RF1(NEGATIVE)')

    system = ecommerce_form.OnlinePurchase()
    
    cart = {
        'Laptop' : 0,
        'Mouse' : 2
    }
    coupon = 'DISCOUNT10'
    address = 'Av. Patria'

    output = system.process_purchase(cart, coupon, address)
    logging.info(f'The purchase result is:{output}')

    assert 'greater than 0' in output 

def test_ivalid_coupon():
    logging.info('TEST CASE 2: RF3(NEGATIVE)')

    system = ecommerce_form.OnlinePurchase()
    
    cart = {
        'Laptop' : 1,
        'Mouse' : 2
    }
    coupon = 'DISCOUNT30'
    address = 'Av. Patria'

    output = system.process_purchase(cart, coupon, address)
    logging.info(f'The purchase result is:{output}')

    assert 'code is not valid' in output     

def test_check_discount():
    logging.info('TEST CASE 3: RF9(POSITIVE)')

    system = ecommerce_form.OnlinePurchase()
    
    cart = {
        'Laptop' : 1,
        'Mouse' : 2
    }
    coupon = 'DISCOUNT10'
    address = 'Av. Patria'

    output = system.process_purchase(cart, coupon, address)
    logging.info(f'The purchase result is:{output}')

    assert '990' in output   


if __name__ == '__main__':

    logging.info('YO chat')


