API provides the ability to record and receive information about organizations and they services

Use Admin part for creating/updatin/deleting organizations, services, districts, categories.

http://localhost:8000/admin/

Viewing the list of organizations displaying by district(GET)
http://localhost:8000/organizations/district_id

Example: http://localhost:8000/organizations/5

Viewing current organization(GET)

http://localhost:8000/organization/pk

Example: http://localhost:8000/organization/1

Viewing current service(GET)

http://localhost:8000/services/id

Example: http://localhost:8000/services/3/

Get the price between min_price and max_price values
GET /organizations/1/?min_price=280.0&max_price=500.0 HTTP/1.1

Example: http://localhost:8000/organizations/1/?min_price=280.0&max_price=500.0

Filtering by max price
GET /organizations/1/?max_price=45.0 HTTP/1.1

Example: http://localhost:8000/organizations/5/?max_price=45.0

Filtering by min price
GET /organizations/1/?min_price=30.0 HTTP/1.1

Example: http://localhost:8000/organizations/1/?min_price=280.0

Filter by service category in this organization with set district
GET /organizations/4/?category=appliances

Example:http://localhost:8000/organizations/4/?category=medicaments
        http://localhost:8000/organizations/4/?category=appliances

Search by organization name
GET /organizations/1/?search=MistrerBo

http://localhost:8000/organizations/1/?search=MistrerBo

Search by service name

http://localhost:8000/organizations/1/?search=Talenol