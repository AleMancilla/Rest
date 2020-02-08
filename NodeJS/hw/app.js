var express = require('express'); //donde requerimos el modulo de express
var app = express(); // nos referimos a la apicacion

//creamos una ruta
app.get('/',function(req, res) {//primer parametro cadena de texto, seg funcion con reques and response
    //cuando accedemos recibimos una peticion
    res.send('Hello World! con NodeJS'); // enviamos una respuesta 
});
// la aplicacion de flask por defecto usa el puerto 5000
app.listen(3000,function() {
    console.log(' * Running on http://127.0.0.1:3000/ (Press CTRL + C to quit)');
});// asi que ponemos el puerto 3000