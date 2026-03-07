async function scan(){

const url = document.getElementById("urlInput").value;

const response = await fetch("/analyze",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({url:url})

});

const data = await response.json();

document.getElementById("result").innerHTML =

`
<h2>Risk Score: ${data.risk_score}/100</h2>
<p>Keywords: ${data.keywords_found}</p>
`;

}