$(document).ready(function(){
					    $('#submit').on('click', function(){
					        $bankname = $('#bankname').val();
					        $accountnumber = $('#accountnumber').val();
					        $highestlevelofeducation = $('#highestlevelofeducation').val();
					        $employmentstatus = $('#employmentstatus').val();
					        $currentemployer = $('#currentemployer').val();
					        $employeraddress = $('#employeraddress').val();
					        $landmark = $('#landmark').val();
					        $income = $('#income').val();
					        $netincome = $('#netincome').val();

					        if($accountnumber == ""){
					            alert("Please complete field");
					        }else{
					            $.ajax({
					                type: "POST",
					                url: '/createemploymentinfo',
					                data:{
					                    bankname: $bankname,
					                    accountnumber: $accountnumber,
					                    highestlevelofeducation: $highestlevelofeducation,
					                    employmentstatus: $employmentstatus,
					                    currentemployer: $currentemployer,
					        			employeraddress:  $employeraddress,
					                    landmark: $landmark,
					                    income: $income,
					                    netincome: $netincome,
					                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
					                },
					                success: function(data){
					                    alert("Next of kin Data have been saved");
				                    // $('#nextofkinemail').val('');
				                    window.location = "{% url 'employmentinfo' %}";
					                }
					            });
					        }
					    });
					});
