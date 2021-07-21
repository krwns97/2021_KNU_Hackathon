const mongoose = require('mongoose')
const Schema = mongoose.Schema;
 
const AccessRecordSchema = new Schema({
  이름: String,
  학번: String,
  건물번호: String,
  시간: String
});

const AccessRecord = mongoose.model('AccessRecord',AccessRecordSchema);
module.exports = AccessRecord