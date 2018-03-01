class PhoneBook:


    def __init__(self, contact_id = 1, contact_name = 'DC Dalin', contact_phone = '0712345678'):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.contact_phone = contact_phone

        self.contacts = []
        self.me = {'id': contact_id, 'name': contact_name, 'phone': contact_phone}
        self.contacts.append(self.me)

    def all_contacts(self):
        return self.contacts

    def add_contact(self):
        pass

    def show_contact(self):
        pass

    def edit_contact(self):
        pass

    def delete_contact(self):
        pass

        

user_1 = PhoneBook()

print(user_1.all_contacts())