console.log('Hola')

async function pedirProductos() {
    const solicitud = await fetch('http://127.0.0.1:5000/productos')

    console.log(solicitud.status)

    // O bien se usa el .text() o el .json() mas no se puede utilizar los dos a la vez
    // el text() se utiliza cuando el backend devuelve netamente texto 
    // const data = await solicitud.text() // es la informacion sin parsear (sin convertir a un formato legible en js)
    // cuando el backend devuelve diccionario 
    const data = await solicitud.json() // me da la informacion parseada para que JS la pueda entender
    console.log(data)
}

pedirProductos()