document.addEventListener('DOMContentLoaded', function () {
    const resultado = document.getElementById('resultado'); // Elemento donde se muestra el resultado
    const botones = document.querySelectorAll('#calculadora button'); // Todos los botones de la calculadora

    botones.forEach(boton => {
        boton.addEventListener('click', function() {
            if (this.id === 'clear') {
                resultado.value = ''; // Limpiar todo
                return;
            }

            if (this.classList.contains('operacion')) {
                if (this.id === 'igual') {
                    // Calcular resultado
                    try {
                        resultado.value = eval(resultado.value);
                    } catch (e) {
                        resultado.value = 'Error'; // Manejar error en caso de una operación inválida
                    }
                } else {
                    resultado.value += this.textContent; // Agregar operador al resultado
                }
            } else {
                resultado.value += this.textContent; // Agregar número o punto al resultado
            }
        });
    });
});