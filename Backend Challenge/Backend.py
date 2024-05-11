def update_shopping_cart(cart, action):
    # __define-ocg__ This function updates the shopping cart based on user actions.
    varOcg = "quantity" if action["type"] in ["add", "change"] else None
    if action["type"] == "add":
        if action["product_id"] in cart:
            cart[action["product_id"]] += action.get(varOcg, 1)
        else:
            cart[action["product_id"]] = action.get(varOcg, 1)
    elif action["type"] == "remove":
        if action["product_id"] in cart:
            if action.get(varOcg, 1) >= cart[action["product_id"]]:
                del cart[action["product_id"]]
            else:
                cart[action["product_id"]] -= action.get(varOcg, 1)
    elif action["type"] == "change":
        if action["product_id"] in cart:
            cart[action["product_id"]] = action.get(varOcg, 1)
    return cart

# Example usage:
cart = {
    "product_1": 2,
    "product_2": 1
}

action = {
    "type": "add",
    "product_id": "product_3",
    "quantity": 3
}

print(update_shopping_cart(cart, action))
