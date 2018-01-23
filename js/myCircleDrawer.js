var draw = SVG('drawingCircles').size(300, 130);
var circle = draw.circle(50).fill('#fff');

var clip = draw.clip();
clip.add(circle.center(35, 35));
clip.add(circle.clone().center(70, 70).size(70).fill('#ccc'));
clip.add(circle.clone().center(90, 30).size(30).fill('#999'));
clip.add(circle.clone().center(105, 115).size(50).fill('#333'));

var rect = draw.rect(100, 100).move(20, 20).fill('#EC5657');
rect.clipWith(clip);

rect.on('mouseover', function() {
	this.animate(300, '-').fill('#642E68');
});
rect.on('mouseout', function() {
	this.animate(300, '-').fill('#EC5657');
});
