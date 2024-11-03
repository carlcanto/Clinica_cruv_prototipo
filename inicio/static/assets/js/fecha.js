document.addEventListener("DOMContentLoaded", function() {
    var fechaHoraActualElemento = document.getElementById("fechaHoraActual");
  
    // Función para obtener la fecha y hora actual en formato personalizado
    function obtenerFechaHoraActualFormateada() {
      var fechaActual = new Date();
      var opcionesFecha = { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' };
      var opcionesHora = { hour: 'numeric', minute: 'numeric', second: 'numeric' };
      var fechaFormateada = fechaActual.toLocaleDateString('es-ES', opcionesFecha);
      var horaFormateada = fechaActual.toLocaleTimeString('es-ES', opcionesHora);
      return fechaFormateada + ' - ' + horaFormateada;
    }
  
    // Mostrar la fecha y hora actual formateada al cargar la página
    fechaHoraActualElemento.textContent = obtenerFechaHoraActualFormateada();
  
    // Actualizar la fecha y hora cada segundo
    setInterval(function() {
      fechaHoraActualElemento.textContent = obtenerFechaHoraActualFormateada();
    }, 1000);
  });
  
  // fecha.js

document.addEventListener('DOMContentLoaded', function() {
  // Obtén el elemento del selector de fecha
  const dateInput = document.getElementById('fecha');
  
  // Verifica si el elemento existe antes de añadirle eventos
  if (dateInput) {
      // Configura el evento para manejar cambios en el selector de fecha
      dateInput.addEventListener('change', function(event) {
          // Obtén la fecha seleccionada
          const selectedDate = event.target.value;

          // Puedes hacer algo con la fecha seleccionada aquí
          // Por ejemplo, enviar la fecha al backend usando fetch
          fetch('/citas/programar/', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': getCookie('csrftoken') // Obtén el token CSRF de las cookies
              },
              body: JSON.stringify({ fecha: selectedDate })
          })
          .then(response => response.json())
          .then(data => {
              console.log('Respuesta del servidor:', data);
              // Maneja la respuesta del servidor aquí
          })
          .catch(error => {
              console.error('Error:', error);
          });
      });
  }
});

// Función para obtener el token CSRF de las cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
