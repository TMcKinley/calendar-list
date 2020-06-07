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

    //console.log(dataObject);

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

app.listen(port, () =>
  console.log(`Example app listening at http://localhost:${port}`)
);
