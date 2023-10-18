function calcular() {
    let qtdPacotes = document.querySelectorAll(`input[name='pacotes']`).length;
    let pacotes = document.querySelectorAll(`input[name='pacotes']`);

    for (let i = 0; i < qtdPacotes; i++) {
        console.log(pacotes[i].value);
    };
};