class PhoneBook:
    

    def __init__(self):
        '''Constructor method, will have a list of dictionaries i.e. phone numbers'''
        self.contacts = []

    def add_contact(self, contact_name, contact_phone, contact_id = '1'):
        '''instance variables, automatically add the next id to the next contact'''
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.contact_phone = contact_phone

        '''Check if phone number is an int'''
        if type(self.contact_phone) == int:
            '''Check if number is not equal to 9, meaning too long or short'''
            if len(str(self.contact_phone)) != 9:
                return 'number short or long'

            self.contact_id = len(self.contacts) + 1
            self.new = {'id': self.contact_id, 'name': self.contact_name, 'phone': contact_phone}
            self.contacts.append(self.new)
            return 'contact added'
        
        return 'not a number'
    def search_contact(self, search_contact):
        result = [element for element in self.contacts if element['name'] == search_contact]
        if result == []:
            return 'contact not found'
        return result

    def edit_phone_number(self, contact_name, new_phone_number):
        contact_to_edit = self.search_contact(contact_name)
        contact_to_edit[0]['phone'] = new_phone_number
        return contact_to_edit

    def delete_contact(self, contact_name):
        contact_to_delete = self.search_contact(contact_name)
        del contact_to_delete[0]
        return 'contact deleted'