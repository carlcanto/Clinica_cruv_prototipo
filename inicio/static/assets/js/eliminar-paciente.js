document.getElementById('myBtnModal').addEventListener('click', function() {
    var cedula = document.getElementById('searchInput').value;
    fetch('{% url "buscar_paciente" %}', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: new URLSearchParams({
            'cedula': cedula
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            // Mostrar mensaje de error y ocultar modal
            document.getElementById('errorMessage').style.display = 'block';
            document.getElementById('myModal').style.display = 'none';
        } else {
            // Ocultar mensaje de error
            document.getElementById('errorMessage').style.display = 'none';
            
            // Mostrar el modal de confirmación
            document.getElementById('myModal').style.display = 'block';

            // Añadir evento al botón de confirmar eliminación
            document.getElementById('confirmDeleteBtn').addEventListener('click', function() {
                fetch('{% url "eliminar_paciente" %}', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': '{{ csrf_token }}'
                    },
                    body: new URLSearchParams({
                        'cedula': cedula
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('Paciente eliminado exitosamente.');
                        // Redirigir o actualizar la página
                        window.location.reload();
                    } else {
                        alert('Error al eliminar el paciente.');
                    }
                    closeModal();
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function closeModal() {
    document.getElementById('myModal').style.display = 'none';
}
