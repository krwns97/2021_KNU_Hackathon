const express = require('express')

const app = express()
const mongoose = require('mongoose')

const HomeController = require('./controllers/home')
const VerificationController = require('./controllers/verification')

app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.use(express.static('public'))

mongoose.connect('mongodb://localhost:27017/my_database', {
    useUnifiedTopology: true,
    useNewUrlParser: true,
    useCreateIndex: true    
});

app.get('/', HomeController);
app.post('/verification', VerificationController);

app.listen(4000, () => console.log('Listening on port 4000!'))
