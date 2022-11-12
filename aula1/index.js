const axios = require('axios')

const news = require("./news.json");

// news.forEach(item => { console.log(item.Title) })

axios.get('hps://api.github.com/users/GarciaGP/repos').then(res => { console.log(res.data) }).catch(err => { console.log("Something went wrong") })