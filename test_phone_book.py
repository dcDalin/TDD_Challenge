import unittest

from phone_book import PhoneBook


class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.initPhoneBook = PhoneBook()

    def test_add_contact(self):
        response = self.initPhoneBook.add_contact('Dalin', 712876245)
        self.assertEqual(response, 'contact added')

    def test_check_phone_number_is_int(self):
        response = self.initPhoneBook.add_contact('Dalin', 'adfi')
        self.assertEqual(response, 'not a number')

    def test_phone_number_length_is_not_nine(self):
        response = self.initPhoneBook.add_contact('Dalin', 3456789)
        self.assertEqual(response, 'number short or long')

    def test_search_contact(self):
        '''Create some contacts before we search for them'''
        self.initPhoneBook.add_contact('Mike', 712872452)
        self.initPhoneBook.add_contact('Mwangi', 712876245)

        response = self.initPhoneBook.search_contact('Mwangi')
        self.assertEqual(response, [{'id': 2, 'name': 'Mwangi', 'phone': 712876245}])

    def test_contact_does_not_exist(self):
        '''Create some contacts before we search for them'''
        self.initPhoneBook.add_contact('Mike', 712872452)
        self.initPhoneBook.add_contact('Mwangi', 712876245)

        response = self.initPhoneBook.search_contact('Nancy')
        self.assertEqual(response, 'contact not found')

    def test_edit_phone_number(self):
        '''
            Create a contact before we can edit it
            Edit function takes in the name of the person and the new phone number
        '''
        self.initPhoneBook.add_contact('Ann', 712876245)

        response = self.initPhoneBook.edit_phone_number('Ann', 765356999)
        self.assertEqual(response, [{'id': 1, 'name': 'Ann', 'phone': 765356999}])

    def test_delete_contact(self):
        '''
            Create a contact that we will delete
        '''
        self.initPhoneBook.add_contact('Ann', 712676245)

        response = self.initPhoneBook.delete_contact('Ann')
        self.assertEqual(response, 'contact deleted')        

if __name__ == '__main__':
    unittest.main()