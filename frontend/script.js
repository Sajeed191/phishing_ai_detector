async function scanURL(){

let url=document.getElementById("urlInput").value;

let response=await fetch("/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({url:url})

})

let data=await response.json()

let resultDiv=document.getElementById("result")

if(data.error){

resultDiv.innerHTML=data.error
return
}

resultDiv.innerHTML=

"Result: "+data.result+
"<br>Confidence: "+data.confidence+"%"+
"<br><br>Threat Indicators:<br>"+
data.threat_indicators.join("<br>")

}