// Si le colocamos en el proyecto que ahora utilizaremos el type module entonces las importaciones AUN tenemos que colocar las extensiones porque sino lo tomara como si estuviesemos utilizando una libreria
import {dividir} from './funciones.js'

console.log('Hola desde el archivo principal')

const resultado = dividir(50,5)

console.log(resultado)