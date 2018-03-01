class PhoneBook:
    

    def __init__(self):
        '''Constructor method, will have a list of dictionaries i.e. phone numbers'''
        self.contacts = []

    def search_contact_name(self, search_contact):
        '''Search for contacts'''
        result = [element for element in self.contacts if element['name'] == search_contact]
        if result == []:
            return False
        return result
    
    def search_contact_phone(self, search_contact):
        '''Search for contacts'''
        result = [element for element in self.contacts if element['phone'] == search_contact]
        if result == []:
            return False
        return result

    def phone_number_exists(self, search_phone_number):
        '''Check if phone number already exists'''
        for find_contact in self.contacts:
            if find_contact['phone'] == search_phone_number:
                return True
                break;
        return False 

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
            
            '''Check if phone number exists'''
            if self.phone_number_exists(self.contact_phone):
                return 'phone number exists'

            self.contact_id = len(self.contacts) + 1
            self.new = {'id': self.contact_id, 'name': self.contact_name, 'phone': contact_phone}
            self.contacts.append(self.new)
            return 'contact added'
        
        return 'not a number'

    def show_all_contacts(self):
        return self.contacts

    def edit_phone_number(self, contact_name, new_phone_number):
        if self.search_contact_phone:
            contact_to_edit = self.search_contact_name(contact_name)
            contact_to_edit[0]['phone'] = new_phone_number
            return contact_to_edit
        return 'Contact does not exist'

    def delete_contact(self, contact_name):
        contact_to_delete = self.search_contact_name(contact_name)
        del contact_to_delete[0]
        return 'contact deleted'

user = PhoneBook()

user.add_contact('dalo', 838238382)
user.add_contact('maggie', 238383283)

print(user.delete_contact('dalo'))