$(document).ready(function(){

    const url="https://api.1up.health/fhir/dstu2/Patient"

    // PASTE NEW ACCESS TOKEN TO TEST IT.
    var access_token="9091d346371842dccfff9bc7b752d298bc588f52"

    fetch(url+"?access_token="+access_token)
    .then(response => response.json())
    .then(data => {
        console.log(data);

        // INTEGRATING DATA HAVE 6 REOCRDS.
        console.log(data.entry[0].resource.name);

        function cardTemplates(card){

            return `
            <div class="card mt-1" style="width:400px">
            <div class="card-body">
            <h4 class="card-title" id="name">CARD FAMILY: ${card.family[0]}</h4>

                <h4 class="card-title" id="name">CARD GIVEN: ${card.given[0]}</h4>
                <label class="card-title" id="age"><strong>CARD PERIOD START:</strong> ${card.period.start}</label><br>
                <label class="card-title" id="age"><strong>CARD PERIOD TEXT:</strong> ${card.text}</label><br>
                <label class="card-title" id="age"><strong>CARD PERIOD USE:</strong> ${card.use}</label><br>
            </div>
        </div>`
        };

        document.getElementById("display").innerHTML=`${data.entry[0].resource.name.map(cardTemplates).join("")}`
    });


        
    
});