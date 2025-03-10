'use strict';

var ohContainer = document.querySelector('.oh');
var allCards = document.querySelectorAll('.oh--card');
var nope = document.getElementById('nope');
var love = document.getElementById('love');

function initCards(card, index) {
  var newCards = document.querySelectorAll('.oh--card:not(.removed)');

  newCards.forEach(function (card, index) {
    card.style.zIndex = allCards.length - index;
    card.style.transform = 'scale(' + (20 - index) / 20 + ') translateY(-' + 30 * index + 'px)';
    card.style.opacity = (10 - index) / 10;
  });
  
  ohContainer.classList.add('loaded');
}

initCards();

allCards.forEach(function (el) {
  var hammertime = new Hammer(el);

  hammertime.on('pan', function (event) {
    el.classList.add('moving');
  });

  hammertime.on('pan', function (event) {
    if (event.deltaX === 0) return;
    if (event.center.x === 0 && event.center.y === 0) return;

    //ohContainer.classList.toggle('oh_love', event.deltaX > 0);
    const percentage = Math.min(Math.max(Math.abs(event.deltaX) / 4, 0), 100);
    if (event.deltaX > 0) {
      event.target.style.background = `linear-gradient(to top, #2EE7B6 ${percentage}%, transparent 100%)`;
    }
    else {
      event.target.style.background = `linear-gradient(to top, #FF3E3E ${percentage}%, transparent 100%)`;
    }
    //ohContainer.classList.toggle('oh_nope', event.deltaX < 0);

    var xMulti = event.deltaX * 0.03;
    var yMulti = event.deltaY / 80;
    var rotate = xMulti * yMulti;

    event.target.style.transform = 'translate(' + event.deltaX + 'px, ' + event.deltaY + 'px) rotate(' + rotate + 'deg)';
  });

  hammertime.on('panend', function (event) {
    el.classList.remove('moving');
    //ohContainer.classList.remove('oh_love');
    //ohContainer.classList.remove('oh_nope');
    event.target.style.background="white";

    var moveOutWidth = document.body.clientWidth;
    var keep = Math.abs(event.deltaX) < 80;
    event.target.classList.toggle('removed', !keep);

    if (keep) {
      event.target.style.transform = '';
    } else {
      var endX = Math.max(Math.abs(event.velocityX) * moveOutWidth, moveOutWidth);
      var toX = event.deltaX > 0 ? endX : -endX;
      var endY = Math.abs(event.velocityY) * moveOutWidth;
      var toY = event.deltaY > 0 ? endY : -endY;
      var xMulti = event.deltaX * 0.03;
      var yMulti = event.deltaY / 80;
      var rotate = xMulti * yMulti;

      event.target.style.transform = 'translate(' + toX + 'px, ' + (toY + event.deltaY) + 'px) rotate(' + rotate + 'deg)';
      if (event.deltaX > 0) {
        var user = event.target.innerText.split(/\r?\n/)[0];
        var formData = new FormData();
        formData.append('liked-person', user);
        fetch('/like', {
          method: 'POST',
          body: formData
        })
        .then(response => response.json())
        .then(data => console.log('Success:', data))
        .catch(error => console.error('Error:', error));
      }
      initCards();
    }
  });
});

function createButtonListener(love) {
  return function (event) {
    var cards = document.querySelectorAll('.oh--card:not(.removed)');
    var moveOutWidth = document.body.clientWidth * 1.5;

    if (!cards.length) return false;

    var card = cards[0];

    card.classList.add('removed');

    if (love) {
      card.style.transform = 'translate(' + moveOutWidth + 'px, -100px) rotate(-30deg)';
      var user = card.innerText.split(/\r?\n/)[0];
      var formData = new FormData();
      formData.append('liked-person', user);
      fetch('/like', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => console.log('Success:', data))
      .catch(error => console.error('Error:', error));
    } else {
      card.style.transform = 'translate(-' + moveOutWidth + 'px, -100px) rotate(30deg)';
    }

    initCards();

    event.preventDefault();
  };
}

var nopeListener = createButtonListener(false);
var loveListener = createButtonListener(true);

nope.addEventListener('click', nopeListener);
love.addEventListener('click', loveListener);