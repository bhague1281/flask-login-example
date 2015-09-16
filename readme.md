# Authentication with Flask

When using flask-login for authentication, here's the general workflow:

* install flask-login and flask-bcrypt
* create a LoginManager instance and add the app and login view (the name of the template you're using for login)
* define a user model inheriting from UserMixin (required for some default implementations of authentication methods)
* define a function for loading users (remember to include the user_loader decorator from your login manager)
* use the `login_user` function to log the user in (after ensuring that the user exists and the passwords match)
* bcrypt can be implemented using flask-bcrypt (see `generate_password_hash` and `check_password_hash`)
* use the `@login_required` decorator to require authentication for controller functions
* flask-login gives you some methods for checking a user's properties (whether it's an anonymous user, or if the user is authenticated)

For more info, see the documentation for flask-login [here](https://flask-login.readthedocs.org/en/latest/#your-user-class).