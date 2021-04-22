const url = window.location.href

console.log(url)

const  quizBox = document.getElementById('quiz-box')
const  scoreBox = document.getElementById('score-box')
const  resultBox = document.getElementById('result-box')
let data

$.ajax({
    type:'GET',
    url : `${url}data`,
    success: function (response){
        console.log(response)
        const data = response.data
        data.forEach(el => {
            for (const [question,answers] of Object.entries(el)) {
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `

                answers.forEach(answer => {
                    quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <input type="radio" class="ans" id="${question} - ${answer}" name="${question}" value="${answer}">
                        <label for="${question}">${answer}</label>
                    </div>
                `
                })
            }
        });
    },
    error:function(error){
        console.log(error)
    }
})


const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')



const sendData = () =>{
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el =>{
        if (el.checked){
            data[el.name] = el.value
        }else{
            if (!data[el.name]){
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type:'POST',
        url: `${url}sava/`,
        data : data,
        success : function(response){
            const results = response.results
            console.log(results)
            quizForm.classList.add('not-visible')
            scoreBox.innerHTML = `${response.passed ? 'Congratulations !' : 'Ops ..'} Your result id ${response.score.toFixed(2)}`


            results.forEach(res =>{
                const resDiv = document.createElement("div")
                for(const [question,resp] of Object.entries(res)){
                    resDiv.innerHTML += question
                    const cls =['container','p-3','text-light','h3']
                    resDiv.classList.add(...cls)


                    if (resp== 'not answered'){
                        resDiv.innerHTML += '- not answered'
                        resDiv.classList.add('bg-danger')
                    }else{
                        const answer = resp['answered']
                        const correct = resp['correct_answer']

                        if (answer == correct){
                            resDiv.innerHTML += ` answered: ${answer}`
                            resDiv.classList.add('bg-success')
                        }else{
                            resDiv.innerHTML += `| correct answer: ${correct}`
                            resDiv.innerHTML += `| answered: ${answer}`
                            resDiv.classList.add('bg-danger')
                        }

                    }
                }
                resultBox.append(resDiv)
            })
        },
        error:function(error){
        console.log(error)
    }
    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()

    sendData()
} )




