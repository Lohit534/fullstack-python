const getData = async () => {
  try {
    let response = await fetch("https://jsonplaceholder.typicode.com/todos");
    let data = await response.json();
    localStorage.setItem("data", JSON.stringify(data));

    const container = document.getElementById("container");
    container.innerHTML = "";

    data.forEach((item) => {
      const todoItem = document.createElement("p");
      todoItem.textContent = item.title;
      todoItem.classList.add(item.completed ? "green" : "red");

      container.appendChild(todoItem);
    });
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

getData();
