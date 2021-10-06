function select_sec(){
    const valor = document.querySelector('input[name="regiao"]:checked').value
    regiao_capitais = document.querySelector("h2.regiao_capitais")
    regiao_capitais.innerHTML = valor.toUpperCase()
    
    return valor 
}

// FUNÇÃO JQUERY QUE VAI CARREGAR AS INFORMAÇÕES NO ONLOAD DA PÁGINA
$(function(){
    //tag select da página 2 do html 
    $("#select_grafic").on("change", function(){
        
        var valor_select = $(this).val()
        // alert(valor_select)
        // envia para servidor o valor
        $.ajax({
            method: "POST",
            url: "/graficos",
            data: {'tygrafico': valor_select}
        })
        sec_dois = document.querySelector('.sec_dois')
        
        sec_dois.innerHTML = ""
        // setTimeout(function(){
        //     // alert('TEMPO')
        // }, 1000);

        if (valor_select == "0"){
            $(".sec_dois").hide()
            
        }else {
            // ESSA CODICIONAL VAI CRIAR AS TAGS QUE CHAMAM AS IMAGENS DOS GRÁFICOS
            var lista = ['Nordeste', 'Norte', 'Centro-Oeste', 'Sudeste', 'Sul']
            $(".posicao-Nordeste").remove();
            $(".posicao-Norte").remove();
            $(".posicao-Centro-Oeste").remove();
            $(".posicao-Sudeste").remove();
            $(".posicao-Sul").remove();
            
            for (let i of lista){
                sec_dois.innerHTML += `<h1>${i}</h1><div class="posicao-${i}"></div>`
                grafico = `url('../static/graficos/grafico_${i}_${valor_select}.png')`
                
                $(".posicao-"+i).css("background-image", grafico)
            }
            $(".sec_dois").show()
            
            // setTimeout(function(){
                
            // }, 2000);
        
        }  
    }) 
    // seciona

    $.getJSON("../static/conteudo_secao.json", function(data) { 
        cria_elementos(data) // FUNÇÃO QUE VAI CRIAR OS ELEMENTOS

        // ABRE O ARQUIVO JSON
        $(".seleciona_r").click(function(){
            cria_elementos(data) // FUNÇÃO QUE VAI CRIAR OS ELEMENTOS
        }) 
    })  
});


function cria_elementos(data){
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


// setTimeout(function(){
// }, 1000);
// var xhr = new XMLHttpRequest();

// xhr.onreadystatechange = function(){
//     if (xhr.readyState == 4 && xhr.status == 200){
//         console.log(xhr)
//     }
// }
// xhr.open("GET", "file:///D:/PROGRAMAÇÃO%20GERAL/Projeto_de_Previsao_do_Tempo/templates/secao_graficos.html")
// xhr.send()
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


// let minhaUrl = `${window.location.origin}/${valor_select}`
        // var url = window.location.search;
        // var minhaUrl = window.location.href = `${window.location.search}?`+valor_select
        // alert(minhaUrl)