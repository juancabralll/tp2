const $ = (id) => document.getElementById(id)
const lista = $("lista")
const tareas = $("tareas")

const obtenerDatos = async () => {
  const respuesta = await fetch("https://jsonplaceholder.typicode.com/users")
  console.log(respuesta)
  if (respuesta.ok) {
    const data = await respuesta.json()
    console.log(data)
    data.forEach((usuario) => {
      const item = document.createElement("li")
      item.innerHTML = `${usuario.id} - ${usuario.name} - ${usuario.username} - ${usuario.email} - ${usuario.website}`
      item.appendChild(btnVerTareas(usuario.id, usuario.name))
      lista.appendChild(item)
    })
  }
}

const btnVerTareas = (userId, userName) => {
  const btn = document.createElement("button")
  btn.innerHTML = "Ver tareas"
  btn.addEventListener("click", async () => {
    tareas.innerHTML = `Tareas de ${userName}`
    const res = await fetch(
      `https://jsonplaceholder.typicode.com/users/${userId}/todos`
    )
    if (res.ok) {
      const data = await res.json()
      data.forEach((tarea) => {
        const item = document.createElement("li")
        if (tarea.completed) {
          item.style.color = "green"
        } else {
          item.style.color = "red"
        }
        item.innerHTML = `${tarea.id} - ${tarea.title} - ${
          tarea.completed ? "Completado" : "Pendiente..."
        }`
        tareas.appendChild(item)
      })
    }
  })

  return btn
}
obtenerDatos()
