```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Expense manager</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
  </head>
  <body>
    <body>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid"><a class="navbar-brand" href="#">Expense</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                      aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"><span
                      class="navbar-toggler-icon"></span></button>
              <div class="collapse navbar-collapse" id="navbarNav">
                  <ul class="navbar-nav">
                      <li class="nav-item"><a class="nav-link active" href="#">Home</a>
                      </li>
                  </ul>
              </div>
          </div>
      </nav>
    <div class="container mt-1">
      <div class="row">
        <div class="col-md-4">
          <form onsubmit="onFormSubmit()">
            <div>
              <label for="date">Date</label>
              <input type="text" name="date" id="date" />
              <button type="button" class="btn btn-primary btn-sm" onclick="getMyDate()">
                get current date
              </button>
            </div>
            <div>
              <label for="sum">sum</label>
              <input type="number" readonly value="0" id="sum" />
            </div>
            <div>
              <label for="product">Item</label>
              <input type="text" name="product" autofocus id="product" autocomplete="off"/>
            </div>
            <div>
              <label for="perPrice">Price</label>
              <input type="number" name="perPrice" id="perPrice" style="font-size: 4rem; width:250px" required/>
            </div>
  
            <button type="submit" class="btn btn-primary btn-sm">Submit</button>
            <button type="button" class="btn btn-primary btn-sm" onclick="export2csv()">CSV</button>
          </form>
        </div>
        <div class="col-md-4">
          <table class="table table-sm table-bordered" id="storeList">
            <thead>
              <tr>
                <th>Item</th>
                <th>Price</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
        <div class="col-md-4">
          <textarea id="csv" cols="40" rows="10"></textarea>
        </div>
      </div>
    </div>
    <script type="text/javascript" src="./script.js"></script>

  </body>
</html>
```

```javascript
var selectedRow = null;
var my_sum = document.getElementById("sum");
var y = document.getElementById("product");


function onFormSubmit(e) {
  event.preventDefault();
  var formData = readFormData();
  if (selectedRow == null) {
    insertNewRecord(formData);
  } else {
    updateRecord(formData);
  }
  resetForm();
}

//Retrieve the data
function readFormData() {
  var formData = {};
  formData["product"] = y.value;
  formData["perPrice"] = document.getElementById("perPrice").value;
  return formData;
}

//Insert the data
function insertNewRecord(data) {
  var table = document
    .getElementById("storeList")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.length);
  cell2 = newRow.insertCell(0);
  cell2.innerHTML = data.product;
  cell4 = newRow.insertCell(1);
  cell4.innerHTML = data.perPrice;
  cell4 = newRow.insertCell(2);
  sum.value = parseInt(sum.value) + parseInt(data.perPrice);
  cell4.innerHTML = `<button onClick="onEdit(this)" class="btn btn-primary btn-sm" >Edit</button> <button onClick="onDelete(this)" class="btn btn-primary btn-sm" >Delete</button>`;
  y.focus();
}
var temp = 0;
//Edit the data
function onEdit(td) {
  selectedRow = td.parentElement.parentElement;
  y.value = selectedRow.cells[0].innerHTML;
  document.getElementById("perPrice").value = selectedRow.cells[1].innerHTML;
  temp = parseInt(selectedRow.cells[1].innerText);
  y.focus();
}
function updateRecord(formData) {
  selectedRow.cells[0].innerHTML = formData.product;
  selectedRow.cells[1].innerHTML = formData.perPrice;
  sum.value = parseInt(sum.value) + parseInt(formData.perPrice) - temp;
  y.focus();
}

//Delete the data
function onDelete(td) {
  if (confirm("Do you want to delete this record?")) {
    row = td.parentElement.parentElement;
    document.getElementById("storeList").deleteRow(row.rowIndex);
    sum.value = parseInt(sum.value) - parseInt(row.cells[1].innerText);
    resetForm();
    y.focus();
  }
}

//Reset the data
function resetForm() {
  y.value = "";
  document.getElementById("perPrice").value = "";
  selectedRow = null;
}

function export2csv() {
  let data = "";
  x = document.getElementById("date").value;
  const tableData = [];
  const rows = document.querySelectorAll("table tr");
  for (const row of rows) {
    const rowData = [];
    for (const [index, column] of row.querySelectorAll("th, td").entries()) {
      // To retain the commas in the "Description" column, we can enclose those fields in quotation marks.
      // console.log(index, column, column.tagName)
      if (column.tagName === "TH") {
        continue;
      } else if ((index + 1) % 3 === 0) {
        rowData.push('"' + x + '"');
      } else if (index % 3 === 0) {
        rowData.push('"' + column.innerText + '"');
      } else {
        rowData.push(column.innerText);
      }
    }
    tableData.push(rowData.join(","));
  }
  data += tableData.join("\n");
  document.getElementById("csv").value = data;
}

getMyDate();
function getMyDate() {
  const mth = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  var currentDate = new Date();
  var day = currentDate.getDate();
  var month = mth[currentDate.getMonth()];
  var year = currentDate.getFullYear();
  document.getElementById("date").value = day + "-" + month + "-" + year;
}
```