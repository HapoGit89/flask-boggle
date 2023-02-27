
console.log("JS here")

const $subButton = $('#submitguess')
const $guessInput = $('#guess')

$subButton.on("click", async function (e) {
    e.preventDefault()
    await sendGuess($guessInput.val())
})


async function sendGuess(guess) {

    await axios({
        url: `/guess`,
        method: "POST",
        data: { guess: guess },
    });

}