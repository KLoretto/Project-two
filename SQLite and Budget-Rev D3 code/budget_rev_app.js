var margin = {top: 20, right: 20, bottom: 50, left: 110},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scaleLinear()
    .range([0, width]);

var y = d3.scaleLinear()
    .range([height, 0]);

var color = d3.scaleOrdinal(d3.schemeCategory10);

var xAxis = d3.axisBottom(x);

var yAxis = d3.axisLeft(y);

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.csv("best_picture.csv", function(error, data) {
  if (error) throw error;

  data.forEach(function(d) {
    d.budget = +d.budget;
    d.revenue = +d.revenue;
  });

  x.domain(d3.extent(data, function(d) { return d.budget; })).nice();
  y.domain(d3.extent(data, function(d) { return d.revenue; })).nice();

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .append("text")
      .attr("class", "label")
      .attr("x", width)
      .attr("y", -6)
      .style("text-anchor", "end")
      .text("Sepal Width (cm)");

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Sepal Length (cm)")

  var toolTip = d3.select("body")
      .append("div")
      .style("display", "none")
      .classed("tooltip", true)

  var chart = svg.selectAll(".dot")
      .data(data)
    .enter().append("circle")
      .attr("class", "dot")
      .attr("r", 8)
      .attr("cx", function(d) { return x(d.budget); })
      .attr("cy", function(d) { return y(d.revenue); })
      .style("fill", "black")
      
      
      chart.on("mouseover", function (d) {
        toolTip.style("display", "block")
          .html(
            `<strong> Title - ${d.title}<br> Budget - ${d.budget}<br> Revenue - ${d.revenue}<strong>`)
          .style("left", d3.event.pageX + "px")
          .style("top", d3.event.pageY + "px")
      })
      .on("mouseout", function () {
        toolTip.style("display", "none")
      });
  
      

  svg.append("text")             
      .attr("transform",
            "translate(" + (width/2) + " ," + 
                           (height + margin.top + 20) + ")")
      .style("text-anchor", "middle")
      .text("Movie Budget");  
  
  svg.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left)
      .attr("x",0 - (height / 2))
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text("Gross Revenue"); 

});