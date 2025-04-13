async function get_suggestion(value) {
    let resultat_div = document.getElementById("resultat");
    liste = ["teste", "teste1", "teste2", "teste3", "teste4", "teste5", "teste6", "teste7", "teste8", "teste9"];
    await fetch("http://localhost:8000/suggestions/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ "mot_a_corriger": value }),
    }).then(res=>res.json())
    .then(data => {
        liste = data;
    });
    console.log(liste);
    resultat_div.innerHTML = "";

    for (let i = 0; i < liste.length; i++) {
        resultat_div.innerHTML += `<p onclick='choisir_mot("${liste[i]}")'>` + liste[i] + "</p>";
    }
}

function choisir_mot(mot) {
    document.getElementById("mot").value = mot;
}