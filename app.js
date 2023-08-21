const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.urlencoded({ extended: false }));

// Handle form submission for food providers
fetch('https://15.206.68.176/cgi-bin/app.py', (method: 'POST', body: formData))
app.post('/food-provider', (req, res) => {
  const name = req.body.name;
  const email = req.body.email;
  const phone = req.body.phone;
  const address = req.body.address;
  const quantity = req.body.quantity;
  const type = req.body.type;
  // Save the form data to a database or send an email to the appropriate party
  // Return a response to the client indicating success or failure
});

// Handle form submission for volunteers
fetch('https://15.206.68.176/cgi-bin/app.py', (method: 'POST', body: formData))
app.post('/volunteer', (req, res) => {
  const name = req.body.name;
  const email = req.body.email;
  const phone = req.body.phone;
  // Save the form data to a database or send an email to the appropriate party
  // Return a response to the client indicating success or failure
res.redirect(__dirname + '/success.html');
});

app.listen(3000, () => {
  console.log('Server started on port 5500');
});
