// JavaScript Document
var emailpattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,3})|(([a-zA-Z]{2,3})+\.([a-zA-Z]{2,3}))/;
function trimmer(tt){var st=new String(tt);var b;var tx="";var blankseq="Y";	for(c=0;c<st.length;c++){b=st.substr(c,1); if(!(b==" ")) blankseq="N"; if(blankseq=="N") tx=tx+b;}tt=tx;tx="";var st=new String(tt);var blankseq="Y";for(c=st.length-1;c>=0;c--){b=st.substr(c,1); if(!(b==" ")) blankseq="N";	if(blankseq=="N") tx=b+tx;}return tx;}
/*....vars......*/var processfile=function(pfile,param){if(typeof param==='undefined') param="";if(param!="") paramset="?"+param; else	paramset=""; if(typeof pfile==='undefined') return ""; else return siteroot+"model/process/"+pfile+".php"+paramset;};
function hitFile(filename,param){if(typeof param==='undefined') param="";document.location=processfile(filename,param);}
function ajaxprocessing(ProcessFile,SendMethod,Parameters,MsgContainer){var xmlhttp;if(window.XMLHttpRequest) xmlhttp=new XMLHttpRequest();	else xmlhttp=new ActiveXObject("Mircrosoft.XMLHTTP"); xmlhttp.onreadystatechange=function(){document.getElementById(MsgContainer).innerHTML=document.getElementById(MsgContainer).innerHTML+"<i class='fa fa-spinner'></i>"; if(xmlhttp.readyState==4 && xmlhttp.status==200) document.getElementById(MsgContainer).innerHTML=xmlhttp.responseText;}; if(SendMethod=="GET"){xmlhttp.open("GET",siteroot+"model/process/"+ProcessFile+".php?"+Parameters,true);xmlhttp.send();} if(SendMethod=="POST"){xmlhttp.open("POST",siteroot+"model/process/"+ProcessFile+".php",true);xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded"); xmlhttp.send(Parameters);}}
///........function to display user messages in specified element block.....
function alertmsg(ElementID,Message){var strlen=(new String(Message)).length;$("#"+ElementID).css({"display":"block"});$("#"+ElementID).addClass("alert alert-warning alert-dismissable");$("#"+ElementID).html('<button type="button" class="close" data-dismiss="alert" aria-hidden="true"><i class="fa fa-close"></i></button><i class="fa fa-info-circle"></i> '+Message);$("#"+ElementID).focus(); var msgtimeout=setTimeout(function(){$("#"+ElementID).fadeOut(800);},strlen*120);}
function CheckboxValues(chkbox){var chk=document.getElementsByName(chkbox); var  values=new Array();ind=0;for(i=0; i<chk.length; i++){if(chk[i].checked){ values[ind]=chk[i].value; ind++;}} return values;}
var submitForm=function(formID,ActionFile){document.getElementById(formID).action=processfile(ActionFile);document.getElementById(formID).submit();}
function load_content_onscroll(footerHeight,dContainer,prFile,callBack){
    if(typeof callBack==='undefined'){
        callBack="";
    }
    /*if($(window).width()>640)
        var extraheight=footerHeightDesktop;
    else
        var extraheight=footerHeightMobile;*/
    var extraheight=footerHeight+350;
    if($(window).scrollTop() > ($(document).height() - extraheight) - $(window).height())
    {
        
        $('div#loadmoreajaxloader').show();
        $.ajax({
        url: processfile(prFile),
        success: function(html)
        {
            if(html)
            {
                    $("#"+dContainer).append(html);
                    $('div#loadmoreajaxloader').hide();
            }else
            {
                    $('div#loadmoreajaxloader').html('');
            }
            if(callBack!=""){
                callBack();
            }
        }
        });
    }
}

$.each($(".datepicker"),function(key, obj){
    var dt=$("#"+obj.id);
    var objval=dt.val();
    dt.datepicker({dateFormat:'dd-mm-yy'});
    dt.datepicker("setDate",objval);
    if(dt.hasClass("dob")){
        with(dt){
            datepicker("option", "changeYear", true);
            datepicker("option", "minDate", '-100Y');
            datepicker("option", "maxDate", '0');
            datepicker("option", "yearRange", '1900:c');
        }
    }else{
        dt.datepicker("option", "minDate", '0'); 
    }
    //$("#"+obj.id).keypress(function(e) {return false;});
});

$("#frmsubsnl").submit(function(e) {
	var txt=document.getElementById("txtnlemail");
	var email=txt.value;
	var msg="subsnlmsg";
	
	if(trimmer(email)==""){
		alertmsg(msg,"Please specify e-mail ID.!");
		return false;
	}
	if(emailpattern.test(email)==false){
		alertmsg(msg,"Please enter valid e-mail ID..!");
		return false;
	}
	
	var param="email="+email;
	$(this).get(0).reset();
	$("#"+msg).text("Submitting Query...");$("#"+msg).css({"display":"block"});
	ajaxprocessing("postnl","POST",param,msg);
	return false;
});
///contact form
$("#frmcontact").submit(function(e) {
	var name=$("#txtcname").val();
	var email=$("#txtcemail").val();
	var phone=$("#txtcphone").val();
	var message=$("#txtcmessage").val();
	var emsg="message-contact";
	if(trimmer(name)==""){
		alertmsg(emsg,"Please specify your name.!");
		return false;
	}
	if(trimmer(email)==""){
		alertmsg(emsg,"Please specify e-mail ID.!");
		return false;
	}
	if(emailpattern.test(email)==false){
		alertmsg(emsg,"Please enter valid e-mail ID..");
		return false;
	}
	if(trimmer(phone)==""){
		alertmsg(emsg,"Please specify phone..!");
		return false;
	}
	if(trimmer(message)==""){
		alertmsg(emsg,"Please enter message..!");
		return false;
	}
	
	var param="txtname="+name+"&txtemail="+email+"&txtphone="+phone+"&txtmessage="+message;
	$(this).get(0).reset();
	$("#"+emsg).text("Submitting Query...");$("#"+emsg).css({"display":"block"});
	ajaxprocessing("postcontact","POST",param,emsg);
	return false;
});

///inquiry form
$("#frminquiry").submit(function(e) {
	var name=$("#txtinqname").val();
        var companyname=$("#txtinqcompanyname").val();
	var email=$("#txtinqemail").val();
	var phone=$("#txtinqphone").val();
        var landline=$("#txtinqlandline").val();
        var address=$("#txtinqaddress").val();
        var country=$("#txtinqcountry").val();
	var message=$("#txtinqmessage").val();
	var emsg="message-inquiry";
	if(trimmer(name)==""){
		alertmsg(emsg,"Please specify your name.!");
		return false;
	}
	if(trimmer(email)==""){
		alertmsg(emsg,"Please specify e-mail ID.!");
		return false;
	}
	if(emailpattern.test(email)==false){
		alertmsg(emsg,"Please enter valid e-mail ID..");
		return false;
	}
	if(trimmer(phone)==""){
		alertmsg(emsg,"Please specify phone..!");
		return false;
	}
        if(trimmer(country)==""){
		alertmsg(emsg,"Please specify country name..!");
		return false;
	}
	if(trimmer(message)==""){
		alertmsg(emsg,"Please enter message..!");
		return false;
	}
	
	var param=$(this).serialize();
	$(this).get(0).reset();
	$("#"+emsg).text("Submitting Query...");$("#"+emsg).css({"display":"block"});
	ajaxprocessing("sendinquiry","POST",param,emsg);
	return false;
});

///feedback form
$("#frmfeedback").submit(function(e) {
	var name=$("#txtfbname").val();
	var email=$("#txtfbemail").val();
	var phone=$("#txtfbphone").val();
	var emsg="message-feedback";
	if(trimmer(name)==""){
		alertmsg(emsg,"Please specify your name.!");
		return false;
	}
	if(trimmer(email)==""){
		alertmsg(emsg,"Please specify e-mail ID.!");
		return false;
	}
	if(emailpattern.test(email)==false){
		alertmsg(emsg,"Please enter valid e-mail ID..");
		return false;
	}
	if(trimmer(phone)==""){
		alertmsg(emsg,"Please specify phone..!");
		return false;
	}
    

	$("#"+emsg).text("Submitting Query...");$("#"+emsg).css({"display":"block"});
	$.ajax({
		type:'POST',
		data:$(this).serialize(),
		url: processfile("sendfeedback"),
		success: function(result){
			alertmsg(emsg,result);
			$("#frmfeedback").get(0).reset();
		}
	});
	return false;
});


///Home collection form
$("#frmcollection").submit(function(e) {
	var name=$("#txthmcname").val();
	var email=$("#txthmcemail").val();
	var phone=$("#txthmcphone").val();
        var address=$("#txthmcaddress").val();
	var dated=$("#txthmcdate").val();
	var timed=$("#txthmctime").val();
	var age=$("#txthmcage").val();
	var emsg="message-collection";
	if(trimmer(name)==""){
		alertmsg(emsg,"Please specify your name.!");
		return false;
	}
	if(trimmer(email)==""){
		alertmsg(emsg,"Please specify e-mail ID.!");
		return false;
	}
	if(emailpattern.test(email)==false){
		alertmsg(emsg,"Please enter valid e-mail ID..");
		return false;
	}
	if(trimmer(phone)==""){
		alertmsg(emsg,"Please specify phone..!");
		return false;
	}
        if(trimmer(address)==""){
		alertmsg(emsg,"Please specify address..!");
		return false;
	}
	if(trimmer(dated)==""){
		alertmsg(emsg,"Please enter collection date..!");
		return false;
	}
	if(trimmer(timed)==""){
		alertmsg(emsg,"Please enter collection time..!");
		return false;
	}
	if(trimmer(age)==""){
		alertmsg(emsg,"Please enter age..!");
		return false;
	}
        if(PinNotFound==true){
                alertmsg(emsg,"Specified PIN is not available for collecting sample.!");
                return false;
        }
	
	$("#"+emsg).text("Submitting Query...");$("#"+emsg).css({"display":"block"});
	$.ajax({
		type:'POST',
		data:$(this).serialize(),
		url: processfile("sendhomecollection"),
		success: function(result){
			alertmsg(emsg,result);
			$("#frmcollection").get(0).reset();
		}
	});
	return false;
});


$("#txtregemail, #txtregphone").blur(function(e) {
    checkregistration();
});
function checkregistration(){
    var email=$("#txtregemail").val();
    var phone=$("#txtregphone").val();
    var param="email="+email+"&phone="+phone;
    $.ajax({
        type:'POST',
        url: processfile("chkregister"),
        data:param,
        success: function(result){
            if(result!="Success"){
                $("#message-email").text(result).fadeIn(1000).fadeOut(8000);
                $("#txtproceed").val("1");
            }else{
                $("#message-email").text("");
                $("#txtproceed").val("0");
            }
        }
    });
}
$("#frmregister").submit(function(e) {
        var fname=$("#txtregfname").val();
        var lname=$("#txtreglname").val();
	var email=$("#txtregemail").val();
        var phone=$("#txtregphone").val();
	var pwd=$("#txtregpwd").val();
	var cpwd=$("#txtregconfpwd").val();
	
	var emsg="message-register";
        
	if(trimmer(email)==""){
		alertmsg(emsg,"Please specify email ID.!");
		return false;
	}
	if(emailpattern.test(email)==false){
		alertmsg(emsg,"Please enter valid e-mail ID..");
		return false;
	}
        if(trimmer(phone)==""){
		alertmsg(emsg,"Please specify phone number.!");
		return false;
	}
        if(trimmer(fname)==""){
		alertmsg(emsg,"Please specify first name.!");
		return false;
	}
	if(trimmer(pwd)==""){
		alertmsg(emsg,"Please specify password.!");
		return false;
	}
	if(pwd!=cpwd){
            alertmsg(emsg,"Specified and confirmed passwords are not same.!");
            return false;
	}
        if($("#txtproceed").val()=="1"){
            alertmsg(emsg,$("#message-email").text());
            return false;
        }
        if($('#chkterms').prop("checked")==false){
                alertmsg(emsg,"Please check if agree with terms and conditions.!");
		return false;
        }
        submitForm("frmregister","webregistration");
        return false;
});

$("#frmcheckout").submit(function(e) {
        var pname=$("#txtpatientname").val();
        var pgender=$("#selgender").val();
	var page=$("#txtpatientage").val();
        var hmcpin=$("#txthmcpin").val();
	var hmcaddress=$("#txthmcaddress").val();
	var hmcdate=$("#txthmcdate").val();
        var hmctime=$("#txthmctime").val();
        var sdpdate=$("#txtsdpdate").val();
        var sdptime=$("#txtsdptime").val();
        var sdpname=$("#txtsdpdepositor").val();
        var name=$("#txtname").val();
        var phone=$("#txtphone").val();
        var address=$("#txtaddress").val();
        var city=$("#txtcity").val();
        var statename=$("#txtstatename").val();
        var pin=$("#txtpin").val();
	
	var emsg="message-checkout";
        
	if(trimmer(pname)==""){
		alertmsg(emsg,"Please specify patient name.!");
		return false;
	}
        if(trimmer(page)==""){
		alertmsg(emsg,"Please specify age of patient.!");
		return false;
	}
        
        if($("#chkhomecolprice").prop("checked")==true){
            if(trimmer(hmcdate)==""){
                    alertmsg(emsg,"Please specify date of collecting sample.!");
                    return false;
            }
            if(trimmer(hmctime)==""){
                    alertmsg(emsg,"Please specify time of collecting sample.!");
                    return false;
            }
            if(trimmer(hmcpin)==""){
                    alertmsg(emsg,"Please specify pincode of area for collecting sample.!");
                    return false;
            }
            if(trimmer(hmcaddress)==""){
                    alertmsg(emsg,"Please specify address for collecting sample.!");
                    return false;
            }
            if(PinNotFound==true){
                    alertmsg(emsg,"Specified PIN is not available for collecting sample.!");
                    return false;
            }
        }else{
            if(trimmer(sdpdate)==""){
                    alertmsg(emsg,"Please specify date of depositing the sample at lab.!");
                    return false;
            }
            if(trimmer(sdptime)==""){
                    alertmsg(emsg,"Please specify time of depositing the sample at lab.!");
                    return false;
            }
            if(trimmer(sdpname)==""){
                    alertmsg(emsg,"Please specify name of the sample depositor.!");
                    return false;
            }
        }
        if(trimmer(name)==""){
		alertmsg(emsg,"Please specify name.!");
		return false;
	}
        if(trimmer(phone)==""){
		alertmsg(emsg,"Please specify phone number.!");
		return false;
	}
        if(trimmer(address)==""){
		alertmsg(emsg,"Please specify address.!");
		return false;
	}
        if(trimmer(city)==""){
		alertmsg(emsg,"Please specify city.!");
		return false;
	}
        if(trimmer(statename)==""){
		alertmsg(emsg,"Please specify state name.!");
		return false;
	}
        if(trimmer(pin)==""){
		alertmsg(emsg,"Please specify pincode.!");
		return false;
	}
        if($('#chkterms').prop("checked")==false){
                alertmsg(emsg,"Please check if agree with terms and conditions.!");
		return false;
        }
});

$("#frmonlinepmt").submit(function(e) {
        var pname=$("#txtpatientname").val();
        var pgender=$("#selgender").val();
	var page=$("#txtpatientage").val();
        var pref=$("#txtpatientref").val();
        var name=$("#txtname").val();
        var email=$("#txtemail").val();
        var phone=$("#txtphone").val();
        var address=$("#txtaddress").val();
        var city=$("#txtcity").val();
        var statename=$("#txtstatename").val();
        var pin=$("#txtpin").val();
        var amount=$("#txtamount").val();
        var description=$("#txtdescription").val();
	var emsg="message-onlinepmt";
        
	if(trimmer(pname)==""){
		alertmsg(emsg,"Please specify patient name.!");
		return false;
	}
        if(trimmer(page)==""){
		alertmsg(emsg,"Please specify age of patient.!");
		return false;
	}
        if(trimmer(pref)==""){
		alertmsg(emsg,"Please specify age of patient reference.!");
		return false;
	}
        
        
        if(trimmer(name)==""){
		alertmsg(emsg,"Please specify name.!");
		return false;
	}
        if(trimmer(email)==""){
		alertmsg(emsg,"Please specify email ID.!");
		return false;
	}
	if(emailpattern.test(email)==false){
		alertmsg(emsg,"Please enter valid e-mail ID..");
		return false;
	}
        if(trimmer(phone)==""){
		alertmsg(emsg,"Please specify phone number.!");
		return false;
	}
        if(trimmer(address)==""){
		alertmsg(emsg,"Please specify address.!");
		return false;
	}
        if(trimmer(city)==""){
		alertmsg(emsg,"Please specify city.!");
		return false;
	}
        if(trimmer(statename)==""){
		alertmsg(emsg,"Please specify state name.!");
		return false;
	}
        if(trimmer(pin)==""){
		alertmsg(emsg,"Please specify pincode.!");
		return false;
	}
        if(trimmer(amount)==""){
		alertmsg(emsg,"Please specify amount to be paid.!");
		return false;
	}
        if(trimmer(description)==""){
		alertmsg(emsg,"Please specify description for the payment to be done.!");
		return false;
	}
        if($('#chkterms').prop("checked")==false){
                alertmsg(emsg,"Please check if agree with terms and conditions.!");
		return false;
        }
});

$("#frmpaynow").submit(function(e) {
    var emsg="message-paynow";
    if($('#rdpayoptioncash').prop("checked")==true && $('#chkackcash').prop("checked")==false){
        alertmsg(emsg,"Please mark check on acknowledgement for pay CASH.!");
        return false;
    }
});
$("#btnVerifyCode").click(function(e) {
    var email=$("#txtveriemail").val();
    var vericode=$("#txtvericode").val();   
    var emsg="reg-verify-msg";
    var param="emailid="+email+"&vericode="+vericode;
    $.ajax({
        type:'POST',
        url: processfile("vericode-ok"),
        data:param,
        success: function(result){
            if(result.indexOf("does not match")>-1){
                alertmsg(emsg,result);
            }
            else{
                document.getElementById("reg-verify").innerHTML=result;
            }
        }
    });
    return false;
});

$("#frmlogin").submit(function(){
    var email=$("#txtuseremail").val();
    var pwd=$("#txtuserpwd").val();
    var emsg="message-login";
    if(trimmer(email)==""){
        alertmsg(emsg,"Please specify email ID.!");
        return false;
    }
    if(emailpattern.test(email)==false){
        alertmsg(emsg,"Please enter valid e-mail ID..");
        return false;
    }
    if(trimmer(pwd)==""){
        alertmsg(emsg,"Please specify password.!");
        return false;
    }
    var param="email="+email+"&pwd="+pwd;
    $.ajax({
        type:'POST',
        url: processfile("chkuserlogin"),
        data:param,
        success: function(result){
            if(result!="Success"){
                alertmsg(emsg,result);
            }
            else
                hitFile("reflocation");
        }
    });
    return false;
});
function weblogout(){hitFile("logout");}
$("#frmforgot").submit(function(e) {
	var email=$("#txtfgtemail").val();
	var emsg="message-forgot";

	if(trimmer(email)==""){
		alertmsg(emsg,"Please specify email ID.!");
		return false;
	}
	if(emailpattern.test(email)==false){
		alertmsg(emsg,"Please enter valid e-mail ID..");
		return false;
	}
	
	var param="email="+email;
	$("#"+emsg).text("Please wait...");$("#"+emsg).css({"display":"block","text-align":"center"});
        $.ajax({
            type:'POST',
            url: processfile("retrievepwd"),
            data:param,
            success: function(result){
                alertmsg(emsg,result);
                if(result.indexOf("check inbox")!=-1)
                $("#frmforgot").get(0).reset();   
            }
        });
	return false;
});


$("#frmchangepassword").submit(function(e){
    var emsg="message-password";
    var param=$(this).serialize();
    $.ajax({
        type:'POST',
        url: processfile("chpwd"),
        data:param,
        success: function(result){
            alertmsg(emsg,result);
            if(result.indexOf("successfully")!=-1)
            $("#frmchangepassword").get(0).reset();   
        }
    });
    return false;
});

$("#frmprofile").submit(function(e) {
    var fname=$("#txtfirstname").val();
    var emsg="message-profile";

    if(trimmer(fname)==""){
            alertmsg(emsg,"Please specify first name.!");
            return false;
    }

    submitForm("frmprofile","update-profile");
    return false;
});

$("#txtpatientname").keyup(function(e){
    if($("#txtsdpdepositor")){
        $("#txtsdpdepositor").val($(this).val());
    }
});

$("[name='rdsamplecollect']").click(function(){
   if($(this).val()=="yes"){
       $("#sample-collect-info").slideDown();
       $("#sample-deposit-info").slideUp();
   }else{
       $("#sample-deposit-info").slideDown();
       $("#sample-collect-info").slideUp();
       $("#txthmcpin").val("");
       $("#txthmcolcharges").val(0);
       $("#colcharges-search").text("");
       $("#hmcolcharges").text("0");
   }
});
var PinNotFound=true;
$("#txthmcpin").keyup(function(){
    findColCharges();
});
function findColCharges(){
    if($("#txthmcpin").val().length>6){
        $("#colcharges-search").text("Searching for Collection Charges..");
        param="pin="+$("#txthmcpin").val();
        $.ajax({
            type:'POST',
            url: processfile("showcolcharges"),
            data:param,
            success: function(result){
                if(result!="not found"){
                    $("#hmcolcharges").text(result);
                    $("#txthmcolcharges").val(result);
                    PinNotFound=false;
                    checkoutcalc();
                    alertmsg("colcharges-search","Sample collection charges has been added to your order total.");
                }else{
                    $("#hmcolcharges").text(0);
                    $("#txthmcolcharges").val(0); 
                    PinNotFound=true;
                    alertmsg("colcharges-search","This location could not be found.");
                }
            }
        });
    }
}
$("[name='rdpayoption']").click(function(){
    $(".pay-note").hide();
    if($(this).val()=="Cash"){
        $("#pay-cash-note").fadeIn("slow");
    }else{
        $("#pay-online-note").fadeIn("slow");
    }
});
$(".pay-option").click(function(){
    $("#frmpaynow").attr("action",$(this).attr("data-url"));
});

function checkoutcalc() {
    var grandtotal = Number($("#txtcartsubtotal").val())+Number($("#txthmcolcharges").val());
    $("#carttotal").text(grandtotal);
    $("#txtcarttotal").val(grandtotal);
}

function checkcolavail(){
    if(typeof $("#txthmcdate").val()!=="undefined"){
        param="collectdate="+$("#txthmcdate").val();
        $.ajax({
            type:'POST',
            url: processfile("checkavailability"),
            data:param,
            success: function(result){
                $("#txthmctime").html(result);
                $("#txthmctime").niceSelect('update');
            }
        });
    }
}
$("#txthmcdate").on("change",function(){
    checkcolavail();
});

function checkagentavail(){
    if(typeof $("#txthmcdate").val()!=="undefined" && typeof $("#txthmctime").val()!=="undefined"){
        param="collectdate="+$("#txthmcdate").val()+"&collecttime="+$("#txthmctime").val();
        $.ajax({
            type:'POST',
            url: processfile("checkagentavail"),
            data:param,
            success: function(result){
                $("#txthmcagent").html(result);
                $("#txthmcagent").niceSelect('update');
            }
        });
    }
}
$("#txthmctime").on("change",function(){
    checkagentavail();
});

$("#seltestsort").on("change",function(){
    var frm=$("#frmsort").get(0);
    frm.action=processfile("sort-tests");
    frm.submit();
});


$("#btnclearfilter").click(function(){
    $("#txtalpha").val("");
    $("[type='checkbox']").prop("checked",false);
    $("#chktest").prop("checked",true);
    $("#txtsearchtext").val("");
    frmfiltersubmit();
});
$(".anc-alpha").click(function(){
    var txt=$(this).text();
    $("#txtalpha").val(txt);
    frmfiltersubmit();
});
$("#frmfilter [type='checkbox']").click(function(){
    frmfiltersubmit();
});
function frmfiltersubmit(){
    var frm=$("#frmfilter").get(0);
    frm.action=processfile("filter-tests");
    frm.submit();
}

$("#frmsearch").submit(function(){
    if($("#txtsearch").val().length==0){
        return false;
    }
    $(this).get(0).action=processfile("search-tests");
});
$("#txtsearch").keyup(function(e){
    if($(this).val().length>0){
        searchvalue=$(this).val();
        $(this).parents(".search").find(".clear-search").show();
    }
    if(e.keyCode==13){
        $("#frmsearch").submit();
    }
});
$(".clear-search").click(function(){
    $("#txtsearch").val("").focus();
    $(this).hide();
});

function view_all_tests(obj){
    var pkgid=obj.attr("test-data");
    var pkgname=obj.attr("pkg-name");
    param="pkgid="+pkgid;
    $.ajax({
        type:'POST',
        url: processfile("loadpkgtests"),
        data:param,
        success: function(result){
            if(result!=""){
                $('#tests-included .modal-title').html(pkgname);
                $('#tests-included .test-included-ele').html(result);
                $('#tests-included').modal('show');
            }
        }
    });
}
$(".btn-view-tests").click(function(){
    view_all_tests($(this));
});
$(document).click(function () {
    checkoutcalc();
});

function InputIncDecBtn() {
    /*input incrementer==============================*/
    $(".numbers-row").append('<div class="inc button_inc">+</div><div class="dec button_inc">-</div>');
    $(".button_inc").on("click", function () {
        var $button = $(this);
        var oldValue = $button.parent().find("input").val();

        if ($button.text() == "+") {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don't allow decrementing below zero
            if (oldValue > 1) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                if ($(this).parent(".numbers-row").hasClass("zero-value"))
                    newVal = 0;
                else
                    newVal = 1;
            }
        }
        $button.parent().find("input").val(newVal);
    });
}
InputIncDecBtn();

var searchvalue='';
$('#txtsearch').autocomplete({
    //valueKey:'value',
    titleKey:'title',
    closeOnBlur:false,
    source:[{
        url:processfile("searchlist","query=%QUERY%"),
        type:'remote',
        getValue:function(item){
            return item.title;
        },
        getTitle:function(item){
            return item.title;
        },
        ajax:{
            dataType : 'json'
        }
    }],
    render:function(item,source,pid,query ){
        var value = item[this.valueKey],
            data=item.data;
            carturl=item.carturl;
        return '<div '+(value==query?'class="test-search-item active"':'class="test-search-item"')+
         ' data-value="'+
         encodeURIComponent(value)+'" onmousedown="searchvalue=\''+value+'\'" ontouchstart="searchvalue=\''+value+'\'"><span class="col-xs-10 test-title">'+
         value+'</span><a href="javascript:void(0)" class="col-xs-2 cart-btn" cart-data="'+
        data+'" onmousedown="'+(carturl==''?'add_to_cart($(this).attr(\'cart-data\'))':'document.location=\''+carturl+'\'')+'" ontouchstart="'+(carturl==''?'add_to_cart($(this).attr(\'cart-data\'))':'document.location=\''+carturl+'\'')+'">'+(carturl==''?'Add':'View')+' </a></div>';
       }
}).on("pick.xdsoft",function(){
    if(sp=searchvalue.split("<br>")){
        searchvalue=sp[0];
    }
    $(this).val(searchvalue);
});

var hmcityid;
function pinareas(){
    $('#txthmcpin').autocomplete('destroy');
    $('#txthmcpin').removeClass('xdsoft_input');
    $('#txthmcpin').removeAttr("autocomplete");
    $('#txthmcpin').removeAttr("style");
    $('#txthmcpin').val('');
    var hmcityid=(($("#txthmccity").val()).split(":"))[0];
    $('#txthmcpin').autocomplete({
        valueKey:'title',
        source:[{
            url:processfile("pinarealist","cityid="+hmcityid+"&query=%QUERY%"),
            type:'remote',
            getValueFromItem:function(item){
                return item.title
            },
            ajax:{
                dataType : 'json'
            }
        }]
    }).on('selected.xdsoft',function(e,datum){
        findColCharges();
    });
}
$("#txthmccity").change(function(){
    pinareas();
});