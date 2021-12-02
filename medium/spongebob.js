// Remember the spongebob meme that is meant to make fun of people by repeating what they say in a mocking way?

// You need to create a function that converts the input into this format, with the output being the same string expect there is a pattern of uppercase and lowercase letters.

// Examples:

// spongeMeme("stop Making spongebob Memes!") // => 'StOp mAkInG SpOnGeBoB MeMeS!'

let myString = "Thanks Alex"
function spongeBob(myString){
    return myString.split("").map((char, i) => i%2 === 0 ? char.toUpperCase(): char.toLowerCase()).join("")
}
console.log(spongeBob(myString))