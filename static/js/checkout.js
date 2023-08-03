$(document).ready(function(){
   /*$("#checkout").on('click',function(){
    doc = new jsPDF("p", "mm", [300, 300])
    check_pdf=$("#check-bill").html()
    doc.fromHTML(check_pdf);
    doc.save("output.pdf");
   })*/
   $("#checkout").on('click',function(){
    var mywindow = window.open("", "PRINT", "height=600,width=600");
    mywindow.document.write(check_pdf=$("#check-bill").html());
    mywindow.document.close();
    mywindow.focus();
    mywindow.print();
    return true;
   })
})