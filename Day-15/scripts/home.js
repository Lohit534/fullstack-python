let food = JSON.parse(localStorage.getItem("food"));
if (food == null) food = [];

const displayFood = () => {
  const foodContainer = document.getElementById("food-container");
  foodContainer.innerHTML = "";
  food.forEach((element, index) => {
    const foodItem = document.createElement("div");
    foodItem.classList.add("item");
    foodItem.innerHTML = `
        <p>${index + 1}. ${element}</p>
        <select class="status">
            <option value="pending">Pending</option>
            <option value="done">Done</option>
        </select>
        `;

    const select = foodItem.querySelector(".status");
    select.addEventListener("change", (event) => {
      foodItem.style.backgroundColor =
        event.target.value == "done" ? "green" : "red";
    });

    if (select.value == "done") {
      foodItem.style.backgroundColor = "green";
    } else {
      foodItem.style.backgroundColor = "red";
    }

    foodContainer.append(foodItem);
  });
};

displayFood();

const button = document.getElementById("btn");
button.addEventListener("click", () => {
  const input = document.getElementById("input");
  if (input.value.trim() != "") {
    food.push(input.value);
    localStorage.setItem("food", JSON.stringify(food));
    input.value = "";
    displayFood();
  }
});
