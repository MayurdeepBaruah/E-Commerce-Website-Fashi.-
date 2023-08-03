$(document).ready(function()
{
    $("#blog_upd_btn").hide();
    
    function display_blog()
    {
        $.ajax({
            url:'/display_blog',
            type: 'POST',
            success: function(blog_data){
                if(blog_data.length<=0 || blog_data==0)
                {
                    var disp_blog=`<h1 class="text-center bg-dark text-white">DATA NOT FOUND IN THE BLOG TABLE</h1>`;
                }
                else
                {
                    disp_blog=`
                    <tr>
                        <th>Blog ID</th>
                        <th>Blog Images</th>
                        <th>Blog Title</th>
                        <th>Blog Category</th>
                        <th>Blog Date</th>
                        <th>Blog Description</th>
                        <th>Blog Miscellaneous Description</th>
                    </tr>
                    `;
                    for(let i of blog_data)
                    {
                      disp_blog+=`
                        <tr>
                            <th>${i[0]}</th>
                            <th><img src="./static/Images/${i[1]}" alt="${i[1]}" style="width: 100px; height: 100px; border-radius: 5px;"></th>
                            <th>${i[2]}</th>
                            <th>${i[3]}</th>
                            <th>${i[4]}</th>
                            <th>${i[5]}</th>
                            <th>${i[6]}</th> 
                            <th><button type="button" class="btn btn-dark text-dark blog-upd" data-id="${i[0]}">UPDATE</th>
                            <th><button type="button" class="btn btn-dark text-dark blog-del" data-id="${i[0]}">DELETE</th>
                        </tr>
                        `
                    }
                }
                $("#blog_disp_data").html(disp_blog)
            }
        })
    }
    $("#blog_add_btn").on('click', function()
    {
        var data_blog=new FormData(this.form)
        $.ajax({
            url:'/Insert_Blog',
            type:'POST',
            contentType: false,
            processData: false,
            data: data_blog,
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
                $("#Blog-Modal").modal('hide')
                display_blog();
            }
        })
    })
    $(document).on('click','.blog-del', function(){
        var blog_ids=$(this).data('id');
        $.ajax({
            url:'/delete_blog',
            type:'DELETE',
            data:{'blog-id':blog_ids},
            success:function(res){
                if(res==1)
                {
                    alert('Deleted')
                }
                else
                {
                    alert('Error')
                }
                display_blog();
            }
        })
    })
    $("#blog_upd_btn").on('click', function(){
        var blog_ids=$(this).data('id');
        var upd_blog=new FormData(this.form)
        upd_blog.append('blog-id',blog_ids)
        for(let i of upd_blog)
        {
            console.log(i)
        }
        $.ajax({
            url:'/update1_blog',
            type:'PUT',
            contentType: false,
            processData: false,
            data: upd_blog,
            success: function(res)
            {
                if (res==1)
                {
                    alert('Updated')
                }
                else
                {
                    alert('Error')
                }
                $("#Blog-Modal").modal('hide')
                display_blog();
            }
        })
    })
    $(document).on('click','.blog-upd', function()
    {
        var blog_ids=$(this).data('id')
        $.ajax({
            url:'/update_blog',
            type:'POST',
            data:{'blog-id': blog_ids},
            success:function(res){
                data=res
                $('#filename').val(data[1])
                $('#blog_title').val(data[2])
                $('#blog_cat').val(data[3])
                $('#blog_desp').val(data[5])
                $('#blog_desp1').val(data[6])
                $('#blog_upd_btn').attr('data-id', data[0])
                $('#blog_upd_btn').show()
                $('#blog_add_btn').hide()
            }
        })
    $('#Blog-Modal').modal('show');
    })
    display_blog();
})