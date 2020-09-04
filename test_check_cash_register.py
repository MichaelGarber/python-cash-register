from check_cash_register import  check_cash_register

def test_check_cash_register():
        assert (check_cash_register(19.5, 20,[['PENNY', 1.01], ['NICKEL', 2.05], ['DIME', 3.1], ['QUARTER', 4.25], ['ONE', 90],['FIVE', 55], ['TEN', 20], ['TWENTY', 60], ['ONE HUNDRED', 100]]) == {'status': 'OPEN', 'change': [['QUARTER', 0.5]]})
        assert (check_cash_register(3.26, 100,[['PENNY', 1.01], ['NICKEL', 2.05], ['DIME', 3.1], ['QUARTER', 4.25], ['ONE', 90],['FIVE', 55], ['TEN', 20], ['TWENTY', 60], ['ONE HUNDRED', 100]]) == {'status': 'OPEN','change': [['TWENTY', 60], ['TEN', 20], ['FIVE', 15], ['ONE', 1], ['QUARTER', 0.5], ['DIME', 0.2],['PENNY', 0.04]]})
        assert (check_cash_register(19.5, 20, [['PENNY', 0.01], ['NICKEL', 0], ['DIME', 0], ['QUARTER', 0], ['ONE', 0],['FIVE', 0], ['TEN', 0], ['TWENTY', 0], ['ONE HUNDRED', 0]]) == {'status': 'INSUFFICIENT_FUNDS', 'change': []})
        assert (check_cash_register(19.5, 20, [['PENNY', 0.01], ['NICKEL', 0], ['DIME', 0], ['QUARTER', 0], ['ONE', 1],['FIVE', 0], ['TEN', 0], ['TWENTY', 0], ['ONE HUNDRED', 0]]) == {'status': 'INSUFFICIENT_FUNDS', 'change': []})
        assert (check_cash_register(19.5, 20, [['PENNY', 0.5], ['NICKEL', 0], ['DIME', 0], ['QUARTER', 0], ['ONE', 0],['FIVE', 0], ['TEN', 0], ['TWENTY', 0], ['ONE HUNDRED', 0]]) == {                    'status': 'CLOSED','change': [['PENNY', 0.5], ['NICKEL', 0], ['DIME', 0], ['QUARTER', 0], ['ONE', 0], ['FIVE', 0],['TEN', 0], ['TWENTY', 0], ['ONE HUNDRED', 0]]})
        print("Code is correct")