function solve() {
  const addButtons = Array.from(document.querySelectorAll(".add-product"));
  const textarea = document.querySelector("textarea");
  const checkoutButton = document.getElementsByClassName("checkout")[0];

  let cart = [];
  let totalPrice = 0;

  for (const button of addButtons) {
    button.addEventListener("click", addButtonHandler);
  }
  checkoutButton.addEventListener("click", checkoutHandler);

  function addToCart(name, price) {
    cart.push({ name: name, price: price });
    totalPrice += price;
    textarea.value += `Added ${name} for ${price.toFixed(2)} to the cart.\n`;
  }

  function addButtonHandler(e) {
    const button = e.currentTarget;

    const tableRow = button.parentElement.parentElement;
    const nameEl = tableRow.querySelector(".product-title");
    const priceEl = tableRow.querySelector(".product-line-price");

    let name = nameEl.textContent;
    let price = Number(priceEl.textContent);

    addToCart(name, price);
  }

  function checkoutHandler() {
    let uniqueProducts = [...new Set(cart.map((product) => product.name))].join(
      ", "
    );
    textarea.value += `You bought ${uniqueProducts} for ${totalPrice.toFixed(
      2
    )}.`;

    addButtons.forEach((button) => (button.disabled = true));
    checkoutButton.disabled = true;
  }
}
