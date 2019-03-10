// */
// 	function validate(){
// 		var username = document.getElementById("username").value;
// 		var password = document.getElementById("password").value;
// 	}

// 	$("#submit").click(function(){
// 		var hasError = false;
// 		var passwordValue = $("#password").val();
// 		var userNameValue = $("#username").val();

// 		if(passwordValue == '' && userNameValue == ''){
// 			$("#submit").on("click", function(){
// 				$(this).after('<div id="error2">The username you entered doesnt belong to an account. Please check your username and try again.</div>');
// 				$(this).off();
// 			});
// 			hasError = true;
// 		} else if (passwordValue == ''){
// 			$("#submit").on("click", function(){
// 				$(this).after('<div id="error1">Sorry, your password was incorrect. Please double-check your password.</div>');
// 				$(this).off();
// 			});
// 			hasError = true;
// 		} else if (userNameValue == ''){
// 			$("#submit").on("click", function(){
// 				$(this).after('<div id="error2">The username you entered doesnt belong to an account. Please check your username and try again.</div>');
// 			});
// 			hasError = true;
// 		}
// 	//	if(hasError == true){ return false;}
// });
// });
