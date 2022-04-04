function sendEmail(){
  Email.send({
  Host : "smtp.gmail.com",
  Username : "palabrasglosariolcen@gmail.com",
  Password : "glosariolcen2022",
  To : "palabrasglosariolcen@gmail.com",
  From : "soporte@laconstitucionesnuestra.cl",
  Subject : "Palabra para Glosario LCEN 2022",
  Body : "Palabras sugeridas para Glosario: " + document.getElementById("palabra").value
}).then(
message => alert("Se ha enviado la palabra correctamente. La revisaremos e incluiremos en el Glosario.")
);
}
