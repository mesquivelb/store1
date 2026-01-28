from faker import Faker
import random
from app.models import User, Product, Category, Order, OrderItem, CartItem
from app.database import SessionLocal
from typing import List

fake = Faker()
db = SessionLocal()
products: List[Product]
categories: List[Category]
users: List[User]

# Ahora el IDE sabe que los elementos tienen .id, .price, .name, .full_name
p: Product
cat: Category
user: User

p = Product()
cat = Category()
user = User()
categories = []
category_names = ["Electrónica", "Ropa", "Hogar", "Deportes", "Juguetes"]
for name in category_names:
    c = Category(name=name)
    db.add(c)
    categories.append(c)
db.commit()

# Verificar que se crearon
for c in categories:
    print(f"Category {c.name} has id {c.id}")

# ------------------------------
# 2️⃣ Crear productos
# ------------------------------
products = []
for _ in range(50):
    p = Product(
        name=fake.word(),
        description=fake.sentence(),
        price=random.randint(50, 1000),
        category_id=random.choice(categories).id
    )
    db.add(p)
    products.append(p)
db.commit()

# Verificar que se crearon
print(f"✅ {len(products)} productos creados")

# ------------------------------
# 3️⃣ Crear usuarios
# ------------------------------
users = []
for _ in range(25):
    u = User(
        email=fake.email(),
        full_name=fake.name(),
        password="test123"
    )
    db.add(u)
    users.append(u)
db.commit()
print(f"✅ {len(users)} usuarios creados")

# ------------------------------
# 4️⃣ Crear cart items
# ------------------------------
for user in users:
    for _ in range(random.randint(1, 5)):
        product = random.choice(products)
        quantity = random.randint(1, 3)
        ci = CartItem(
            user_id=user.id,
            product_id=product.id,
            quantity=quantity
        )
        db.add(ci)
db.commit()
print("✅ CartItems creados")

# ------------------------------
# 5️⃣ Crear órdenes y order_items
# ------------------------------
for _ in range(30):
    user = random.choice(users)
    order = Order(user_id=user.id, total=0, status="pending")
    db.add(order)
    db.commit()  # Commit para que order.id exista

    total = 0
    for _ in range(random.randint(1, 5)):
        product = random.choice(products)
        quantity = random.randint(1, 3)
        oi = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=quantity
        )
        db.add(oi)
        total += product.price * quantity

    order.total = total
    db.commit()  # ✅ Commit final de la orden y sus items

print("✅ Base de datos poblada completamente para pruebas (Users, Categories, Products, CartItems, Orders, OrderItems)")


print("Ejemplo producto:", products[0].id, products[0].price)
print("Ejemplo categoría:", categories[0].id, categories[0].name)
print("Ejemplo usuario:", users[0].id, users[0].full_name)
