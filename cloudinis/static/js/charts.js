

var ctx1 = document.getElementById('chart1').getContext('2d');
var myChart = new Chart(ctx1, {
    type: 'doughnut',
    data: {
        labels: ['Fixed', 'Not Fixed'],
        datasets: [{
           // data: [20, 9],
            data:data11,
            backgroundColor: [
                'rgba(0,255,127, 0.8)',
                'rgba(255, 99, 132, 0.8)',

            ],
            borderColor: [
                'rgb(8,122,55)',
                'rgb(125,50,60)',

            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive:true,
        maintainAspectRatio: false,

    }
});




var ctx2 = document.getElementById('chart2').getContext('2d');
var myChart = new Chart(ctx2, {
    type: 'bar',
    data: {
        // labels: ['PolicyA', 'PolicyB', 'PolicyC', 'PolicyD', 'PolicyE', 'PolicyF', 'PolicyG', 'PolicyH'],
        labels:labels22,
        datasets: [{
            label: 'my policies',
            // data: [3, 4, 80, 0, 105, 40, 50,10],
            data: data22,
            backgroundColor: 'rgb(73,180,192)',
            borderColor: 'rgb(54,99,146)',
            borderWidth: 1
        }]
    },
    options: {
        responsive:true,
        maintainAspectRatio: false,

    }
});

var ctx3 = document.getElementById('chart3').getContext('2d');
var myChart = new Chart(ctx3, {
    type: 'line',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'],
        datasets: [{
            label: 'violations',
            data: [5, 4, 3, 8, 10, 1, 12,10, 1,6,30,12],
            backgroundColor: 'rgba(76,194,194,0.6)',
            borderColor: 'rgb(47,120,120)',
            borderWidth: 2,
            fill: false
        }]
    },
    options: {
        responsive:true,
        maintainAspectRatio: false,

    }
});


var ctx4 = document.getElementById('chart4').getContext('2d');
var myChart = new Chart(ctx4, {
    type: 'pie',
    data: {
        labels: ['S3', 'EC2', 'anotherResource', 'anotherResource2', 'anotherResource3'],
        datasets: [{
            label: 'Resources',
            data: [10, 40, 5, 18, 10],
            backgroundColor: [
                'rgba(255,99,132,0.8)',
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 206, 86, 0.8)',
                'rgba(67,192,76,0.8)',
                'rgba(153, 102, 255, 0.8)',
                'rgba(255, 159, 64, 0.8)'
            ],
            borderColor: [
                'rgb(156,55,88)',
                'rgb(37,112,156)',
                'rgb(156,126,53)',
                'rgb(66,156,72)',
                'rgb(101,55,156)',
                'rgb(156,98,38)'
            ],
            borderWidth: 1,
            fill: false
        }]
    },
    options: {
        responsive:true,
        maintainAspectRatio: false,

    }
});