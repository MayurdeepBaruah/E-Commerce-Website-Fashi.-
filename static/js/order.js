$(document).ready(function()
{
    function display_product_order()
     {
       $.ajax({
         url:'/disp_ord_detail',
         type:'POST',
         success: function(ord)
         {
           if(ord.length <=0)
           {
             disp3=`<h1 class='text-center bg-dark text-white'>DATA IS NOT FOUND IN THE PRODUCT USER TABLE</h1>`
           }
           else
           {
             var disp3=`
             <tr>
               <th>Order ID</th>
               <th>User ID</th>
               <th>Order Total</th>
             </tr>`;
             for(let row3 of data3)
             {
               disp3+=`
               <tr>
                 <th>${row3[0]}</th>
                 <th>${row3[1]}</th>
                 <th>${row3[2]}</th>
               </tr>
               `
             }
           }
           $('#o_disp_data').html(disp3)
         }
       })
     }
     display_product_order()
     $(document).on('click','checkout',function(){
      prd_qty=$(this).data('id');
      $.ajax({
        url:'/insert_ord_detail',
        url
      })

     })
})
