document.addEventListener('DOMContentLoaded', function () {
    // Radio - Área Perímetro
    let resultadoR = document.getElementById('resultR');
    let botonRadio = document.getElementById('buttonRadio');

    botonRadio.addEventListener('click', function() {
        let radio = parseFloat(document.getElementById('radio').value);
        resultadoR.innerHTML = 'Área: ' + 3.14 * (radio)**2 + 'm2 y la circunferencia: ' + 2*radio + 'πm.';

    });

    let resultadoTri = document.getElementById('resultTri');
    let botonTriangle = document.getElementById('buttonTriangle');

    botonTriangle.addEventListener('click', function() {
        let base = parseFloat(document.getElementById('base').value);
        let altura = parseFloat(document.getElementById('altura').value);
        resultadoTri.innerHTML = 'Área: ' + (base*altura)/2 + 'cm.';

    });

    let resultadoCuadrado = document.getElementById('resultCuadrado');
    let botonCuadrado = document.getElementById('buttonCuadrado');

    botonCuadrado.addEventListener('click', function() {
        let lado = parseFloat(document.getElementById('lado').value);
        resultadoCuadrado.innerHTML = 'Perímetro: ' + lado*4 + 'cm y el área: ' + lado**2 + 'cm2.';

    });

    x = 10;
    x = x+3;
    console.log(x);

    total = 50;
    console.log('- - - - - - - - - -');
    console.log(total-10);
    console.log(total+(total*0.21));
    console.log(total+20+(20*0.10));
    console.log('- - - - - - - - - -');
    total = total-10;
    total = total+(total*0.21);
    total = total+20+(20*0.10);
    console.log('Encadenando resultados: ' + total);

    y = 15;

    y_1 = y / 3;
    if(y%3==0){
        console.log('el resto entre 3 es 0');
    }

    y_2 = y / 5;
    if(y%5==0){
        console.log('el resto entre 5 es 0');
    }

    y_3 = y / 7;
    if(y%7==0){
        console.log('el resto entre 7 es 0');
    }

    y_4 = y / 10;
    if(y%10==0){
        console.log('el resto entre 10 es 0');
    }

    saldo = 100;

    saldo = saldo-(saldo*0.10);

    saldo = saldo - 15;

    saldo = saldo+(saldo*0.125);

    saldo = saldo / 2;
    
    saldo = saldo+(saldo*0.21);
    console.log('Saldo: ' + saldo);

    hola = 'Hola que tal?';
    if(hola.length>10){
        console.log('Es mayor que 10 caracteres');
    }

    

});