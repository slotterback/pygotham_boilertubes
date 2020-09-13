const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const tau = Math.PI * 2;
const radius = 50;

ctx.beginPath();

for (var i = 0; i < 6; i++) {
    if( i % 2 === 1) {
	ctx.moveTo(radius*(i+2),radius*(1+Math.sqrt(3)));
        ctx.arc(radius*(i+1),radius*(1+Math.sqrt(3)),radius,0,tau);
    } else {
        ctx.moveTo(radius*(i+2),radius);
        ctx.arc(radius*(i+1),radius,radius,0,tau);
    }
}

ctx.stroke();

