function fullnamecheck(){

	var name=document.getElementById('err_full_name');
	var entireName=document.register.entireName;
	var returnValue = /^[A-Za-z ]{1,50}$/;
	 if(entireName.value.length>0){
		name.innerHTML="";
	 	if(returnValue.test(entireName.value))
	 	{
			name.innerHTML="";
	 	}

	 	else{
			name.innerHTML="Enter Valid Name - Alphabets only with a maximum length of 50 charecters";
	 	}

	 }
	 	else{
			name.innerHTML="This cannot be blank";
	 	}

     }
     


     function loginEmailcheck(){

		var emailSent=document.getElementById('err_login_email');
		var emailValue=document.login.emailValue;
		var regex = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/;
		if(emailValue.value.length>0){
			emailSent.innerHTML="";
			if(regex.test(emailValue.value))
			{
				emailSent.innerHTML="";
			}
	
			else{
				emailSent.innerHTML="Enter Valid Email - All lowercase & Alphanumeric - something@something.domain";
			}
	
		}
			else{
				emailSent.innerHTML="This cannot be blank";
			}
	
	
		}
	
	
	function loginPasswordcheck(){
	
		var pass=document.getElementById('err_login_password');
		var passwordSend=document.login.passwordSend;
		var regex = /^.{8,10}$/;
			if(passwordSend.value.length>0){
				pass.innerHTML="";
				if(regex.test(passwordSend.value))
				{
					pass.innerHTML="";
				}
	
				else{
					pass.innerHTML="Must contain at least 8 to at most 10 charecters (including special charecters)";
				}
	
			}
				else{
					pass.innerHTML="This cannot be blank";
				}
	
	
			}



			function numberCheck(){
	
				var pass=document.getElementById('err_login_password');
				var passwordSend=document.login.passwordSend;
				var regex = /^.{10}$/;
					if(passwordSend.value.length>0){
						pass.innerHTML="";
						if(regex.test(passwordSend.value))
						{
							pass.innerHTML="";
						}
			
						else{
							pass.innerHTML="Must contain 10 charecter";
						}
			
					}
						else{
							pass.innerHTML="This cannot be blank";
						}
	
			}