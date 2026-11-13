// Bug 4: deduplicate usernames without changing their first-seen order.
function uniqueUsernames(users) {
  const seen = new Set();
  const result = [];

  for (const user of users) {
    const normalized = user.trim().toLowerCase();
    if (!seen.has(normalized)) {
      seen.add(normalized);
      result.push(normalized);
    }
  }
  return result;
}

const incoming = [
  "Zara",
  " ali ",
  "ZARA",
  "Mina",
  "ALI",
];
console.log(uniqueUsernames(incoming));
module.exports = { uniqueUsernames };
