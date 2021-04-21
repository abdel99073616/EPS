console.log('sfsfGSRhsrfgb')
const url = window.location.href

console.log(url)

const  quizBox = document.getElementById('quiz-box')

let data

$.ajax({
    type:'GET',
    url : `${url}data`,
    success: function (response){
        console.log(response)
        data = response.data
        data.forEach(el => {
            for (const [question,answers] of Object.entries(el)){
               console.log(question)
               console.log(answers)
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
            }
            });
    },
    error:function(error){
        console.log(error)
    }
})