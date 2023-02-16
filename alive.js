const express = require('express');
const app = express();
const PORT = 6969;

app.get('/', (req, res) => {

  res.send('stfu')

  
})

app.listen(PORT, ()=>{
  console.log(PORT)
})
