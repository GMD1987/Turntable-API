/**
 * Automatically vote up on a song when 2 people say "bop"!
 * It's not against the turntable.fm policy to do so...
 * Reccomended for rooms with more people in it!
 */

var Bot    = require('ttapi');
var AUTH   = 'xxxxxxxxxxxxxxxxxxxxxxxx';
var USERID = 'xxxxxxxxxxxxxxxxxxxxxxxx';
var ROOMID = 'xxxxxxxxxxxxxxxxxxxxxxxx';

var bot = new Bot(AUTH, USERID, ROOMID);

bopcount = 0;

bot.on('speak', function (data) {
  var text = data.text;

  // Any command with "bop" in it will work (ex: "bop","bop i beg you!!!","lolbopbaby", etc.)
  if (text.match(/bop/)) {
    bopcount += 1;
  }

  // And when the bopcount reaches two...
  if (bopcount == 2) {
    bot.vote('up');
  }
});

// Reset bopcount per new song
bot.on('newsong', function (data) {
  bopcount = 0;
});
