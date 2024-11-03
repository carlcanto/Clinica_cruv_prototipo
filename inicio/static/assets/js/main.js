const express = require('express');
const nodemailer = require('nodemailer');
const app = express();
const bodyParser = require('body-parser');

// Configurar el parser para JSON
app.use(bodyParser.json());

// Configurar el transporte de Nodemailer (debes usar tus propias credenciales)
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'tuemail@gmail.com',
        pass: 'tucontraseña'
    }
});

// Simular una base de datos de usuarios
const usuarios = [
    { email: 'heytucorreo@gmail.com', password: 'password123' },
    // Otros usuarios
];

// Endpoint para manejar la solicitud de restablecimiento de contraseña
app.post('/reset-password', (req, res) => {
    const { email } = req.body;
    const usuario = usuarios.find(user => user.email === email);

    if (usuario) {
        // Enviar correo de restablecimiento
        const mailOptions = {
            from: 'tuemail@gmail.com',
            to: email,
            subject: 'Restablecimiento de contraseña',
            text: `Hola, tu contraseña es: ${usuario.password}`
        };

        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                console.log(error);
                res.status(500).send({ success: false, message: 'Error al enviar el correo.' });
            } else {
                console.log('Correo enviado: ' + info.response);
                res.send({ success: true });
            }
        });
    } else {
        res.send({ success: false, message: 'Correo no encontrado.' });
    }
});

// Iniciar el servidor
app.listen(3000, () => {
    console.log('Servidor iniciado en el puerto 3000');
});
