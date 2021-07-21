const mongoose = require('mongoose')
const Schema = mongoose.Schema;
 
const StudentInformationSchema = new Schema({
  이름: String,
  학번: String,
  블루투스ID: String,
});

const StudentInformation = mongoose.model('StudentInformation',StudentInformationSchema);
module.exports = StudentInformation