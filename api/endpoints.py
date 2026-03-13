PRODUCTS = "/products"
USERS = "/users"
CARTS = "/carts"

LOGIN = "/auth/login"
CATEGORIES = "/products/categories"


def PRODUCT_BY_ID(product_id):
    return f"/products/{product_id}"


def USER_BY_ID(user_id):
    return f"/users/{user_id}"


def CART_BY_ID(cart_id):
    return f"/carts/{cart_id}"