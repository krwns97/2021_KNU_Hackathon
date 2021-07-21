const AccessRecord = require('../models/AccessRecord.js')
const StudentInformation = require('../models/StudentInformation.js')

module.exports = async (req, res) =>{
    // var body = req.body;
    // console.log(body);

    var bluetooth = req.body.bluetooth
    var students = []

    for(var i=0;i<bluetooth.length;i++){
        const student = await StudentInformation.find({"블루투스ID": bluetooth[i]}) 
        // console.log(student);
        if(student.length > 0){
            students.push(student[0]);
        }
    }
    console.log(students)

    for(var i=0;i<students.length;i++){
        var newAccessRecord = new AccessRecord(
            {
                이름: students[i]["이름"],
                학번: students[i]["학번"],
                건물번호: req.body.location,
                시간: req.body.time
            });
        
        newAccessRecord.save(function (error, data) {
            if (error) {
                console.log(error);
            } else {
                // console.log(students[i]["이름"] + ' Saved!')
                console.log('Save')
            }
        });
    }

    if(students.length == 0){
        res.send("0");
    }else{
        res.send("11");
    }
}