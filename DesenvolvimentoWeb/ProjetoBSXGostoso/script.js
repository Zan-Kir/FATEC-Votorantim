function calcular() {
    let combo = Number(document.getElementById('inputCombo').value);
    calcularAdicionais();
    calcularEntrega();
    total = combo + valorAdicionais + valorEntrega;
    (document.getElementById('totalValor')).value = (`R$${total}.`);
    document.getElementById('descricao').value = (`Seu combo custará ${combo}, com ${valorAdicionais} de Adicionais e ${valorEntrega} de taxa de entrega.`)
}

function calcularAdicionais () {
    valorAdicionais = 0;
    let adicionais = document.querySelectorAll(`input[type='checkbox']`)
    for (let i = 0; i < adicionais.length; i++) {
        if (adicionais[i].checked) {
            valorAdicionais += Number(adicionais[i].value);
        };
    };
};

function calcularEntrega() {
    let entrega = document.querySelectorAll(`input[name='entrega']`);

    for (let i = 0; i < entrega.length; i++) {
        if (entrega[i].checked) {
            valorEntrega = Number(entrega[i].value);
            break;
        }
    };
};
