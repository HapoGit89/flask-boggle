

const $subButton = $('#submitguess')
const $guessInput = $('#guess')
const $score = $('#score')
const $time = $('#timer')
const $restartButton = $('#restart')
const $all = $("*")

let score = 0;


let count = ''

async function game_countdown(time) {
    let timer = setInterval(function () {
        time--;
        if (time <= 0) {
            clearInterval(timer);
            count = 0
            console.log(count)
            
        }
        else {
            count = time
            console.log(count)
        }
        $time.text(`Remaining Time: ${count}`)

    }, 1000)
}

game_countdown(60)

async function send_score(points){
    const response = await axios({
        url: `/gameend`,
        method: "POST",
        data: { score: points },

    })

    return response.data
}

$restartButton.on("click", async function(){
    console.log("Button works")
    await send_score(score)
    window.location.replace('/newgame')
})


$subButton.on("click", async function (e) {
    e.preventDefault()
    if (count != 0) {
        const result = await sendGuess($guessInput.val())
        if (result.data === "ok") {
            score += $guessInput.val().length
            $score.text(`Score: ${score}`)

        }
        $('#result').text(`Last guess: ${$guessInput.val().toUpperCase()}     ---->     ${result.data.toUpperCase()}`)
    }
    $guessInput.val('')
})


async function sendGuess(guess) {

    const response = await axios({
        url: `/guess`,
        method: "POST",
        data: { guess: guess },
    });

    return response

}