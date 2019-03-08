#
# (c) 2018 Last Update from Infoline
#

import csv

bbs_path = '/u01/bbs/data/'
fname = 'zenpho.csv' # Change to source csv file
dbname = bbs_path + 'zenpho.db' # Change to target sqlite db

contacts = []

try:
  from io import BytesIO
except ImportError: # Python < 2.6
  from StringIO import StringIO as BytesIO

with open(fname, 'rb') as binf:
  c = binf.read().decode('utf-16').encode('utf-8')
for line in csv.reader(BytesIO(c)):
  contacts.append((list(line)))

#
# DEBUG
#
#print (contacts)

import sqlite3

con = sqlite3.connect(dbname)
con.text_factory="UTF-8"
cur = con.cursor()
cur.execute("""
create table contacts (
first_name,
given_name,
additional_name,
family_name,
yomi_name,
given_name_yomi,
additional_name_yomi,
family_name_yomi,
name_prefix,
name_suffix,
initials,
nickname,
short_name,
maiden_name,
birthday,
gender,
location,
billing_information,
directory_server,
mileage,
occupation,
hobby,
sensitivity,
priority,
subject,
notes,
group_membership,
email_1_type,
email_1_value,
email_2_type,
email_2_value,
email_3_type,
email_3_value,
email_4_type,
email_4_value,
im_1_type,
im_1_service,
im_1_value,
phone_1_type,
phone_1_value,
phone_2_type,
phone_2_value,
phone_3_type,
phone_3_value,
phone_4_type,
phone_4_value,
address_1_type,
address_1_formatted,
address_1_street,
address_1_city,
address_1_po_box,
address_1_region,
address_1_postal_code,
address_1_country,
address_1_extended_address,
address_2_type,
address_2_formatted,
address_2_street,
address_2_city,
address_2_po_box,
address_2_region,
address_2_postal_code,
address_2_country,
address_2_extended_address,
organization_1_type,
organization_1_name,
organization_1_yomi_name,
organization_1_title,
organization_1_department,
organization_1_symbol,
organization_1_location,
organization_1_job_description,
website_1_type,
website_1_value,
website_2_type,
website_2_value,
custom_field_1_type,
custom_field_1_value text
);
""")

cur.executemany("""insert into contacts (
first_name,
given_name,
additional_name,
family_name,
yomi_name,
given_name_yomi,
additional_name_yomi,
family_name_yomi,
name_prefix,
name_suffix,
initials,
nickname,
short_name,
maiden_name,
birthday,
gender,
location,
billing_information,
directory_server,
mileage,
occupation,
hobby,
sensitivity,
priority,
subject,
notes,
group_membership,
email_1_type,
email_1_value,
email_2_type,
email_2_value,
email_3_type,
email_3_value,
email_4_type,
email_4_value,
im_1_type,
im_1_service,
im_1_value,
phone_1_type,
phone_1_value,
phone_2_type,
phone_2_value,
phone_3_type,
phone_3_value,
phone_4_type,
phone_4_value,
address_1_type,
address_1_formatted,
address_1_street,
address_1_city,
address_1_po_box,
address_1_region,
address_1_postal_code,
address_1_country,
address_1_extended_address,
address_2_type,
address_2_formatted,
address_2_street,
address_2_city,
address_2_po_box,
address_2_region,
address_2_postal_code,
address_2_country,
address_2_extended_address,
organization_1_type,
organization_1_name,
organization_1_yomi_name,
organization_1_title,
organization_1_department,
organization_1_symbol,
organization_1_location,
organization_1_job_description,
website_1_type,
website_1_value,
website_2_type,
website_2_value,
custom_field_1_type,
custom_field_1_value
) values (
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?,
?
);""", contacts)
con.commit()
con.close()

