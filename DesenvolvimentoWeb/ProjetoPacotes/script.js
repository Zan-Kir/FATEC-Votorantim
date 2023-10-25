let valorPacote;
let valorAdicionais;
let totalPacote;
let nome;

function calcular() {
    let nome = document.getElementById('nome').value
    calcularValorPacote();
    calcularAdicionais();
    totalPacote = valorAdicionais + valorPacote;
    // alert(`O total do pacte é R$${totalPacote}.`);
    (document.getElementById('totalViagem')).innerHTML = `${nome}. O total do pacote é R$${valorPacote} e R$${valorAdicionais} de adicionais. Total de R$${totalPacote}.`

}

function calcularValorPacote() {
    valorPacote = 0;
    let qtdPacotes = document.querySelectorAll(`input[name='pacotes']`).length;
    let pacotes = document.querySelectorAll(`input[name='pacotes']`);

    for (let i = 0; i < qtdPacotes; i++) {
        if (pacotes[i].checked) {
            valorPacote = Number(pacotes[i].value);
            break;
        }
    };
};

function calcularAdicionais () {
    valorAdicionais = 0;
    let adicionais = document.querySelectorAll(`input[type='checkbox']`)
    for (let i = 0; i < adicionais.length; i++) {
        if (adicionais[i].checked) {
            valorAdicionais += Number(adicionais[i].value);
        };
    };
};
