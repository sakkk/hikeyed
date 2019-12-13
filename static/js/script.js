$(function(){

    // toggleメニュー
    $("#toggle").click(function(){
        $("ul").slideToggle(200);
    });

    // 売上番号、価格、小計を入力不可
    // $("#id_sales").prop("disabled", "true");
    // $("#id_price").prop("disabled", "true");
    // $("#id_sub_total").prop("disabled", "true");

    // 商品名が変更されたときの処理
    $("#id_product").change(function(){
        $("#id_price").val("8800");
        // 小計を更新
        var sub_total = $("#id_price").val() * $("#id_amount").val();
        $("#id_sub_total").val(sub_total);
    });

    // 数量が変更されたときの処理
    $("#id_amount").change(function(){
        var sub_total = $("#id_price").val() * $("#id_amount").val();
        $("#id_sub_total").val(sub_total);
    });
});