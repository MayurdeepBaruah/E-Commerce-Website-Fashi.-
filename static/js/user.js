$(document).ready(function()
{
    function display_product_user(){
        $.ajax({
          url:'/display_product_user',
          type:'POST',
          success: function(data2)
          {
            if(data2.length <=0 || data2==0)
            {
              disp2=`<h1 class='text-center bg-dark text-white'>DATA IS NOT FOUND IN THE PRODUCT USER TABLE</h1>`
            }
            else
            {
              var disp2=`
              <tr>
                <th>User ID</th>
                <th>User Name</th>
                <th>User Email</th>
                <th>User Password</th>
                <th>User Age</th>
                <th>User Gender</th>
                <th>User Address</th>
                <th>User Mobile</th>
              </tr>`;
              for(let row2 of data2)
              {
                disp2+=`
                <tr>
                  <th>${row2[0]}</th>
                  <th>${row2[1]}</th>
                  <th>${row2[2]}</th>
                  <th>${row2[3]}</th>
                  <th>${row2[4]}</th>
                  <th>${row2[5]}</th>
                  <th>${row2[6]}</th>
                  <th>${row2[7]}</th>
                </tr>
                `
              }
            }
            $('#u_disp_data').html(disp2)
          }
        })
      }
      display_product_user()
    
    $('#user_register').on('click', function()
    {
        var user_data=new FormData(this.form);
        for(let i of user_data)
        {
            console.log(i)
        }
        $.ajax({
            url:'/Insert_User',
            type:'POST',
            contentType: false,
            processData: false,
            data: user_data,
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