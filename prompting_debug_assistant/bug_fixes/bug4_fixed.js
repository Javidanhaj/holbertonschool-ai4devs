// Goal: Apply a percentage discount to each shopping cart item.

function applyDiscount(price, discountRate) {
  if (discountRate < 0 || discountRate > 1) {
    throw new Error("Discount must be between 0 and 1");
  }
  return price * (1 - discountRate);
}

const cart = [
  { name: "Keyboard", price: 100, discount: 0.10 },
  { name: "Mouse", price: 40, discount: 0.25 },
];

for (const item of cart) {
  const finalPrice = applyDiscount(item.price, item.discount);
  console.log(`${item.name}: $${finalPrice.toFixed(2)}`);
}
console.log("Expected final prices: $90.00 and $30.00");
