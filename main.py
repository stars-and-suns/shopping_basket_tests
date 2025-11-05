import item
import shoppingbasket as sb

tomatoSoup = item.Item("Tomato Soup", "200mL can", 0.70)
spaghetti = item.Item("Spaghetti", "500g pack", 1.10)
blackOlives = item.Item("Black Olives Jar", "200g Jar", 2.10)
mozzarella = item.Item("Mozzarella", "100g", 1.50)
gratedCheese = item.Item("Grated Cheese", "100g", 2.20)

my_basket = sb.ShoppingBasket()

my_basket.addItem(tomatoSoup, 4)
my_basket.addItem(blackOlives, 1)
my_basket.addItem(mozzarella, 2)
my_basket.addItem(tomatoSoup, 6)

my_basket.view()
