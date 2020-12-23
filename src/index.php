<?
function pg_connect_db(){      
        $dbconn = pg_connect("dbname=postgres user=postgres host=localhost password=mango");
        pg_set_client_encoding($dbconn, 'UTF8');
        return $dbconn;
}
?>