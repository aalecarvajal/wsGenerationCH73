const titulo = document.querySelector("#titulo");
titulo.textContent = "Mis proyectos";

const botonAgregar = document.querySelector("#agregar");
const contenedor = document.querySelector("#proyectos");
let contador = 0;

botonAgregar.addEventListener("click", function () {
  contador++;
  const tarjeta = document.createElement("div");
  tarjeta.textContent = "Proyecto " + contador;
  tarjeta.classList.add("tarjeta");
  contenedor.appendChild(tarjeta);  
});

const botonTema = document.querySelector("#tema");
const guardado = localStorage.getItem("tema");

if (guardado === "oscuro") {
  document.body.classList.add("oscuro");
}

botonTema.addEventListener("click", () => {
  document.body.classList.toggle("oscuro");
  const activo = document.body.classList.contains("oscuro");
  localStorage.setItem("tema", activo ? "oscuro" : "claro");
});
