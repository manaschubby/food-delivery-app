# FOOD Delivery API


 This is a backend API for a food delivering app. This has various functionalities like User registartion, Outlet Registration, User ordering, order ready functionality and order deletion functionality.
 The Endpoints are not yet documented. Keep a lookout for this README.md for further updates to this API.

Installation:

1. Clone the repository from https://github.com/manaschubby/food-delivery-app.git
2. Install the required packages by running the command `pip install -r requirements.txt`
3. Create a database by running the command `python manage.py migrate`
4. Run the development server by running the command python manage.py runserver


Usage:

1. Register as a customer or restaurant owner.
2. Once registered, log in to your account.
3. If you are a customer, you can search for restaurants based on their name.
4. After finding a restaurant, you can view its menu and add items to your cart.
5. Go to your cart and click on the checkout button.
6. If you are a restaurant owner, you can add, update, or delete items from your menu. You can also view and manage orders that have been placed by customers.


Directory Structure:

`food_delivery_app` - Main Django application directory
`accounts` - Django application for handling user authentication and registration
`restaurants` - Django application for handling restaurant-related functionality, such as menu management
`orders` - Django application for handling order-related functionality, such as order placement and tracking


here are the URL endpoints for the Food Delivery App:

`/` - Home page, displays a list of all restaurants
`/restaurants/<int:restaurant_id>/` - Restaurant detail page, displays the menu for the specified restaurant
`/search/` - Search page, allows customers to search for restaurants by name or location
`/cart/` - Cart page, displays the items in the customer's cart and allows them to place an order
`/orders/` - Orders page, displays a list of orders placed by the customer
`/accounts/signup/` - Sign up page for customers and restaurant owners
`/accounts/login/` - Login page for customers and restaurant owners
`/accounts/logout/` - Logout page for customers and restaurant owners
`/restaurants/<int:restaurant_id>/menu/add/` - Add item page for restaurant owners, allows them to add items to their menu
`/restaurants/<int:restaurant_id>/menu/<int:item_id>/update/` - Update item page for restaurant owners, allows them to update items on their menu
`/restaurants/<int:restaurant_id>/menu/<int:item_id>/delete/` - Delete item page for restaurant owners, allows them to delete items from their menu
`/restaurants/<int:restaurant_id>/orders/` - Restaurant orders page, allows restaurant owners to view and manage orders placed by customers.

 ### THIS API WAS CREATED AS AN ASSIGNMENT FOR SMARTCAMPUS BPHC INDUCTIONS
