$(document).ready(function(){


    function disp_flt() {
        $.ajax({
            url: '/Shopprod',
            type: 'GET',
            success: function (prod) {
                flt = "";
                if (prod.length <= 0 || prod == 0) {
                    var flt = `<h1 class="text-dark">Sorry! No product is available</h1>`
                }
                else {
                    for (let i of prod) {
                        flt += `
                    <div class="col pt-5">
                    <a href="/Shop/product_detail/${i[0]}" class="text-decoration-none text-dark">
                    <div class="card" style="width: 16rem;">
                        <img src="./static/Images/${i[7]}" class="card-img-top img-fluid" alt="${i[7]}" style="height: 200px;">
                        <div class="card-body">
                            <div class="row d-flex justify-content-evenly">
                                <div class="col">
                                    <h6 class="">${i[8]}</h6>
                                </div>
                                    <h4 class="card-text">${i[1]}</h4>
                                
                                <div class="col">
                                    <h5 class="text-warning text-end">₹${i[2]}</h5>
                                </div>
                            </div>
                        </a>
                            <div class="d-grid gap-2 mt-2">
                                <button data-id="${i[0]}" type="button" class="btn btn-warning add_cart">Add to Cart</button>
                              </div>
                        </div>
                    </div>
                </div>`

                    }

                }
                $("#disp_flt").html(flt)
            }
        })
    }

    disp_flt()



    $(document).on('click', '.add_cart', function () {
        var cart_data = $(this).data('id')
        console.log(cart_data)
        $.ajax({
            url: '/insert_cart',
            type: 'POST',
            data: { 'cart-id': cart_data },
            success: function (res) {
                if (res == 1) {
                    alert('inserted')
                }
                else if (res == -1) {
                    alert('Product Already Added')
                }
                else if (res == 2){
                    alert('log in')
                }
                else
                {
                    alert('error')
                }
            }
        })
    })
    $(document).on('click', '.cart-del', function () {
        var cart_del_data = $(this).data('id')
        console.log(cart_del_data)
        $.ajax({
            url: '/del_cart',
            type: 'DELETE',
            data: { 'cart-id': cart_del_data },
            success: function (res) {
                if (res == 1) {
                    alert('deleted')
                }
                else {
                    alert('error')
                }
        

            }
        })
    })
    $(document).on('change', '.prod_qty', function () {
        var p_ids = $(this).data('id')
        var qty = $(this).val()
        console.log(p_ids)
        console.log(qty)
        $.ajax({
            url: '/upd_cart',
            type: 'POST',     
            data: {"id":p_ids,"q":qty},
            success: function (res) {
                console.log(res)
                if(res == 0) {
                    {
                        alert('error')
                    }
                }
                else{
                alert('Updated')
                console.log(res)
                $('.t-price').text("₹"+res)
            }
        }
        })
    })

    $(document).on('click', '#prod-flt', function () {
        prodFrom = new FormData(this.form)
        if (prodFrom.getAll('pcat').length == 0) {
            disp_flt()

        }
        else {
            $.ajax({
                url: '/Shopprod',
                type: 'POST',
                contentType: false,
                processData: false,
                data: prodFrom,
                success: function (prod) {
                    flt = "";
                    if (prod.length <= 0 || prod == 0) {
                        var flt = `<h1 class="text-dark">Sorry! No product is available</h1>`
                    }
                    else {
                        for (let i of prod) {
                            flt += `
                    <div class="col pt-5">
                    <a href="{{url_for('prod_detail',id=${i[0]})}}" class="text-decoration-none text-dark">
                    <div class="card" style="width: 16rem;">
                        <img src="./static/Images/${i[7]}" class="card-img-top img-fluid" alt="${i[7]}" style="height: 200px;">
                        <div class="card-body">
                            <div class="row d-flex justify-content-evenly">
                                <div class="col">
                                    <h6 class="">${i[8]}</h6>
                                </div>
                                    <h4 class="card-text">${i[1]}</h4>
                                
                                <div class="col">
                                    <h5 class="text-warning text-end">₹${i[2]}</h5>
                                </div>
                            </div>
                        </a>
                            <div class="d-grid gap-2 mt-2">
                                <button data-id="${i[0]}" type="button" class="btn btn-warning add_cart">Add to Cart</button>
                              </div>
                        </div>
                    </div>
                </div>`

                        }

                    }
                    $("#disp_flt").html(flt)
                }
            })
        }
    })
    $(document).on('click','.add-check',function(){
        check_id=$(this).data('id')
        console.log(check_id)
        $.ajax({
            url:'/insert_check',
            type: 'POST',
            data:{'check-id':check_id},
            success: function(res)
            {
                if(res==1)
                {
                    alert('Inserted')
                }
                else
                {
                    alert('Error')
                }
            }
        })
    })
})