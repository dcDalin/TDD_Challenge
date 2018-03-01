contacts = [{'phone': 712872452, 'id': 1, 'name': 'Nancy'}, {'phone': 712876245, 'id': 2, 'name': 'Mwangi'}]

for contact in contacts:
    if contact['name'] == 'Nancy':
        print 'Found the wanker'
        break;
    print contact['name']