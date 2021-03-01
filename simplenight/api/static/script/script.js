$(document).ready(function(){
    urls = [
        "http://127.0.0.1:8001/indigo/",
        "http://127.0.0.1:8002/spicejet/",
        "http://127.0.0.1:8003/airindia/"
    ] 

    for (i = 0; i < 3; i++) {

        fetch(urls[i])
        .then(response => response.json())
        .then(data => {
            
            for(j=0;j<data.length;j++){
                $("#display").append(
                    `<div class="card mt-1" style="width:100%">
                        <div class="card-body">
                        <h4 class="card-title" id="name">FLIGHT: ${data[j].flight_name}(${data[j].flight_id})</h4>
                            <div class="d-flex justify-content-around">
                                <div class="col-sm">
                                    <label class="card-title" id="name"><strong>Source:</strong> ${data[j].source}</label><br>
                                    <label class="card-title" id="name"><strong>Departure time:</strong> ${data[j].departure_time}</label><br>
                                    <label class="card-title" id="age"><strong>Fare:</strong> ${data[j].fare}</label>
                                </div>
                                <div class="col-sm">
                                    <label class="card-title" id="name"><strong>Destination:</strong> ${data[j].destination}</label><br>
                                    <label class="card-title" id="age"><strong>Arrival time:</strong> ${data[j].arrival_time}</label>
                                </div>
                            </div>
                        </div>
                    </div>`
                )
            }
        });
    } 
});
 
// function flightTemplates(flight){

    //     return `
    //     <div class="card mt-1" style="width:400px">
    //     <div class="card-body">
    //     <h4 class="card-title" id="name">FLIGHT NO: ${flight.flight_id}</h4>
    //         <label class="card-title" id="name"><strong>Departure time:</strong> ${flight.departure_time}</label><br>
    //         <label class="card-title" id="age"><strong>Arrival time:</strong> ${flight.arrival_time}</label><br>
    //         <label class="card-title" id="age"><strong>Fare:</strong> ${flight.fare}</label><br>
    //     </div>
    // </div>`
    // };

    // document.getElementById("display").innerHTML=`${data1.map(flightTemplates).join("")}`

    // const request = new XMLHttpRequest();
    // request.open('POST', url, false);
    // equest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    // request.setRequestHeader('Accept', 'application/json');
    // request.send("username=sam&password=NIT2bheem!");
    // request.onreadystatechange = function() {
    //         // D some business logics here if you receive return
    //    if(request.readyState === 4 && request.status === 200) {
    //        console.log(request.responseText);
    //    }
    // }
    // request.send()

    // var urls = ["http://127.0.0.1:8001/gettoken/ username=sam&password=NIT2bheem!",
    //             "http://127.0.0.1:8002/gettoken/ username='sam' password='NIT2bheem!'",
    //             "http://127.0.0.1:8003/gettoken/ username='sam' password='NIT2bheem!'"]