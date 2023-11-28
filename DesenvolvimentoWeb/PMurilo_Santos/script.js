document.getElementById(`idade`).addEventListener('click', async function () {
    let cep = document.getElementById(`cep`).value
    let api = `https://viacep.com.br/ws/${cep}/json`
    let respostaAPI = await fetch(api)
    let dadosCEP = await respostaAPI.json()
    document.getElementById(`cidade`).value = `${dadosCEP.localidade}`
})

document.getElementById(`cadastrar`).addEventListener('click', async function () {
    let idade = Number(document.getElementById(`idade`).value)
    let idadeMaisTrinta = idade + 30
    alert(`A idade +30 é de: ${idadeMaisTrinta}`)
    termos = document.querySelectorAll(`input[name='termos']`)
    if (termos[0].checked) {
        document.getElementById(`cadastro`).innerHTML = `Cadastrado com sucesso`
    }
})
