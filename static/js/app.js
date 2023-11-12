const inputBox = document.querySelector("input[type='text']");
const buttons = Array.from(document.querySelectorAll("input[type='button']"));
const hists = Array.from(document.querySelectorAll("td[name='calc_hist']"));
let string = "";


hists.forEach(hist => {
    hist.addEventListener('click', (e) => {
        string = inputBox.value = e.target.innerHTML;
    });
});

inputBox.addEventListener('input', (e) => {
    const value = e.target.value;
    const allowedChars = /^[0-9+*/()-]*$/;
    if (!allowedChars.test(value)) {
        e.target.value = string;
    }
});

buttons.forEach(button => {
    button.addEventListener('click', (e) => {
        if (e.target.value == 'AC') {
            inputBox.value = string = "";
        }
        else if (e.target.value == 'DEL') {
            string = inputBox.value;
            string = string.substring(0, string.length - 1);
            inputBox.value = string;
        }
        else {
            string += e.target.value;
            inputBox.value = string;
        }
    });
});