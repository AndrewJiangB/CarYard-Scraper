var pg = require("pg");
var connectionString = "postgres://postgres:mango@postgres/localhost:5432/postgres";
var pgClient = new pg.Client(connectionString);
pgClient.connect();
var query = pgClient.query("SELECT * FROM cars;");
document.getElementById("main").innerHTML = query;
console.log("sending");

let something = "Hello world 2"
document.getElementById("second").innerHTML = something;