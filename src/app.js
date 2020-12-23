const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

function dbcall(){
    var pg = require("pg");
    var connectionString = "postgres://postgres:mango@postgres/localhost:5432/postgres";
    var pgClient = new pg.Client(connectionString);
    pgClient.connect();
    var query = pgClient.query("SELECT * FROM cars;");
    document.getElementById("main").innerHTML = query;
    console.log("sending");

    let something = "Hello world 2"
    document.getElementById("second").innerHTML = something;
}

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});