$(document).ready(function(){
				    $('#submit').on('click', function(){
				        $nextofkinname = $('#nextofkinname').val();
				        $nextofkinrelationship = $('#nextofkinrelationship').val();
				        $nextofkinaddress = $('#nextofkinaddress').val();
				        $nextofkinphone = $('#nextofkinphone').val();
				        $nextofkinemail = $('#nextofkinemail').val();
				        $landmark = $('#landmark').val();
				        $income = $('#income').val();


				        if($nextofkinemail == ""){
				            alert("Please complete field");
				        }else{
				            $.ajax({
				                type: "POST",
				                url: '/createnextofkin',
				                data:{
				                    nextofkinrelationship: $nextofkinrelationship,
				                    nextofkinname: $nextofkinname,
				                    nextofkinaddress: $nextofkinaddress,
				                    nextofkinphone: $nextofkinphone,
				                    nextofkinemail: $nextofkinemail,
				                    landmark: $landmark,
				                    income: $income,
				                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

				                },
				                success: function(data){
				                    alert("Data have been saved");
				                    // $('#nextofkinemail').val('');
				                    window.location = "/paymentinfo/employmentinfo.html";
				                }
				            });
				        }
				    });
				});