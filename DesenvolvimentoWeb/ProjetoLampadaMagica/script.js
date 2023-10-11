let lampada = document.getElementById('lampada');

function ligar() {
    lampada.src="luzLigada.gif";
    lampada.alt="Luz Acesa";
};

function desligar() {
    lampada.setAttribute("src", "luzDesligada.gif");
    lampada.alt="Luz Apagada";
};

function alternar() {
    if (lampada.getAttribute('src') == "luzLigada.gif") {
        desligar();
    }

    else if (lampada.getAttribute('src') == "luzDesligada.gif"){
        ligar();
    };

};

function sumir() {
    lampada.style.display = "none";
    document.getElementById('titulo').style.color = "red";
    // lampada.hidden = true;
};

function aparecer() {
    lampada.style.display = "block";
    document.getElementById('titulo').style.color = "black";
    // lampada.hidden = false;
};

function piscar() {
    alternar()
}

// setTimeout(piscar, 100)
setInterval(piscar, 500)
