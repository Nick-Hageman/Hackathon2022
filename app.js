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

console.log('Starting up on: ' + config.port);
app.listen(config.port);