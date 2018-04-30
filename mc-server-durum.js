const Discord = require('discord.js');
const client = new Discord.Client();
client.login('token');

var request = require('request');
var mcCommand = '/minecraft';
var mcIP = '123.123.123.123'; // server ip'si
var mcPort = 1234; // Port

client.on('message', message => {
    if (message.content === mcCommand) {
        var url = 'http://mcapi.us/server/status?ip=' + mcIP + '&port=' + mcPort;
        request(url, function(err, response, body) {
            if(err) {
                console.log(err);
                return message.reply('Serverin bilgisini alırken bir hata ile karşılaşıldı...');
            }
            body = JSON.parse(body);
            var durum = '*Server kapalı.*';
            if(body.online) {
                durum = '**Minecraft** serveri **online**  -  ';
                if(body.players.now) {
                    durum += '**' + body.players.now + '** içeride!';
                } else {
                    durum += '*Kimse oynamıyor!*';
                }
            }
            message.reply(durum);
        });
    }
});
