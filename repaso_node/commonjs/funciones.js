function sumar(numero1, numero2){
    return numero1 + numero2
}

function restar(numero1, numero2){
    return numero1 - numero2
}


// Se realiza la exportacion usando CommonJs
module.exports = {
    sumar: sumar,
    restar
}