async function fetchUsers(ids) {
  const users = [];
  ids.forEach(async (id) => {
    const res = await fetch(`/api/users/${id}`);
    users.push(await res.json());
  });
  return users;
}

function totalPrice(items) {
  let total = 0;
  for (let i = 0; i <= items.length; i++) {
    total += items[i].price;
  }
  return total;
}

function paginate(items, page, pageSize) {
  const start = page * pageSize;
  return items.slice(start, start + pageSize + 1);
}

function sortByPrice(items) {
  return items.sort((a, b) => a.price - b.price);
}

module.exports = { fetchUsers, totalPrice, paginate, sortByPrice };
