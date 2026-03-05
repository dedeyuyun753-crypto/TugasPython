<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Kalkulator Menara</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto;
}

body{
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:linear-gradient(135deg,#6a8cff,#a86af9);
transition:0.4s;
}

body.dark{
background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

.container{
width:420px;
padding:30px;
border-radius:30px;
background:rgba(255,255,255,0.15);
backdrop-filter:blur(20px);
box-shadow:0 15px 40px rgba(0,0,0,0.25);
color:white;
animation:float 4s ease-in-out infinite;
}

@keyframes float{
0%{transform:translateY(0)}
50%{transform:translateY(-10px)}
100%{transform:translateY(0)}
}

h1{
text-align:center;
margin-bottom:20px;
font-weight:600;
}

.toggle{
position:absolute;
top:20px;
right:20px;
cursor:pointer;
font-size:22px;
}

.section{
margin-top:15px;
}

.section h3{
margin-bottom:5px;
font-size:16px;
opacity:0.9;
}

input{
width:100%;
padding:12px;
border:none;
border-radius:15px;
margin:6px 0;
outline:none;
background:rgba(255,255,255,0.8);
}

button{
width:100%;
padding:13px;
margin-top:15px;
border:none;
border-radius:18px;
font-weight:bold;
background:white;
cursor:pointer;
transition:0.3s;
}

button:hover{
transform:scale(1.05);
}

.result{
margin-top:18px;
padding:15px;
border-radius:18px;
background:rgba(255,255,255,0.2);
font-size:14px;
line-height:1.6;
animation:fade 0.5s;
}

@keyframes fade{
from{opacity:0;transform:translateY(10px)}
to{opacity:1;transform:translateY(0)}
}

.icons{
display:flex;
justify-content:center;
gap:30px;
margin-bottom:10px;
}

.cylinder,.cone{
width:60px;
height:60px;
position:relative;
}

.cylinder{
background:linear-gradient(#eee,#bbb);
border-radius:50%/20%;
box-shadow:inset 0 -10px 15px rgba(0,0,0,0.2);
}

.cone{
width:0;
height:0;
border-left:30px solid transparent;
border-right:30px solid transparent;
border-bottom:60px solid #ddd;
filter:drop-shadow(0 5px 5px rgba(0,0,0,0.2));
}

</style>
</head>

<body>

<div class="toggle" onclick="toggleMode()">🌙</div>

<div class="container">

<h1>Kalkulator Menara</h1>

<div class="icons">
<div class="cylinder"></div>
<div class="cone"></div>
</div>

<div class="section">
<h3>Silinder</h3>
<input type="number" id="r_silinder" placeholder="Jari-jari silinder">
<input type="number" id="t_silinder" placeholder="Tinggi silinder">
</div>

<div class="section">
<h3>Kerucut</h3>
<input type="number" id="r_kerucut" placeholder="Jari-jari kerucut">
<input type="number" id="t_kerucut" placeholder="Tinggi kerucut">
</div>

<button onclick="hitung()">Hitung</button>

<div id="output" class="result" style="display:none"></div>

</div>

<script>

function toggleMode(){
document.body.classList.toggle("dark")
}

function hitung(){

let r_sil = parseFloat(document.getElementById("r_silinder").value)
let t_sil = parseFloat(document.getElementById("t_silinder").value)

let r_ker = parseFloat(document.getElementById("r_kerucut").value)
let t_ker = parseFloat(document.getElementById("t_kerucut").value)

let pi = Math.PI

let keliling_sil = 2*pi*r_sil
let luas_sil = 2*pi*r_sil*(r_sil+t_sil)
let volume_sil = pi*r_sil*r_sil*t_sil

let s = Math.sqrt((r_ker*r_ker)+(t_ker*t_ker))
let keliling_ker = 2*pi*r_ker
let luas_ker = pi*r_ker*(r_ker+s)
let volume_ker = (1/3)*pi*r_ker*r_ker*t_ker

let hasil = `
<b>Silinder</b><br>
Keliling Alas : ${keliling_sil.toFixed(2)}<br>
Luas Permukaan : ${luas_sil.toFixed(2)}<br>
Volume : ${volume_sil.toFixed(2)}<br><br>

<b>Kerucut</b><br>
Keliling Alas : ${keliling_ker.toFixed(2)}<br>
Luas Permukaan : ${luas_ker.toFixed(2)}<br>
Volume : ${volume_ker.toFixed(2)}
`

let output = document.getElementById("output")
output.style.display="block"
output.innerHTML=hasil

}

</script>

</body>
</html>
