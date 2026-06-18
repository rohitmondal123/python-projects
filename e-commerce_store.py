# ============ show products =============

def show_products(products):
    print("\n AVAILABLE PRODUCTS: : ")
    print("-" * 70)
    for pid, p in products.items():
        print(f"{pid:<3} | {p['name']:<20} | ${p['price']:<8.2f} | Stock: {p['quantity']}")
    print("-" * 70)

# =========== add to cart ==================


def add_to_cart(products,cart,product_id,quantity):
    if product_id in products and products[product_id]['quantity'] >= quantity:
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        products[product_id]['quantity'] -= quantity
        print(f"Added {quantity}     x {products[product_id]['name']} to the cart")
    else:
        print("Product not available in the stock or insufficient stock !...")

# ============ view cart ===========


def view_cart(products,cart):
    if not cart:
        print("\nYour cart is empty")
        return
    print("\n YOUR CART ---")
    total = 0
    print("-"*70)
    for pid,qty in cart.items():
        product = products[pid]
        cost = product['price'] * qty
        total += cost
        print(f"{product['name']:<20} × {qty:<3} @ ${product['price']:<8.2f} = ${total:>.2f}")
    print("-"*70)
    subtotal, discount, tax, grand = _totals()
    print(f"Cart Total Price : ${total}")
    if discount:
        print(f"Discount ({applied_code}) : -${discount:>.2f}")
    print(f"Tax {TAX_RATE*100:.0f}%    : ${tax:>.2f}")
    print(f"Total     : ${grand:>.2f}")



# ========= tax caculation =========

TAX_RATE = 0.10
def _totals():
    subtotal = sum(products[pid]['price'] * qty for pid, qty in cart.items())
    discount = subtotal * DISCOUNT_CODES.get(applied_code, 0) if applied_code else 0
    taxable  = max(subtotal - discount, 0)
    tax      = taxable * TAX_RATE
    grand    = taxable + tax
    return subtotal, discount, tax, grand


# ============ discount ==============


DISCOUNT_CODES = {
    "ROHIT2006": 0.10,
    "BRAINWARE"  : 0.05,
    "PYTHON":0.02
}
applied_code = None
def apply_discount(code):
    global applied_code
    code = code.upper()
    if code in DISCOUNT_CODES:
        applied_code = code
        print(f"Applied promo code '{code}' . ")
    else:
        print("Invalid or expired promo code.")


# ============= remove element from store =============

def remove_from_cart(pid, qty):
    if pid not in cart:
        print("That item is not in your cart.")
        return
    qty_to_remove = min(qty, cart[pid])
    cart[pid]     -= qty_to_remove
    if cart[pid] == 0:
        del cart[pid]
    products[pid]['quantity'] += qty_to_remove
    print(f"Removed {qty_to_remove} × {products[pid]['name']} from cart.")


# ============ checkout ==============

def checkout(products,cart):
    if not cart:
        print("Our cart is empty ! Please add item into the cart to be chectout .....")
        return
    subtotal, discount, tax, grand = _totals()
    print(f"Total amount payable    : ${grand:>.2f}")
    if input("Proceed to pay ? (Y/N) ").strip().lower() != 'y':
        print("Checkout cancelled.")
        return
    cart.clear()
    global applied_code
    applied_code = None
    print("Payment complete ........")
    print("THANK YOU FOR YOUR PURCHASE -------")

# ================= main =================

products = {
    1: {'name': 'Laptop',      'price': 999.99, 'quantity': 10},
    2: {'name': 'Smartphone',  'price': 499.99, 'quantity': 25},
    3: {'name': 'Headphones',  'price': 149.99, 'quantity': 50},
    4: {'name': 'Book',        'price': 19.99, 'quantity': 100},
    5: {'name': 'Tablet',      'price': 299.99, 'quantity': 30},
    6: {'name': 'Smartwatch',  'price': 199.99, 'quantity': 40},
    7: {'name': 'Keyboard',    'price': 49.99, 'quantity': 70},
    8: {'name': 'Mouse',       'price': 29.99, 'quantity': 80},
    9: {'name': 'Backpack',    'price': 59.99, 'quantity': 60},
    10: {'name': 'Bottle',    'price': 9.99, 'quantity': 200}
}

cart = {}

print("\n====== N1 CODEX STORE ======")
print("1: Show products")
print("2: Add to cart ")
print("3: view cart")
print("4: Checkout")
print("5: Apply Discount Code")
print("6: Remove From Cart")
print("7: Exit")

while True:
    choice = int(input("Enter your choice : "))
    if choice == 1:
        show_products(products)
    elif choice == 2:
        try:
            pid = int(input("Enter product id to add to the cart : "))
            qty = int(input("Enter quantity : "))
            add_to_cart(products,cart,pid,qty)
        except ValueError:
            print("Please enter valid option ....")
    elif choice == 3:
        view_cart(products,cart)
    elif choice == 4:
        checkout(products,cart)
    elif choice == 7:
        print("Thank you for visiting N1 CODEX STORE . GOODBYE !!")
        break
    elif choice == 5:
        apply_discount(input("Enter promo code : ").strip())
    elif choice == 6:
        pid = int(input("Enter product id to remove from the cart : "))
        qty = int(input("Enter quantity : "))
        remove_from_cart(pid,qty)
    else:
        print("Invalid choice .Enter valid choice (1 - 7) .....")