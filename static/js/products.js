$(document).ready(function()
{
    $('#p_upd_btn').hide()

// displaying data on product_table
  
function display_prod(){
    $.ajax({
      url:'/display_product',
     type:'POST',
     success: function(data1)
     {
       if(data1.length <=0 || data1==0)
        {
            console.log(data1)
          disp1=`<h1 class='text-center bg-dark text-white'>DATA IS NOT FOUND IN THE PRODUCT TABLE</h1>`
        }
        else
        {
          var disp1=`
          <tr>
            <th>Product ID</th>
            <th>Product Name</th>
            <th>Product Price</th>
            <th>Product Category ID</th>
            <th>Product Short Description</th>
            <th>Product Long Description</th>
            <th>Product Insert Date</th>
            <th>Product Images</th>
          </tr>`;
          for(let row1 of data1)
          {
            disp1+=`
            <tr>
              <th>${row1[0]}</th>
              <th>${row1[1]}</th>
              <th>${row1[2]}</th>
              <th>${row1[3]}</th>
              <th>${row1[4].slice(0,20)}...</th>
              <th>${row1[5].slice(0,20)}...</th>
              <th>${row1[6]}</th>
              <th><img src="./static/Images/${row1[7]}" alt="${row1[7]}" height="100px" width="100px" style="border-radius: 5px;"></th>
              <th><button type="button" class="btn btn-info text-dark p-upd" data-id="${row1[0]}">Update</button></th>
              <th><button type="button" class="btn btn-info text-dark p-del" data-id="${row1[0]}">Delete</button></th>
            </tr>
            `;
          }
        }
        $('#p_disp_data').html(disp1)
      }
    })
    
  }
 

  // adding data in the product_table
 
  $('#p_add_btn').on('click', function(){
    var Add_data1= new FormData(this.form);

    for(let i of Add_data1)
    {
        console.log(i)
    }
    
   $.ajax({
      url:'/insert_product',
      type:'POST',
      contentType: false,
      processData: false,
      data: Add_data1,
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
        $('#prod_modal').modal('hide')
        display_prod();
      }
    })
  })

// adding updated data in the product_table
 
  $('#p_upd_btn').on('click', function(){
    var p_ids=$(this).data('id')
    console.log(p_ids)
    var updated_data1=new FormData(this.form)

    updated_data1.append('p-id',p_ids)
    for(let i of updated_data1)
    {
        console.log(i)
    }
    $.ajax({
        url:'/update_product',
        type:'PUT',
        contentType: false,
        processData: false,
        data: updated_data1,
        success: function(res)
        {
          if(res =='inserted')
          {
            alert('updated')
          }
          else
          {
            alert('Error')
          }
          $('#prod_modal').modal('hide')
          display_prod();
        }
      })
  })

// deleting data from the product_table

  $(document).on('click','.p-del', function(){
    var p_ids=$(this).data('id')
    console.log(p_ids)
    $.ajax({
        url:'/delete_product',
        type:'DELETE',
        data:{'p-id':p_ids},
        success: function(res)
        {
          if(res =='Deleted')
          {
            alert('deleted')
          }
          else
          {
            alert('Error')
          }
          display_prod()
        }
      })
  })

//displaying data to be updated in product management form

  $(document).on('click','.p-upd', function(){
    var p_ids=$(this).data('id')
    console.log(p_ids)
    $.ajax({
          url:'/update1_product',
          type:'POST',
          data:{'p-id':p_ids},
          success: function(res)
          {
            data=res
            console.log(res)
            $('#p_name').val(data[1])
            $('#p_price').val(data[2])
            $('#p_cat').val(data[3])
            $('#p_srt_desp').val(data[4])
            $('#p_lng_desp').val(data[5])
            $('#p_ins_date').val(data[6])
            // $('#p_img').val(data[7])
            $('#p_upd_btn').attr('data-id', data[0])
            $('#p_upd_btn').show()
            $('#p_add_btn').hide()
          }
      })
      $('#prod_modal').modal('show')
  })
  $("")
  display_prod()
})