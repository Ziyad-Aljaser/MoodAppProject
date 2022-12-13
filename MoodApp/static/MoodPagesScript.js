let btn = document.querySelector('#bn');

function getRandomNumber(min, max) {
    let step1 = max - min + 1;
    let step2 = Math.random() * step1;
    return Math.floor(step2) + min;
}

function createArrayOfNumbers(start, end){
    let myArray = [];
    for(let i = start; i <= end; i++) {
        myArray.push(i);
    }
    return myArray;
}

function isItRepeated(){

    if(numbersArray.length === 0){
        alert("There is no more phrases");
        return;
    }

    let randomIndex = getRandomNumber(0, numbersArray.length-1);
    let randomNumber = numbersArray[randomIndex];
    numbersArray.splice(randomIndex, 1)

    let authorPic = '<img src="'+ AuthorPic[randomNumber] +'" style="border-radius: 50%; width: 250px;" alt=""/>';


    document.getElementById("a").innerHTML = (Author[randomNumber])
    document.getElementById("p").innerHTML = (Phrase[randomNumber])
    document.getElementById("pic").innerHTML = (authorPic)

}

let numbersArray = createArrayOfNumbers(0, Id.length-1);
isItRepeated();

btn.addEventListener("click", () => {

    isItRepeated();

 });