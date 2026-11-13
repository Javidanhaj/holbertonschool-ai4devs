// Bug 3: return only products cheaper than or equal to a price limit.
function filterByPrice(products, maxPrice) {
  if (typeof maxPrice !== "number" || maxPrice < 0) {
    throw new Error("maxPrice must be a non-negative number");
  }

  const results = [];
  for (const product of products) {
    if (product.price <= maxPrice) {
      results.push(product);
    }
  }
  return results;
}

const items = [
  { name: "Notebook", price: 5 },
  { name: "Pen", price: 2 },
  { name: "Bag", price: 25 },
];
console.log(filterByPrice(items, 5));
module.exports = { filterByPrice };
