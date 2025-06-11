const head = document.getElementById("id1");
head.style.fontStyle = "italic";

const Div1 = document.getElementById("div1");
Div1.addEventListener("mouseover", () => {
  Div1.style.backgroundColor = "teal";
});
Div1.addEventListener("mouseout", () => {
  Div1.style.backgroundColor = "white";
});
const ADiv1 = document.getElementById("txt");
ADiv1.addEventListener("mouseover", () => {
  ADiv1.style.backgroundColor = "gray";
});
ADiv1.addEventListener("mouseout", () => {
  ADiv1.style.backgroundColor = "white";
});
const BDiv1 = document.getElementById("ema");
BDiv1.addEventListener("mouseover", () => {
  BDiv1.style.backgroundColor = "gray";
});
BDiv1.addEventListener("mouseout", () => {
  BDiv1.style.backgroundColor = "white";
});

const bt = document.getElementById("submit");
bt.addEventListener("dblclick", () => {
  bt.style.backgroundColor = "red";
});

document.querySelector(".div2").style.backgroundColor = "lightblue";

// const btn = document.addEventListener("click", () => {
//   alert("Welcome to my new world");
// });
let newDiv = document.createElement("div2");
newDiv.textContent = "Hello, this is a new div!";
document.body.appendChild(newDiv);
newDiv.style.color = "black";
newDiv.classList.add("div2");

const Color = ["lightgreen", "red", "blue"];

window.addEventListener("resize", () => {
  let randomIndex = Math.floor(Math.random() * Color.length);
  document.body.style.backgroundColor = Color[randomIndex];
});

window.addEventListener("scroll", () => {
  document.body.style.backgroundColor = "white";
});
