

const $subButton = $('#submitguess')
const $guessInput = $('#guess')
const $score = $('#score')
const $time = $('#timer')

let count = ''

function countdown(time) {
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

countdown(60)

let score = 0;

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
})


async function sendGuess(guess) {

    const response = await axios({
        url: `/guess`,
        method: "POST",
        data: { guess: guess },
    });

    return response

}