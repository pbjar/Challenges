var express = require("express");
var app = express();
app.listen(3000, () => {
 console.log("Server running on port 3000");
});
const cors = require('cors');
app.use(cors());
//app.options('*', cors());


app.use(function (req, res, next) {
    if (req.ip !== '::ffff:127.0.0.1') { // Wrong IP address
      res.status(401);
      return res.send(req.ip);
    }
    return res.send("flag{re@l_unpr0tected_functi0ns}");

  });
  