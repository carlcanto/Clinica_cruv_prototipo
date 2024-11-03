// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtnModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }


}
// Abrir el modal de confirmacion de eliminacion
function openDeleteModal() {
    document.getElementById("myModal").style.display = "block";
}

// Cerrar el modal de confirmación de eliminación
function closeDeleteModal() {
    document.getElementById("myModal").style.display = "none";
}

document.getElementById("confirmDeleteBtn").addEventListener("click", function() {
    // Lógica para eliminar el paciente
    // Ejemplo: eliminarPaciente(idPaciente);
    closeDeleteModal();
    alert("Eliminacíon Exitosa.");
});

document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#miFormulario');
  form.addEventListener('submit', (event) => {
      event.preventDefault();
      const formData = new FormData(form);
      fetch('/citas/programar/', {
          method: 'POST',
          body: formData,
          headers: {
              'X-CSRFToken': getCookie('csrftoken'),
              'Content-Type': 'application/x-www-form-urlencoded'
          }
      })
      .then(response => response.json())
      .then(data => {
          if (data.status === 'success') {
              console.log('Cita programada con ID:', data.cita_id);
          } else {
              console.error('Error:', data.errors);
          }
      })
      .catch((error) => {
          console.error('Error:', error);
      });
  });
});

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