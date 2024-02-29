// Se realiza la importacion usando CommonJS
const {restar, sumar} = require('./funciones')

const resultadoSuma = sumar(10,20)
const resultadoResta = restar(50,40)

console.log(resultadoSuma)
console.log(resultadoResta)

console.log('Hola mundo')