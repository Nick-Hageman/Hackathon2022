const Burge = require("../../app/models/burge");

async function accessDB() {
    //const test = await Burge.findAll();
      let Foods = await Moisture.findAll({
        where : {
          //Not Null
        }
      })
      //Create array for each plant
    console.log(Foods);
  }
  accessDB();