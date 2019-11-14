# Organization-info-Rest-API

API provides the ability to record and receive information about organizations and they services.
In the admin you can use CRUD operations for organizations, services, districts, categories.

------------
## The following actions are available:

| Methods  | Actions  |Examples |
| ------------ | ------------ | ------------ |
| **GET** | The list of organizations displaying by district **/organizations/district_id** | **/organizations/5**|
| **GET** | Current organization **/organization/pk** | **/organization/1** |
| **GET** |Current service **/services/pk** | **/services/3/**|
| **GET** | Get the price between min_price and max_price values | **/organizations/1/?min_price=280.0&max_price=500.0**  |
| **GET** | Filtering by max price | **/organizations/1/?max_price=45.0** |
| **GET** |Filtering by min price | **/organizations/1/?min_price=30.0** |
| **GET** |Filter by service category in this organization with set district | **/organizations/4/?category=medicaments**|
| **GET** |Search by organization name MistrerBo | **/organizations/1/?search=MistrerBo** |
| **GET** |Search by service name Toolenol | **/organizations/1/?search=Toolenol** |
