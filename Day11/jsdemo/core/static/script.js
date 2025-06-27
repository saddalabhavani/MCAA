<script>
function add()
{
var num1,num2,sum;
num1=parseInt(document.getElementById("txtFirstNumber").value);
num2=parseInt(document.getElementById("txtSecondNumber").value);
sum=num1+num2;
document.getElementById("txtAnswer").value=sum;
}
function sub()
{
var num1,num2,sub;
num1=parseInt(document.getElementById("txtFirstNumber").value);
num2=parseInt(document.getElementById("txtSecondNumber").value);
sub=num1-num2;
document.getElementById("txtAnswer").value=sub;
}
function mul()
{
var num1,num2,mul;
num1=parseInt(document.getElementById("txtFirstNumber").value);
num2=parseInt(document.getElementById("txtSecondNumber").value);
mul=num1*num2;
document.getElementById("txtAnswer").value=mul;
}
function clearScreen()
{
document.getElementById("txtFirstNumber").value="";
document.getElementById("txtSecondNumber").value=""; 
document.getElementById("txtAnswer").value="";
}
</script>