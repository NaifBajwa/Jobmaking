const petsData0 = [
    {
        name: "Purrsloud",
        species: "Cat",
        favFoods: ["wet food", "dry food", "<strong>any</strong> food"],
        birthYear: 2016,
        photo: "https://learnwebcode.github.io/json-example/images/cat-2.jpg"
    },
    {
        name: "Barksalot",
        species: "Dog",
        birthYear: 2008,
        photo: "https://learnwebcode.github.io/json-example/images/dog-1.jpg"
    },
    {
        name: "Meowsalot",
        species: "Cat",
        favFoods: ["tuna", "catnip", "celery"],
        birthYear: 2012,
        photo: "https://learnwebcode.github.io/json-example/images/cat-1.jpg"
    },
    {
        name: "Purrsloud",
        species: "Cat",
        favFoods: ["wet food", "dry food", "<strong>any</strong> food"],
        birthYear: 2016,
        photo: "https://learnwebcode.github.io/json-example/images/cat-2.jpg"
    },
    {
        name: "Barksalot",
        species: "Dog",
        birthYear: 2008,
        photo: "https://learnwebcode.github.io/json-example/images/dog-1.jpg"
    },
    {
        name: "Meowsalot",
        species: "Cat",
        favFoods: ["tuna", "catnip", "celery"],
        birthYear: 2012,
        photo: "https://learnwebcode.github.io/json-example/images/cat-1.jpg"
    }
];

const petsData1 = [
{
    "ID": "rec0TGDtfNq5k5oh0",
    "Name": "Lena Andersson",
    "Yrke": "S\u00e4ljare",
    "Annonstitel": "S\u00e4ljare Region Nord \u2013 V\u00e4sterbotten, V\u00e4sternorrland och J\u00e4mtland",
    "Arbetsgivare": "Ramudden AB",
    "Sistadatum": "2020-12-30",
    "url": "http://www.cnn.com"
},
{
    "ID": "rec0Vl8QMVAwOgvv6",
    "Name": "karin Karlsson",
    "Yrke": "Lastbilsf\u00f6rare",
    "Annonstitel": "CE-chauff\u00f6rer s\u00f6kes f\u00f6r start omg\u00e5ende!",
    "Arbetsgivare": "Nordic BR Norr AB",
    "Sistadatum": "2020-12-31",
    "url": "http://www.bcc.com"
},
{
    "ID": "rec0gIaNjqFByL76P",
    "Name": "Ali Ramalah",
    "Yrke": "L\u00e4rare i grundskolan",
    "Annonstitel": "L\u00e4rare i Samh\u00e4llsorienterade \u00e4mnen till N\u00e4ldens skola, J\u00e4mtland",
    "Arbetsgivare": "Krokoms kommun",
    "Sistadatum": "2021-01-01",
    "url": "http://www.dn.se"
},
{
    "ID": "rec1Bk2dk4ZdTXTez",
    "Name": "Ingrid Larsson",
    "Yrke": "Snickare",
    "Annonstitel": "Mockfj\u00e4rds F\u00f6nster s\u00f6ker montagef\u00f6retag till V\u00e4sternorrland",
    "Arbetsgivare": "Mockfj\u00e4rds F\u00f6nster AB",
    "Sistadatum": "2021-01-07",
    "url": "http://www.sr.se"
},
{
    "ID": "rec26K5HeLY7xsWfh",
    "Name": "Owen Sten",
    "Yrke": "Utvecklare",
    "Annonstitel": "Utvecklare/samordnare inom social h\u00e5llbarhet ",
    "Arbetsgivare": "L\u00e4nsstyrelsen i V\u00e4sternorrlands l\u00e4n",
    "Sistadatum": "2021-01-09",
    "url": "http://www.svt.se"
},
{
    "ID": "rec2GSsvKIVuUwZ2q",
    "Name": "Ahmed Farah",
    "Yrke": "L\u00e4kare",
    "Annonstitel": "Tv\u00e5 vikarierande underl\u00e4kare i barn- och ungdomsmedicin vid \u00d6stersunds sjuk",
    "Arbetsgivare": "REGION J\u00c4MTLAND H\u00c4RJEDALEN",
    "Sistadatum": "2021-01-31",
    "url": "http://www.st.nu"
}
];

fetch('./Data/Matchning2.json')
.then(response => response.json() )
.then(data => {
    document.getElementById("app").innerHTML = `
    <h1 class="app-title">${data.length} Jobb Matchningar</h1>
    ${data.map(petTemplate1).join("  ")}
  `
})

function age(birthYear) {
    let calculatedAge = new Date().getFullYear() - birthYear;
    if (calculatedAge == 1) {
        return "1 year old";
    } else if (calculatedAge == 0) {
        return "Baby";
    } else {
        return `${calculatedAge} years old`;
    }
}

function foods(foods) {
    return `
<h4>Favorite Foods</h4>
<ul class="foods-list">
${foods.map(food => `<li>${food}</li>`).join("")}
</ul>
`;
}

function petTemplate0(pet) {
    return `
    <div class="animal">
    <!-- <img class="pet-photo" src="${pet.photo}"> -->
    <h2 class="pet-name">${pet.name} <span class="species">(${pet.species})</span></h2>
    <p><strong>Age:</strong> ${age(pet.birthYear)}</p>
    ${pet.favFoods ? foods(pet.favFoods) : ""}
    </div>
  `;
}

function colorDate(date) {
    let calculatedAge = (new Date(date).getTime() - new Date().getTime()) / 3600000;
    calculatedAge = Math.round(calculatedAge / 24);
    if (calculatedAge < 0) {
        return `<span class="red"><del>${date}</del> (closed)</span>`;
    } else if (calculatedAge < 2) {
        return `<span class="red">${date}</span>`;
    } else if (calculatedAge < 10) {
        return `<span class="yellow">${date}</span>`;
    } else {
        return `<span class="green">${date}</span>`;
    }
}

function colorDate2(date) {
    let calculatedAge = (new Date(date).getTime() - new Date().getTime()) / 3600000;
    calculatedAge = Math.round(calculatedAge / 24);
    if (calculatedAge < 2) {
        return 'task-red';
    } else if (calculatedAge < 10) {
        return 'task-yellow'; 
    } else {
        return 'task';
    }
}


function petTemplate1(pet) {
    return `
    <div class=${colorDate2(pet.Sistadatum)}>
    <h2 class="pet-name">${pet.Name}</h2> 
    <hr size="3" noshade>
    <p><strong>Yrke:</strong><br>${pet.Yrke}</p>
    <p><strong>Annonstitel:</strong><br> <a href=${pet.url} target="_blank">${pet.Annonstitel}</a></p> 
    <p><strong>Arbetsgivare:</strong><br> ${pet.Arbetsgivare}</p>
    <p><strong>Sista datum:</strong><br> ${colorDate(pet.Sistadatum) }</p>
    </div>
  `;
}

function petTemplate(pet) {
    return `
    <div class=${colorDate2(pet.Sistadatum)}>
    <h2 class="pet-name">${pet.Name}</h2> 
    <hr size="3" noshade>
    <p><strong>Yrke:</strong><br>${pet.Yrke}</p>
    <p><strong>Annonstitel:</strong><br> ${pet.Annonstitel}</p> 
    <p><strong>Arbetsgivare:</strong><br> ${pet.Arbetsgivare}</p>
    <p><strong>Sista ans&ouml;kningsdatum:</strong><br> ${colorDate(pet.Sistadatum) }</p>
    </div>
  `;
}

function loadRecords() {
    return `
    <h1 class="app-title">${petsData1.length} Jobb Matchningar</h1>
    ${petsData1.map(petTemplate1).join("  ")}
  `;
}

function loadRecs() {
    document.getElementById("app1").innerHTML = loadRecords();
}
 
