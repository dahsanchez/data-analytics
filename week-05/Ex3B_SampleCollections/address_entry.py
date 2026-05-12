contact_info = {
    'name': 'Dahlia Sanchez',
    'address': '22270 S Garden Ave',
    'city': 'Hayward',
    'state':'CA',
    'zip':'94541'
}
print(f"""
{contact_info['name']}
{contact_info['address']}
{contact_info['city']}
{contact_info['state']}
{contact_info['zip']}
""")

del contact_info['name']

full_name = {
    'first_name': 'Dahlia',
    'last_name':'Sanchez'
    }

full_name.update({
    'honorific': 'Ms.'
})

contact_info.update({
    'full_name': full_name
})

print(f"""
{contact_info['full_name']['honorific']}{contact_info['full_name']['first_name']} {contact_info['full_name']['last_name']}
{contact_info['address']}
{contact_info['city']}
{contact_info['state']}
{contact_info['zip']}
""")