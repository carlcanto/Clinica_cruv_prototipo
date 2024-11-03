// Abrir el modal para agregar paciente
document.getElementById("addBtn").addEventListener("click", function() {
    document.getElementById("addPatientModal").style.display = "block";
});

// Cerrar el modal
function closeModal() {
    document.getElementById("addPatientModal").style.display = "none";
}

// Cerrar el modal al hacer clic fuera del contenido del modal
window.onclick = function(event) {
    if (event.target == document.getElementById("addPatientModal")) {
        closeModal();
    }
}
