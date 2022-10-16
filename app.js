//DB
const Sequelize = require("sequelize");

const sequelize = new Sequelize({
  dialect: "sqlite",
  storage: '/database/burge.db'
});

module.exports = sequelize;
var express = require('express'),
  config = require('./config/config');

const app = express();

/*
app.get('/', function(req, res) {
    res.send("Hello World");
})
*/

require('./config/express')(app, config);

app.listen('3000', function(){
    console.log("Server started on port 3000...")
})