const express = require('express'),
  router = express.Router();
const Burge = require("../models/burge.js");

module.exports = function (app) {
    app.use('/data', router);
};

/*
async function accessDB() {
    const users = await Burge.findAll();
    console.log(users.every(user => user instanceof Burge)); // true
    console.log("All users:", JSON.stringify(users, null, 2));

    router.get('/', function(req, res, next) {
        res.json({ FOODS: users });
    });
}
*/
router.get('/', function(req, res, next) {
    res.json({ value: 1 });
  }) ;