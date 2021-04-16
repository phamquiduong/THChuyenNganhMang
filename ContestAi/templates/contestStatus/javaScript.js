window.onload = function () {
  var chart = new CanvasJS.Chart("chartContainer", {
    title: {
      text: "Number Participant",
    },
    axisY: {
      minimum: 0
    },
    data: [
      {
        type: "column",
        dataPoints: [
          { label: "Registed", y: {{inRegis}} },
          { label: "Todo", y: {{inTodo}} },
          { label: "Has result", y: {{inResult}} },
        ],
      },
    ],
  });
  chart.render();
};
