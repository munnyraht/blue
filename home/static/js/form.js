function validform() {

        
        var email = document.forms["login_form"]["email-address"].value;
        var password = document.forms["login_form"]["password"].value;
        

        if (email==null || email=="")    
        {
            alert("Please Enter Your Email Address");
            return false;
        }else if (password==null || password=="")
        {
            alert("Please Enter Your password");
            return false;
        }
        

    }