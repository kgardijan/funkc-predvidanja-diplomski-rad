import express from 'express';
import bodyParser from 'body-parser';
import axios from 'axios';
import cors from 'cors';

const app = express();
const port = 3000;

app.use(cors())

app.use(express.json())
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs')

const inputData = {
    "Inputs": {
      "input1": []
    },
    "GlobalParameters": {}
  }

app.get('/', function(req, res){
    const predictionResult = {}
    res.render('pages/index');
})


app.post('/predict', async (req, res) => {

    const inputData = {
        "Inputs": {
          "input1": [req.body]
        },
        "GlobalParameters": {}
      }
    console.log(req.body)

    const response = await axios.post("http://127.0.0.1:8000/prediction", inputData);
    console.log(response.data.Results.WebServiceOutput0[0])
    const predictionResult = response.data.Results.WebServiceOutput0[0]
    res.render("pages/prediction.ejs", { predictionResult });
    
});

app.listen(port, () => {
    console.log(`Server is running on port http://localhost:${port}`);
});
