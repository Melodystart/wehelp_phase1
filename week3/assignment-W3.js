function getData(m = 0, n = 15) {

  fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
    .then(function (response) {
      return response.json();
    })
    .then(function (myJson) {
      const data = myJson["result"]["results"]

      for (let i = m; i < n; i++) {

        let division = document.createElement("div");
        let image = document.createElement("img");
        let word = document.createElement("p");

        image.src = data[i]["file"].substr(0, data[i]["file"].indexOf('https', 1))
        word.innerText = data[i]["stitle"]
        division.appendChild(image);
        division.appendChild(word);

        if (i >= 0 && i < 3) {

          division.classList.add("promotion-content");
          image.classList.add("photo1");
          word.classList.add("promotion-text");
          document.querySelector('.promotion').appendChild(division);

        } else {

          division.classList.add("title-content");
          image.classList.add("photo2");
          word.classList.add("title-text");
          document.querySelector('.title').appendChild(division);

        }

        if (i === 2) {
          division.id = "promotion3"
        }

      }

    });
}


getData(0, 15);

let btn = document.getElementById('btn');

btn.addEventListener('click', function () {
  let image = document.querySelectorAll('img');
  console.log(image.length);
  getData(image.length, image.length + 12);
});