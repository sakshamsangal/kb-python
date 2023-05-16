# open cmd

```bash
npm start
ctrl c
npm init --yes
npm install express --save
npm install body-parser --save
npm install mongoose --save



npm install nodemon --save
nodemon --exec npm start (infinite server)
npm install cors

```

```javascript
./models/student.js 
===================================================
const mongoose = require('mongoose')
const x = mongoose.Schema

const schema = new x({
    email: String,
    password: String
})

module.exports = mongoose.model('students', schema)


./routes/api 
===================================================
const express = require("express");
const router = express.Router();
const mongoose = require("mongoose");
const model = require("../models/student");
const db = "mongodb://localhost:27017/college";

mongoose.connect(
  db,
  {
    useNewUrlParser: true
  },
  err => {
    if (err) throw err;
    console.log("mongodb connected");
  }
);
router.post("/post", (req, res) => {
  arr = req.body;
  x = new model(arr);
  x.save((err, data) => {
    if (err) throw err;
    res.json(data);
  });
});

router.get("/", (req, res) => {
    res.send("Hello! This is api");
});
router.get("/get", (req, res) => {
  model.find({}).exec((err, data) => {
    if (err) throw err;
    res.json(data);
  });
});

router.get("/getOne/:id", (req, res) => {
  model.findById(req.params.id).exec((err, data) => {
    if (err) throw err;
    res.json(data);
  });
});

router.put("/put/:id", (req, res) => {
  model.findByIdAndUpdate(
    req.params.id,
    {
      $set: {
        email: req.body.email,
        password: req.body.password
      }
    },
    {
      new: true
    },
    (err, data) => {
      if (err) throw err;
      res.json(data);
    }
  );
});
router.delete("/delete/:id", (req, res) => {
  model.findByIdAndRemove(req.params.id, (err, data) => {
    if (err) throw err;
    res.json(data);
  });
});

module.exports = router;

./server.js
===================================================
const express = require('express');
const bodyParser = require('body-parser');
const api = require('./routes/api');
const port = 3000;
const app = express();


app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/api', api);

app.get('/', (req, res) => {
    res.send("Experess Server");
});

app.listen(port, function(){
    console.log("Server running on localhost:" + port);
});
