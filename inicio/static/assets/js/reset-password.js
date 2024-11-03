document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
    var resetEmail = document.getElementById("correo").value;

    fetch('/reset-password/', {  // Asegúrate de que el endpoint sea el correcto
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')  // Necesario para enviar POST con CSRF token
        },
        body: new URLSearchParams({
            'resetEmail': resetEmail
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Correo de restablecimiento enviado.");
            window.location.href = "/login/";  // Redirige a la página de login
        } else {
            alert("Correo no encontrado.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Ocurrió un error. Por favor, intenta de nuevo.");
    });
});

// Función para obtener el CSRF token
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

