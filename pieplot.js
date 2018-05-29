function init() {
  var data = [{
    values: [11, 9, 3, 2, 1, 0, 0, 0],
    labels: ["Biography", "Drama", "Comedy", "Crime", "Action", "Adventure", "Sci-fi", "Western"],
    colors: ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800080", "#C5B358", "#FF1493"],
    textfont: {size:28, color:"#FFFFFF"},
    hoverinfo:"label+percent", 
    textinfo:"label",     
    type: "pie"
  }];

  var layout = {
    height: 700,
    width: 800,
    
   };

  Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata) {
  var PIE = document.getElementById("pie");
  Plotly.restyle(PIE, "values", [newdata]);
}

function getData(dataset) {
  var data = [];
  switch (dataset) {
    case "datasetActor":
      data = [11, 9, 3, 2, 1, 0, 0, 0];
      break;
    case "datasetActress":
      data = [8, 11, 4, 3, 0, 0, 0, 0];    
      break;
    case "datasetDirector":
      data = [5, 9, 3, 3, 1, 3, 1, 1];
      break;
    case "datasetMovie":
      data = [6, 9, 4, 3, 1, 2, 0, 1];
      break;
    default:
      data = [11, 9, 3, 2, 1, 0, 0, 0];
  }
  updatePlotly(data);
}

init();


