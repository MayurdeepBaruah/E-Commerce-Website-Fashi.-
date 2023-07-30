$(document).ready(function()
{
     function display_timer(){
      var count_date= new Date(" August 9, 2023 12:00:00 ").getTime();
      var a =setInterval(function()
      {
        var current_date=new Date().getTime();
        var b=count_date-current_date;
        var days= Math.floor(b/(1000*60*60*24))
        var hours = Math.floor((b % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((b % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((b % (1000 * 60)) / 1000);

        $("#count_timer").html(days)
        $("#count_timer1").html(hours)
        $("#count_timer2").html(minutes)
        $("#count_timer3").html(seconds)

        if (b<0)
        {
          clearInterval(a);
          $("#count_timer").html("Expired")
        }
      },1000);
     }
     display_timer() 
     $('.owl-carousel').owlCarousel({
      loop:true,
      margin:10,
      nav:true,
      autoplay:true,
      autoplayTimeout:3000,
      responsive:{
          0:{
              items:1
          },
          600:{
              items:2
          },
          1000:{
              items:3
          }
      }
  })
})



      

