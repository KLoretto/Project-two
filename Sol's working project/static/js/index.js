// Get references to the elements of the DOM
var $tbody = document.querySelector("tbody");
var $ceremonyInput = document.querySelector("#ceremony");
var $yearInput = document.querySelector("#year");
var $awardInput = document.querySelector("#award");
var $genreInput = document.querySelector("#genre"); 
var $searchBtn = document.querySelector("#search");
var $recordCounter = document.querySelector("#recordCounter");
var $pages = document.querySelector("#pages");
var $loadBtn = document.querySelector("#load");
var $nextBtn = document.querySelector("#next");
var $prevBtn = document.querySelector("#prev");

// Add event listeners
$searchBtn.addEventListener("click", handleSearchButtonClick);
$loadBtn.addEventListener("click", handleReloadButtonClick);
$nextBtn.addEventListener("click", handleNextButtonClick);
$prevBtn.addEventListener("click", handlePrevButtonClick);
$pages.addEventListener("change", handlePagesChange);

// Initialize global variables
var filteredData = dataSet;
var count = 0;

// Define Event handler functions

// handleNextButtonClick increments count and renders
function handleNextButtonClick() {
    count++;
    renderTable();
}
// handlePrevButtonClick decrements count and renders
function handlePrevButtonClick() {
    count--;
    renderTable();
}

// handlePagesChange renders for new record count selected
function handlePagesChange() {
    renderTable();
}

// handleSearchButtonClick search button click:

function handleSearchButtonClick() {
    var filterCer = $ceremonyInput.value;
    var filterYear = $yearInput.value;
    var filterAward = $awardInput.value;
    var filterGenre = $genreInput.value;

    if (filterCer != "") {
        filteredData = filteredData.filter(function (ceremony) {
        var dataCer = ceremony.Ceremony;
        return dataCer === filterCer;
    });

    }

    if (filterYear != "") {
        filteredData = filteredData.filter(function (year) {
            var dataYear = year.Year;
            return dataYear === filterYear;
    });
    }

    if (filterAward != "") {
        filteredData = filteredData.filter(function (award) {
            var dataAward = award.Award;
            return dataAward === filterAward;
        });
    }

    if (filterGenre != "") {
        filteredData = filteredData.filter(function (genre) {
            var dataGenre= genre.Genre;
            return dataGenre === filterGenre;
        });
    }


    renderTable();
}

// handleReloadButtonClick resets count and search fields, and renders
function handleReloadButtonClick() {
    count = 0;
    filteredData = dataSet;
    $ceremonyInput.value = '';
    $yearInput.value = '';
    $awardInput.value = '';
    $genreInput.value = '';

    renderTable();
}

// Define renderTable function
function renderTable() {
    // clear previously rendered table
    $tbody.innerHTML = "";

    // Get number of records to be rendered
    var pages = Number(document.getElementById("pages").value);

    // Initialize local variables
    var start = count * pages + 1;
    var end = start + pages - 1;
    var btn;

    // Adjusts records displayed for end of data and state of Next button
    if (end > filteredData.length) {
      end = filteredData.length;
      btn = document.getElementById("next");
      btn.disabled = true;
    }
    else {
      btn = document.getElementById("next");
      btn.disabled = false;
    }

    // Adjusts state of Previous button
    if (start == 1) {
      btn = document.getElementById("prev");
      btn.disabled = true;
    }
    else {
      btn = document.getElementById("prev");
      btn.disabled = false;
    }

    // Displays record counts and loads records into table
    $recordCounter.innerText = "From Record: " + start + " to: " + end + " of " + filteredData.length;
    // Outer loop loads specified number of records
    for (var i = 0; i < pages; i++) {
        var item = filteredData[i+(count * pages)];
        var fields = Object.keys(item);
        var $row = $tbody.insertRow(i);
        // Inner loop loads fields in record
        for (var j = 0; j < fields.length; j++) {
            var field = fields[j];
            var $cell = $row.insertCell(j);
            $cell.innerText = item[field];
        }
    }
}

// Provides initial render on open
renderTable();
