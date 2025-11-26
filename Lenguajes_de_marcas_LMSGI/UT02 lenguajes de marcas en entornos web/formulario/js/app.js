  // Script super básico para simular el envío
        function enviarInscripcion() {
            // Obtenemos el valor del nombre para el saludo
            var nombre = document.getElementById('nombre').value;
            var taller = document.getElementById('taller').value;

            if(nombre === "") {
                alert("Por favor, escribe al menos tu nombre.");
            } else {
                alert("¡Gracias " + nombre + "! Tu inscripción al taller de " + taller + " ha sido enviada.");
                // Opcional: resetear formulario tras enviar
                // document.getElementById('miFormulario').reset();
            }
        }

