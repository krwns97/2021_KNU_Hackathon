//node-rest-client호출
var Client = require('node-rest-client').Client;
var client = new Client();

// content-type header 를 json타입으로 지정. 
// 2명 왔고 2명다 리스트에 있는 경우
// var args = {
//   data: { "bluetooth" : ["A8:2B:B9:86:03:15", "48:4B:AA:5A:81:C6"], "time": "7/21 14:20", "location" : "403" },
//   headers: { "Content-Type": "application/json" }
// };
// 2명 왔고 1명만 리스트에 있는 경우
var args = {
    data: { "bluetooth" : ["A8:2B:B9:86:03:15", "adfaf"], "time": "7/21 14:20", "location" : "403" },
    headers: { "Content-Type": "application/json" }
  };
// 2명 왔고 아무도 리스트에 없는 경우
// var args = {
//     data: { "bluetooth" : ["qwer", "adfaf"], "time": "7/21 14:20", "location" : "403" },
//     headers: { "Content-Type": "application/json" }
//   };

//1. 등록없이 바로 사용
client.post("http://localhost:4000/verification", args, function (data, response) {
  // js object로 파싱된 객체 
  console.log(data);
  console.log(JSON.stringify(data));
  // 응답 객체
//   console.log(response);
});
