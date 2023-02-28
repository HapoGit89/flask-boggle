

const $subButton = $('#submitguess')
const $guessInput = $('#guess')
const $score = $('#score')


let score = 0;

$subButton.on("click", async function (e) {
    e.preventDefault()
    const result = await sendGuess($guessInput.val())
    if (result.data === "ok"){
        score += 1
        $score.text(`Score: ${score}`)
        
    }
    $('#result').text(`Last guess: ${$guessInput.val().toUpperCase()}     ---->     ${result.data.toUpperCase()}`)
})


async function sendGuess(guess) {

    const response = await axios({
        url: `/guess`,
        method: "POST",
        data: { guess: guess },
    });

    return response

}