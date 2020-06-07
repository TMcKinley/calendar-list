const fs = require("fs");

const express = require("express");
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use("/", express.static("../dist"));

app.post("/api/save", (req, res) => {
  fs.readFile("../dist/eventlist.json", "utf8", function(err, data) {
    if (err) {
      return console.log(err);
    }

    let dataArray = JSON.parse(data);
    let dataObject = dataArray.find(obj => obj.id === req.body.id);
    dataObject.completed = 1;

    fs.writeFile(
      "../dist/eventlist.json",
      JSON.stringify(dataArray),
      "utf8",
      function(err) {
        if (err) {
          return console.log(err);
        }

        return res.json(req.body);
      }
    );
  });
});

app.post("/api/reset", (req, res) => {
  fs.readFile("../dist/eventlist.json", "utf8", function(err, data) {
    if (err) {
      return console.log(err);
    }

    let dataArray = JSON.parse(data);
    let filteredArray = dataArray.map(obj => {
      obj.completed = 0;

      return obj;
    });

    fs.writeFile(
      "../dist/eventlist.json",
      JSON.stringify(filteredArray),
      "utf8",
      function(err) {
        if (err) {
          return console.log(err);
        }

        return res.json({ success: true });
      }
    );
  });
});

app.listen(port, () =>
  console.log(`Example app listening at http://localhost:${port}`)
);
