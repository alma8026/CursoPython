// let nombre = prompt('Como te llamas?');
// alert('Hola ' + nombre)
let botonIva = document.getElementById('buttonIva');
let botonArea = document.getElementById('buttonArea');
let botonSeg = document.getElementById('buttonSeg');

botonIva.addEventListener('click', function() {
    let precio = parseFloat(document.getElementById('precio').value);
    let iva = parseFloat(document.getElementById('iva').value);
    let result = document.getElementById('result');

    let impuesto = precio * (iva / 100);
    console.log(impuesto)
    let total = precio + impuesto;
    console.log(precio)
    console.log('ads: ' + total);
    result.innerHTML = 'Resultado: ' + total;
});

botonArea.addEventListener('click', function (){
    let lado = parseFloat(document.getElementById('lado').value);
    let resultA = document.getElementById('resultA');
    let P = 4 * lado;
    let A = lado * lado;

    resultA.innerHTML = 'El area es: ' + A + '. Y el perimetro es: ' + P;
});

botonSeg.addEventListener('click', function (){
    let horas = Number.parseInt(document.getElementById('horas').value);
    let minutos = Number.parseInt(document.getElementById('minutos').value);
    let resultSeg = document.getElementById('resultSeg');

    let segundos = (horas*60*60) + (minutos*60);

    resultSeg.innerHTML = 'Son: ' + segundos + ' segundos.';
});