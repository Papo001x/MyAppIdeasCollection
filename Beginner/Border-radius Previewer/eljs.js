function cambiarbordesTL(){
    var valor =document.getElementById('esquina').value;
    document.getElementById('caja').style.borderTopLeftRadius=valor+'px';
}
function cambiarbordesTR(){
    var valor =document.getElementById('esquina2').value;
    document.getElementById('caja').style.borderTopRightRadius=valor+'px';
}
function cambiarbordesDL(){
    var valor =document.getElementById('esquina3').value;
    document.getElementById('caja').style.borderBottomLeftRadius=valor+'px';
}
function cambiarbordesDR(){
    var valor =document.getElementById('esquina4').value;
    document.getElementById('caja').style.borderBottomRightRadius=valor+'px';
}