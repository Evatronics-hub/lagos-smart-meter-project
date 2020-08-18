window.config = {
  type: 'line',
  data: {
    datasets: [{
      data: [0, 0, 0, 0, 0],
	  fillColor : "rgba(220,220,220,0.5)",
	  strokeColor : "rgba(220,220,220,1)",
	  pointColor : "rgba(220,220,220,1)",
	  pointStrokeColor : "#fff",
      backgroundColor: [
        '#00E01C', '#8BFF0D', '#FFEA0D', '#FF650D', '#FF0D61'
      ],
      label: 'Usage'
    }
	],
    labels: ['1','2', '3', '4', '5']
  },
  options: {
    responsive: true
  }
};

window.socket = new WebSocket('ws://localhost:8000/chart')
window.ctx = document.getElementById('myChart').getContext('2d');
window.myPie = new Chart(ctx, config);

socket.onopen = (e) => {
    console.log('Connected to server')
}

socket.onclose = (e) => {
  console.log('Disconnected', e)
}

socket.onmessage = function(e) {
    var data = JSON.parse(e.data)
    config.data.datasets[0].data = data
    myPie.update()
}




// var ctx = document.getElementById('myChart').getContext('2d');
// window.myPie = new Chart(ctx, config);