$(document).ready(function()
{
  $('#p_cat_upd_btn').hide()

   $('#p_cat_add_btn').on('click', function()
   {
      var Add_Data=new FormData(this.form)
      $.ajax({
        url:'/insert',
        type:'POST',
        contentType: false,
        processData: false,
        data: Add_Data,
        success: function(res){
          if(res== 1)
          {
            alert('inserted')
          }
          else
          {
            alert('error')
          }
          $('#Cat-Modal').modal('hide')
          disp_cat();
        }
      })
   })

// displaying product category data in the product category table
   
  function disp_cat()
   {
    $.ajax({
      url:'/display_category',
      type:'POST',
      success: function(data)
      {
    
        if(data.length<=0 || data=='Error')
        {
          
          disp =`<h1 class='text-center bg-dark text-white'>DATA IS NOT FOUND IN THE PRODUCT CATEGORY TABLE</h1>`;
        }
        else
        {
          var disp=`
          <tr>
            <th>Product Category ID</th>
            <th>Product Category Name</th>
            <th>Product Category description</th>
            <th>Product Category Entry Date</th>
            <th>Product Category Image</th>
          </tr>`;
          for(let i of data)
          {
            disp +=`
            <tr>
              <th>${i[0]}</th>
              <th>${i[1]}</th>
              <th>${i[2]}</th>
              <th>${i[3]}</th>
              <th><img src="./static/Images/${i[4]}" alt="${i[4]}" height="100px" width="100px" style="border-radius: 5px;"></th>
              <th><button type="button" class="btn btn-info p-cat-upd text-dark" data-id="${i[0]}">Update</button></th>
              <th><button type="button" class="btn btn-info p-cat-del text-dark" data-id="${i[0]}">Delete</button></th>
            </tr>
            `;
          }
         }
        $('#p_cat_disp_data').html(disp)
      }
    })
  }

// adding updated data in the product category table

  $('#p_cat_upd_btn').on('click', function(){
    let p_cat_ids=$(this).data('id')

    var updated_data=new FormData(this.form)
    updated_data.append('cat_id',p_cat_ids)
    for(let i of updated_data)
    {

        console.log(i)
    }
    $.ajax({
        url:'/update_category',
        type:'PUT',
        contentType: false,
        processData: false,
        data: updated_data,
        success:function(res)
        {
          if(res =='inserted')
          {
            alert('updated')
          }
          else
          {
            alert('Error')
          }
          $('#Cat-Modal').modal('hide')
          disp_cat();
        }
      })
  })

// deleting data from the product_category_table

  $(document).on('click','.p-cat-del', function(){
    var p_cat_ids=$(this).data('id')
    console.log(p_cat_ids)
    $.ajax({
        url:'/delete_category',
        type:'DELETE',
        data:{'cat-id':p_cat_ids},
        success:function(res)
        {
          if(res =='Deleted')
          {
            alert('deleted')
          }
          else
          {
            alert('Error')
          }
          disp_cat()
        }
      })
  })
  //displaying data to be updated in product management form

  $(document).on('click','.p-cat-upd', function(){
    var p_cat_ids=$(this).data('id')
    console.log(p_cat_ids)
    $.ajax({
          url:'/update1_category',
          type:'POST',
          data:{'cat-id':p_cat_ids},
          success:function(res)
          {
            data=res
            $('#p_cat_name').val(data[1])
            $('#p_cat_desp').val(data[2])
            $('#p_cat_date').val(data[3])
            $('#filename').val(data[4])
            $('#p_cat_upd_btn').attr('data-id', data[0])
            $('#p_cat_upd_btn').show()
            $('#p_cat_add_btn').hide()

          }
      })
      $('#Cat-Modal').modal('show')
  })
  disp_cat()
})