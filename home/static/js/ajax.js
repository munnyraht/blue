// **
//  * This javascript script allows to work transparently requests that require 
//  * protection of the CSRF token through AJAX JQUERY.
//  * This will allow you to make requests to Django web Services through AJAX Jquery.
//  * To use it, simply integrate the DjangoAjax.js file into your JS directory and refer to it in your templates 
//  * that require the use of AJAX by POST or some other that requires the CSRF token.
//  * This script is based on the official documentation of Django https://docs.djangoproject.com
//  * 

$ ( function () {
    // We obtain the information of csfrtoken that is stored by cookies in the client
    var csrftoken =  getCookie ( ' csrftoken ' );

    // We add the following in the configuration of the $ .ajax function of Jquery:
    $ . ajaxSetup ({
                    beforeSend :  function ( xhr , settings ) {
                        if ( ! csrfSafeMethod ( settings . type ) &&  sameOrigin ( settings . url )) {
                            // Send the token to same-origin, relative URLs only.
                            // Send the token only if the method warrants CSRF protection
                            // Using the CSRFToken value acquired earlier
                            xhr . setRequestHeader ( " X-CSRFToken " , csrftoken);
                        }
                    }
    });

function  sameOrigin ( url ) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host =  document . location . host ; // host + port
    var protocol =  document . location . protocol ;
    var sr_origin =  ' // '  + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin ||  url . slice ( 0 , origin . length  +  1 ) == origin +  ' / ' ) ||
        (url == sr_origin ||  url . slice ( 0 , sr_origin . length  +  1 ) == sr_origin +  ' / ' ) ||
        // or any other URL that is not relative or absolute relative.
        ! ( / ^ ( \ / \ / | http: | https :) . * / . test (url));
}

// using jQuery
function  getCookie ( name ) {
    var cookieValue =  null ;
    if ( document . cookie  &&  document . cookie  ! =  ' ' ) {
        var cookies =  document . cookie . split ( ' ; ' );
        for ( var i =  0 ; i <  cookies . length ; i ++ ) {
            var cookie =  jQuery . trim (cookies [i]);
            // Does this cookie string begin with the name we want?
            if ( cookie . substring ( 0 , name . length  +  1 ) == (name +  ' = ' )) {
                CookieValue =  decodeURIComponent ( cookie . substring ( name . length  +  1 ));
                break ;
            }
        }
    }
    return cookieValue;
}


    function  csrfSafeMethod ( method ) {
        // these methods do not require CSRF
        return ( / ^ (GET | HEAD | OPTIONS | TRACE) $ / . test (method));
    }
});