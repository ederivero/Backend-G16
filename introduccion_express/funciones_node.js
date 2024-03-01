function saludar(){
    return 'hola buenas!'
}

// Funcion anonima
// Solamente si es a funcion estara almacenada en una variable se podra utilizar la flecha o la palabra 'function'
const despedir = (nombre) => `Adios ${nombre}`


// No se puede hacer esto porque la function de tipo flecha SOLO funciona en el anonimato
// ayuda () => {}

// CALLBACK
// Es la llamada a una funcion dentro de un parametro de otra funcion
const publicarNotas = (nota, cb) => {
    if (nota > 10 ){
        cb(nota)
    }
    else{
        console.log('Estas jalado')
    }
}

publicarNotas(20,(nota)=> {
    console.log(`Esta aprobado con ${nota}`)
})


publicarNotas(20,(nota)=> {
    console.log('Oye ten cuidado te falta repasar!')
})