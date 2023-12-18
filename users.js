// Crear un array vacío para almacenar los usuarios
var users = [];

// Función para agregar un usuario al array
function addUser(username, password) {
  users.push({username: username, password: password});
}

// Agregar un usuario al array
addUser("usuario1", "contraseña1");

// Agregar otro usuario al array
addUser("usuario2", "contraseña2");

// Imprimir el array de usuarios en la consola
console.log(users);