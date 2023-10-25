# init_db.py

from devices import db, app
from devices.models import Device

app.app_context().push()
# Create the database and tables
db.create_all()

# Sample data
sample_data = [
    ('Workstation-01', 'Desktop', 'Office-A'),
    ('Laptop-01', 'Laptop', 'Home-B'),
    ('Server-01', 'Server', 'Datacenter-C'),
    ('Printer-01',	'Printer',	'Office-A'),
    ('Mobile-01',	'Mobile Device',	'Warehouse-D'),
    ('Workstation-02',	'Desktop',	'Office-B'),
    ('Laptop-02', 'Laptop', 'Home-A'),
    ('Server-02', 'Server', 'Datacenter-C'),
    ('Printer-02',	'Printer',	'Office-A'),
    ('Mobile-02',	'Mobile Device',	'Warehouse-D'),
    ('Workstation-03',	'Desktop',	'Office-C'),
    ('Laptop-03', 'Laptop', 'Home-A'),
    ('Server-03', 'Server', 'Datacenter-D'),
    ('Printer-03',	'Printer',	'Office-B'),
    ('Mobile-03',	'Mobile Device',	'Warehouse-E'),
    ('Workstation-03',	'Desktop',	'Office-C'),
    ('Laptop-04', 'Laptop', 'Home-C'),
    ('Server-04', 'Server', 'Datacenter-E'),
    ('Printer-04',	'Printer',	'Office-D'),
    ('Mobile-04',	'Mobile Device',	'Warehouse-F'),


]

# Populate the Devices table
for i,device_data in enumerate(sample_data):
    device = Device(DeviceID=i+1, DeviceName=device_data[0],
                    DeviceType=device_data[1], DeviceLocation=device_data[2])
    db.session.add(device)

db.session.commit()
