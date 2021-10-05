function select_sec(){
    const valor = document.querySelector('input[name="regiao"]:checked').value
    regiao_capitais = document.querySelector("h2.regiao_capitais")
    regiao_capitais.innerHTML = valor.toUpperCase()
    
    return valor 
}

// FUNÇÃO JQUERY QUE VAI CARREGAR AS INFORMAÇÕES NO ONLOAD DA PÁGINA
$(function(){
    $.getJSON("../static/conteudo_secao.json", function(data) { 
        cria_elementos(data) // FUNÇÃO QUE VAI CRIAR OS ELEMENTOS

        // ABRE O ARQUIVO JSON
        $(".seleciona_r").click(function(){
            cria_elementos(data) // FUNÇÃO QUE VAI CRIAR OS ELEMENTOS
        })  

    })
    
});

function cria_elementos(data){
    // var posicao_div = document.createElement('div')
    // posicao_div.classList.add('posicao_div') // VAI CRIAR A CLASS NO ELEMENTO   
    // section_conteudo.appendChild(posicao_div)
    
    console.log(data)
    
    var valor = select_sec()
    var section_conteudo = document.querySelector('#section_conteudo')
    section_conteudo.innerHTML=""
    console.log(data.length)

    for (let i = 0; i < data.length; i++){

        if (data[i][11] == valor){            
            section_conteudo.innerHTML += `
            <div class="posicao_div">
                <h2>Capital: ${data[i][0]}</h2>
                <h3>Código: ${data[i][1]}</h3>
                <p class="att">Atualização: ${data[i][2]}</p>
                <p>Pressão: ${data[i][3]}</p>
                <p>Temperatura: ${data[i][4]}</p>
                <p>Tempo: ${data[i][5]}</p>
                <p>Descrição do Tempo: ${data[i][6]}</p>
                <p>umidade: ${data[i][7]}</p>
                <p>vento_dir: ${data[i][8]}</p>
                <p>vento_int: ${data[i][9]}</p>
                <p class="last_p">Intensidade: ${data[i][10]}</p>
            </div>
            `
        }
        else continue   
    }
}


// método de leitura do arquivo json
// const getTodos = callback => {
//     const request = new XMLHttpRequest()

//     request.addEventListener('readystatechange',() =>{
//         const isRequestOk = request.readyState == 4 && request.status === 200
//         const isRequestNotOk = request.readyState === 4

//         if(isRequestOk) {
//             const data = JSON.parse(request.responseText)
//             callback(null, data)
//             return 
//         }
//         if(isRequestNotOk){
//             callback('Não foi possível obter os dados', null)
//         }

//     })
//     request.open('GET', './static/capitais.json' )
//     request.send()
// }
// getTodos((error, data) =>{
//     console.log('callback executado')
//     if(error){
//         console.log(error)
//         return
//     }
//     console.log(data)

// })



//QUANDO SE MANIPULA CLASSES E IDS É NECESSÁRIO CONCATENAR COM O SIMBOLO DO ATRIBUTO(ELEMENTO)

// function ocu_visu_reg(valor){
//     if (valor == "Sudeste"){
//         document.querySelector(".Sul").style.display = "none"
//         document.querySelector(".Norte").style.display = "none"
//         document.querySelector(".Nordeste").style.display = "none"
//         document.querySelector(".Centro-Oeste").style.display = "none"
//         document.querySelector(".Sudeste").style.display = "block"
//     }
//     if (valor == "Sul"){
//         document.querySelector(".Sul").style.display = "block"
//         document.querySelector(".Norte").style.display = "none"
//         document.querySelector(".Nordeste").style.display = "none"
//         document.querySelector(".Centro-Oeste").style.display = "none"
//         document.querySelector(".Sudeste").style.display = "none"
//     }
//     if (valor == "Centro-Oeste"){
//         document.querySelector(".Sul").style.display = "none"
//         document.querySelector(".Norte").style.display = "none"
//         document.querySelector(".Nordeste").style.display = "none"
//         document.querySelector(".Centro-Oeste").style.display = "block"
//         document.querySelector(".Sudeste").style.display = "none"
//     }
//     if (valor == "Norte"){
//         document.querySelector(".Sul").style.display = "none"
//         document.querySelector(".Norte").style.display = "block"
//         document.querySelector(".Nordeste").style.display = "none"
//         document.querySelector(".Centro-Oeste").style.display = "none"
//         document.querySelector(".Sudeste").style.display = "none"
//     }
//     if (valor == "Nordeste"){
//         document.querySelector(".Sul").style.display = "none"
//         document.querySelector(".Norte").style.display = "none"
//         document.querySelector(".Nordeste").style.display = "block"
//         document.querySelector(".Centro-Oeste").style.display = "none"
//         document.querySelector(".Sudeste").style.display = "none"
//     }
//     return true

// }
