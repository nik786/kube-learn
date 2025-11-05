// JavaScript Document
var cartprocessfolder = "cart/";
function cart_binding(){
    $(".cart-btn").on("click", function (e) {
        add_to_cart($(this).attr("data-item"));
    });

    $("#btn-cancelupdate").click(function () {
        cart_redirect_url("cancel-update");
    });
    $("#btn-additems").click(function () {
        cart_redirect_url("shop-more");
    });

    $("#btn-checkout").click(function () {
        $("#frmcart").get(0).action = processfile(cartprocessfolder + 'checkout');
        $("#frmcart").get(0).submit();
    });

    $("#btn-updatecart").click(function () {
        $("#frmcart").get(0).action = processfile(cartprocessfolder + 'updatecart');
        $("#frmcart").get(0).submit();
    });

    $("#btn-editcartqty").click(function () {
        $("#btn-updatecart").show();
        $(".numbers-row").show();
        $("#btn-cancelupdate").show();
        $("#btn-checkout, #btn-additems, .qty-in-cart").hide();
        $(this).hide();
    });

    $(".remove-cart-item").click(function () {
        jQuery('#' + $(this).parents("tr").attr("id")).remove();
        $("#btn-updatecart, #btn-cancelupdate").show();
        $("#btn-checkout, #btn-additems, #btn-editcartqty").hide();
    });

    $(document).click(function () {
        cartcalc();
    });
}cart_binding();

function add_to_cart(data){
    var citemval = data;
    var cartobj=$('[data-item="'+data +'"]');
    var param = "";
    var citem = citemval.split("~~");
    if(citem instanceof Array){
        param += "itemid=" + citem[0];
        param += "&itemcode=" + citem[1];
        param += "&itemname=" + citem[2];
        param += "&itemprice=" + citem[3];
        param += "&itemqty=1";
        cartobj.find("i").attr("class", "fa fa-cog fa-spin");
        cartobj.addClass("cart-processing");
        $.ajax({
            type: 'POST',
            data: param,
            url: processfile(cartprocessfolder + "addcart"),
            success: function (result) {
                $(".cart-processing").html('View Cart <i class="fa fa-check"></i>');
                $(".cart-processing").attr("href",$(".cart-dropdown ul.dropdown-menu li:last-child a").attr("href"));
                $(".cart-processing").removeClass("cart-processing");
                var cartlastchild = $(".cart-dropdown ul.dropdown-menu li:last-child").html();
                if (result != 'NULL') {
                    var obj = JSON.parse(result);
                    var htmlele = '';
                    for (i = 0; i < obj.data.length; i++) {
                        if (i > 3)
                            break;
                        htmlele += '<li><a href="javascript:void(0)">' + obj.data[i].itemname + '<div class="price"><i class="fa fa-inr"></i> ' + obj.data[i].itemprice + ' x ' + obj.data[i].itemqty + '</div></a><a href="javascript:void(0)" class="fa fa-close" style="display:none"></a></li>';
                    }
                    if(obj.data.length==0){
                        htmlele="<li><a>Cart is Empty!</a></li>";
                    }else{
                        htmlele += "<li>" + cartlastchild + "</li>";
                    }
                    $(".cart-dropdown ul.dropdown-menu").html(htmlele);
                    $(".cart-dropdown i.count").text(obj.data.length);
                    alertmsg("message-cart",citem[2]+" has been added to cart..!");
                }
            }
        });
    }
}

function cart_redirect_url(redirect_type) {
    if (typeof redirect_type === 'undefined')
        redirect_type = "default";
    param = "type=" + redirect_type;
    hitFile(cartprocessfolder + "redirecturl", param);
}

function cartcalc() {
    var grandtotal = 0;
    if($("div").hasClass("cart-list")){
        $(".cart-list table tr").each(function () {
            var cartprice = $(this).find("input[name='txtitemprice[]']").val();
            var cartnos = $(this).find("input[name='txtitemqty[]']").val();
            if (isNaN(cartprice) == false || isNaN(cartnos) == false) {
                var total = cartprice * cartnos;
                grandtotal = grandtotal + total;
                $(this).find("span.item-amount").text(total);
            }
        });
        $("#cartsubtotal").text(grandtotal);
        $("#txtcartsubtotal").val(grandtotal);
        $("#carttotal").text(grandtotal);
        $("#txtcarttotal").val(grandtotal);
    }
}

