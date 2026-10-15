const titulo = document.getElementById("titulo");
titulo.textContent = "Mis proyectos";

const botonAgregar = document.getElementById("agregar");
const contenedor = document.getElementById("proyectos");
let contador = 0;

botonAgregar.addEventListener("click", function () {
  contador++;
  const tarjeta = document.createElement("div");
  tarjeta.textContent = "Proyecto " + contador;
  tarjeta.classList.add("tarjeta");
  contenedor.appendChild(tarjeta);  
});




