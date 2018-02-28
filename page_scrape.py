from bs4 import BeautifulSoup

html = """
  
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">




  

<html>
<HEAD>




<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<META name="GENERATOR" content="IBM WebSphere Studio">


<LINK href="FormStyle.css" rel="stylesheet" type="text/css"> 
<TITLE> Virginia Courts Case Information System </TITLE>
<!-- Disabling Back Button -->
<!--window.history.forward(1);-->
<style> 
	.even{background-color: ffffff;} 
	.odd{background-color: c0c0c0;} 
</style>
<script language="javascript" type="text/javascript" src="js/CriminalCaseDetails.js"> 
</SCRIPT>

</HEAD>
<body  onLoad="goHist();alternate('count'); " >
 

<table class=outer align="center" width="100%"> 
 <tr><td>
 <table class=inner cellspacing="0" cellpadding="0">
  <tr>
  <td align="center">
  	<script language="Javascript" type="text/javascript">
	function hideHeader() {
		document.getElementById("headerDiv").style.display = "none";
	}
</script>
<div id="headerDiv" onclick="hideHeader()" title="Hide Header Image" alt="Hide Header Image"><div id="headerImgDiv"></div></div> 

  </td>
  </tr>
  <tr>
  <td id= BackgroundWhite align = "center">
     
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<HTML>
<HEAD>





<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<META name="GENERATOR" content="IBM WebSphere Studio">

</HEAD>
<BODY>

    
<table cellspacing="5">
 <tr>
 <td>
 
	  <form action = "hearSearch.do" method="post" >
	   <INPUT type= "hidden" name= "submitValue" value="HA"> 
	    <div id= "hearList">
	    <input type="submit" value="  Hearing List " onclick="javascript:submitCheck()">
	    </div>
	  </form>
	   
   
 </td>
 
 <td>

 <form action ="CaseDetail.do" method="post">  
   <INPUT type= "hidden" name= "submitValue" value="P"> 
    <INPUT type= "hidden" name= "courtId" value="003"> 
   <INPUT type="hidden" name= "categorySelected" value='R'>
   <INPUT type="hidden" name= "caseStatus" value='A'> 
   
    <INPUT type="hidden" name= "caseSelected" value='1600007300'>
 
  <div id= "pleadings">
    <input type="submit" value="  Pleadings/Orders " onclick="javascript:submitCheck()">
 </div>
 </form>
 </td> 
 <td>
 
 <form action ="CaseDetail.do" method="post">
    <INPUT type= "hidden" name= "submitValue" value="S">
    <INPUT type= "hidden" name= "page" value=AllCase> 
     <INPUT type= "hidden" name= "courtId" value=003> 
     <INPUT type="hidden" name= "categorySelected" value='R'>
    <INPUT type="hidden" name= "caseStatus" value='A'> 
    
 
    <INPUT type="hidden" name= "caseSelected" value='1600007300'>
  
 
 <div id= "services">
    <input type="submit" value="  Services " onclick="javascript:submitCheck()">
 </div>
 
 </form> 
 </td>
 
 <td>
 <div id= "nameList"> 
 <form action= "MainMenu.do" method= "POST"> 
    <INPUT type= "hidden" name= "courtId" value="003">     
 <div id= "mainmenu">
   <INPUT type="submit" value="Main Menu" onclick="javascript:showMainMenu()">
 </div>
 </form>
 </div>
 </td>
 
 <td>
 <form id= "nextForm" action= "Logoff.do" method= "POST">
   <INPUT type="hidden" name= "searchType">
 <div id= "logoff">
   <INPUT type="submit" value="Logoff" onclick="javascript:submitCheck()">
 </div>
 </form>
 </td>	
 		
 </tr>
</table>
</BODY>
</HTML>

     
  </td>
  </tr>
  <tr id= BackgroundWhite>
  <td>
  
   <div id= "fontMainmenuLarger" align="center">
       Albemarle County Circuit
   <span id="blackFont"> - Criminal Division </span>
   </div>
   
   <div id="fontMainmenuSmaller" align="center">
   Case Details
   </div>	  
 
  <!-- </td>
   </tr>   -->
   <table width="100%" border="0" align="center">
   <tr><td>
   <table width="80%" cellspacing="2" cellpadding="2" border="2" align="center">
	<tr>
	<td nowrap valign="top"><DIV id=fontBold>Case&nbsp;Number:</div>
	CR16000073-00&nbsp;	
	</td>  	   
	<td nowrap valign="top"><DIV id=fontBold>Filed:</div>
	02/01/2016&nbsp;
	</td>
	<td nowrap valign="top"><DIV id=fontBold>Commenced&nbsp;by: </div>
	Direct Indictment&nbsp;
	</td>
	<td nowrap valign="top"><DIV id=fontBold>Locality: </div>
	COMMONWEALTH OF VA  &nbsp;
	</td>
	</tr> 
	<tr>
	<td nowrap valign="top"><DIV id=fontBold>Defendant: </div>
	HURD, LEROY TYVIENNE&nbsp;
	</td>
	<td nowrap valign="top"><DIV id=fontBold>Sex: </DIV> 
	Male&nbsp;
	</td>
	<td nowrap valign="top"><DIV id=fontBold>Race:  </DIV>
	Black (Non-Hispanic)&nbsp;
	</td>
    <td nowrap valign="top"><DIV id=fontBold>DOB: </DIV>  
	05/26/****&nbsp;
	</td>
	</tr>	
<!-- To check for aka and display only when its not null     --->	
   
		
	
	
	
	<tr>
	<td colspan="5">
	<DIV id=fontBold>Address:  </DIV>
	CHARLOTTESVILLE, VA 22901&nbsp;
	</td>
	</tr>
		
	<tr>
	<td nowrap valign="top"><DIV id=fontBold>Charge: </div>
	COMPUTER SOLICIATION 2ND&nbsp;
	</td>
	<td nowrap valign="top"><DIV id=fontBold>Code&nbsp;Section: </div>
	18.2-374.3&nbsp;
	</td>
	<td nowrap valign="top"><DIV id=fontBold>Charge&nbsp;Type: </div>
	Felony&nbsp;
	</td>
	<td nowrap valign="top"><div id=fontBold>Class: </div> 
	&nbsp;
	</td>			
	</tr>
	<tr>
	<td nowrap valign="top"><DIV id=fontBold>Offense&nbsp;Date: </div>
	10/28/2014&nbsp;
	</td>
	<td nowrap valign="top"><DIV id=fontBold>Arrest Date: </div>
	02/04/2016&nbsp;
	</td>
	<td colspan="2">
	
	
	
	&nbsp;
	</td>				
	</tr>
   </table>
   <br/>
   <tr><td>
   
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">





<html>
<HEAD>



</HEAD>

<TABLE BORDER="0" width="80%" align="center" > 
<tr>
<td>
<div id = headerDisplay>Hearings</div> 
<br/>
</td>
</tr>
</table>
<TABLE BORDER="1" width="80%" align="center"  id= "count"> 
<tr>
<TD align= center><span id=hearingFont style="white-space: nowrap;"> # </span></TD>
<TD align= center><span id=hearingFont style="white-space: nowrap;"> Date</span></TD>
<TD align= center><span id=hearingFont style="white-space: nowrap;"> Time</span></TD>
<TD align= center><span id=hearingFont style="white-space: nowrap;"> Type</span></TD>
<TD align= center><span id=hearingFont style="white-space: nowrap;"> Room</span></TD>
<TD align= center><span id=hearingFont style="white-space: nowrap;"> Plea</span></TD>
<TD align= center><span id=hearingFont style="white-space: nowrap;"> Duration</span></TD>
<TD align= center><span id=hearingFont style="white-space: nowrap;"> Jury</span></TD>
<TD align= center><span id=hearingFont style="white-space: nowrap;"> Result</span></TD>
</tr>

<tr>
<td nowrap>
1  
&nbsp;
</td>
<td nowrap>
02/01/2016 
&nbsp;
</td>
<td nowrap>
9:30AM
&nbsp;
</td>
<td nowrap>
Grand Jury
&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>
 
&nbsp;
</td>
<td nowrap>
True Bill
&nbsp;
</td>
</tr>

<tr>
<td nowrap>
2  
&nbsp;
</td>
<td nowrap>
02/02/2016 
&nbsp;
</td>
<td nowrap>
11:30AM
&nbsp;
</td>
<td nowrap>
Capias
&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>
 
&nbsp;
</td>
<td nowrap>
Capias-Defendant Arrested
&nbsp;
</td>
</tr>

<tr>
<td nowrap>
3  
&nbsp;
</td>
<td nowrap>
02/10/2016 
&nbsp;
</td>
<td nowrap>
3:00PM
&nbsp;
</td>
<td nowrap>
Trial
&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>
Guilty
&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>
 
&nbsp;
</td>
<td nowrap>
Tried
&nbsp;
</td>
</tr>

<tr>
<td nowrap>
4  
&nbsp;
</td>
<td nowrap>
06/08/2016 
&nbsp;
</td>
<td nowrap>
3:30PM
&nbsp;
</td>
<td nowrap>
Pre-Sentence Report
&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>

&nbsp;
</td>
<td nowrap>
 
&nbsp;
</td>
<td nowrap>
Sent
&nbsp;
</td>
</tr>

</table>
</html>

   </td></tr>
   <br/>  
   <tr>
   <td>
   <br/>
   
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

 



<html>
<HEAD>

<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<META name="GENERATOR" content="IBM WebSphere Studio">
<LINK href="FinalDispositionStyle.css" rel="stylesheet" type="text/css"> 
</HEAD>

<TABLE BORDER="0" width="80%" align="center"> <tr>
<tr>
<td>
<h3>Final Disposition</h3>
</td>
</tr>
</table>

<table width="80%" border="1" align="center">
 <tr>
 <td nowrap valign="top"><DIV id=fontBold>Disposition&nbsp;Code:</div>
 Guilty&nbsp;
 </td>
 <td nowrap valign="top"><DIV id=fontBold>Disposition&nbsp;Date:</div>
 06/08/2016&nbsp;
 </td>
 <td nowrap valign="top"><DIV id=fontBold>Concluded&nbsp;By:</div>
 Trial - Judge With Witness&nbsp;
 </td>
 </tr>
 <tr>
 <td nowrap valign="top"><DIV id=fontBold>Amended Charge: </div>
 &nbsp;
 </td>
 <td nowrap valign="top"><DIV id=fontBold>Amended&nbsp;Code&nbsp;Section:</div>
 &nbsp;
 </td>
 <td nowrap valign="top"><DIV id=fontBold>Amended&nbsp;Charge&nbsp;Type:</div>
 &nbsp;
 </td>
 </tr>
 </TABLE>
 <BR clear="all">
<TABLE width="80%" border="1" align="center">
<TBODY>
 <TR>
 <td nowrap valign="top"><DIV id=fontBold>Jail/Penitentiary: </DIV>
 Penitentiary&nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Concurrent/Consecutive: </DIV>
 Sentence Is Run Consecutively With Another&nbsp;</TD>
 <td nowrap valign="top" valign="top"><DIV id=fontBold>Life/Death: </DIV>
 &nbsp;</TD>
 </TR>
 <TR>
 <td nowrap valign="top"><DIV id=fontBold>Sentence&nbsp;Time: </DIV>
 10 Year(s)&nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Sentence&nbsp;Suspended: </DIV>
 8 Year(s)&nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Operator&nbsp;License&nbsp;Suspension&nbsp;Time: </DIV>
 &nbsp;</TD>
 </TR>
 <TR>
 <td nowrap valign="top"><DIV id=fontBold>Fine&nbsp;Amount: </DIV>
 &nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Costs: </DIV>
 &nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Fines/Cost&nbsp;Paid: </DIV>
 &nbsp;</TD>
 </TR>
 <TR>
 <td nowrap valign="top"><DIV id=fontBold>Program&nbsp;Type: </DIV>
 &nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Probation&nbsp;Type: </DIV>
 Supervised&nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Probation&nbsp;Time: </DIV>
 1 Year(s)&nbsp;</TD> 
 </TR>
 <TR>
 <td nowrap valign="top"><DIV id=fontBold>Probation&nbsp;Starts: </DIV>
 Probation To Begin Upon Release&nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Court/DMV&nbsp;Surrender: </DIV>
 &nbsp;</TD>
 <TD nowrap valign="top"><DIV id=fontBold>Driver&nbsp;Improvement&nbsp;Clinic:	 </DIV>
 &nbsp;</TD>
 </TR> 
 <TR>
 <td nowrap valign="top"><DIV id=fontBold>Driving&nbsp;Restrictions: </DIV>
 &nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Restriction&nbsp;Effective&nbsp;Date: </DIV>
 &nbsp;</TD>
 <TD nowrap valign="top">
 	
 </TD>
 </TR> 
 <TR>
 <td nowrap valign="top"><DIV id=fontBold>VA Alcohol&nbsp;Safety&nbsp;Action: </DIV>
 &nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Restitution&nbsp;Paid: </DIV>
 &nbsp;</TD>
 <TD nowrap valign="top"><DIV id=fontBold>Restitution&nbsp;Amount: </DIV>
 &nbsp;</TD>
 </TR>
 <TR>
 <td nowrap valign="top"><DIV id=fontBold>Military: </DIV>
 &nbsp;</TD>
 <td nowrap valign="top"><DIV id=fontBold>Traffic&nbsp;Fatality: </DIV>
 &nbsp;</TD>
 <td nowrap valign="top">&nbsp;</TD>
 </TR>
 </TBODY>
</TABLE>
<br/>

</html>

   </td>
   </tr>    
   <tr>
   <td>
   <table width="80%" align="center">
   <tr>
   <td nowrap valign="top" > <div id="fontBold">Appealed Date:</div>
   
   </td>
   </tr>   
   <tr><td>&nbsp;</td></tr>   
   </table>  
	</td>
   </tr>
  </table>
  </td></tr>
 </table> 
 <tr>
 <td id=tdblue height=50 align="center">
    
       <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<HTML>
<HEAD>





<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<META name="GENERATOR" content="IBM WebSphere Studio">

</HEAD>
<BODY>

    
<table cellspacing="5">
 <tr>
 <td>
 
	  <form action = "hearSearch.do" method="post" >
	   <INPUT type= "hidden" name= "submitValue" value="HA"> 
	    <div id= "hearList">
	    <input type="submit" value="  Hearing List " onclick="javascript:submitCheck()">
	    </div>
	  </form>
	   
   
 </td>
 
 <td>

 <form action ="CaseDetail.do" method="post">  
   <INPUT type= "hidden" name= "submitValue" value="P"> 
    <INPUT type= "hidden" name= "courtId" value="003"> 
   <INPUT type="hidden" name= "categorySelected" value='R'>
   <INPUT type="hidden" name= "caseStatus" value='A'> 
   
    <INPUT type="hidden" name= "caseSelected" value='1600007300'>
 
  <div id= "pleadings">
    <input type="submit" value="  Pleadings/Orders " onclick="javascript:submitCheck()">
 </div>
 </form>
 </td> 
 <td>
 
 <form action ="CaseDetail.do" method="post">
    <INPUT type= "hidden" name= "submitValue" value="S">
    <INPUT type= "hidden" name= "page" value=AllCase> 
     <INPUT type= "hidden" name= "courtId" value=003> 
     <INPUT type="hidden" name= "categorySelected" value='R'>
    <INPUT type="hidden" name= "caseStatus" value='A'> 
    
 
    <INPUT type="hidden" name= "caseSelected" value='1600007300'>
  
 
 <div id= "services">
    <input type="submit" value="  Services " onclick="javascript:submitCheck()">
 </div>
 
 </form> 
 </td>
 
 <td>
 <div id= "nameList"> 
 <form action= "MainMenu.do" method= "POST"> 
    <INPUT type= "hidden" name= "courtId" value="003">     
 <div id= "mainmenu">
   <INPUT type="submit" value="Main Menu" onclick="javascript:showMainMenu()">
 </div>
 </form>
 </div>
 </td>
 
 <td>
 <form id= "nextForm" action= "Logoff.do" method= "POST">
   <INPUT type="hidden" name= "searchType">
 <div id= "logoff">
   <INPUT type="submit" value="Logoff" onclick="javascript:submitCheck()">
 </div>
 </form>
 </td>	
 		
 </tr>
</table>
</BODY>
</HTML>
	
    
 </td>
 </tr>

 </table>	
 
<div class="labelBuildNumber">Build #: 3.8.0.1</div>
	
 </body></html>



"""

soup = BeautifulSoup(html, 'html.parser')

# Demographics
main_table = soup.findAll('table')[4]

case_number = main_table.findAll('td')[0].text
name = main_table.findAll('td')[4].text
sex = main_table.findAll('td')[5].text
race = main_table.findAll('td')[6].text
charge = main_table.findAll('td')[9].text
code_section = main_table.findAll('td')[10].text
charge_type = main_table.findAll('td')[11].text

# Final Disposition
final_disposition_table = soup.findAll('table')[8]

disposition_code = final_disposition_table.findAll('td')[0].text
disposition_date = final_disposition_table.findAll('td')[1].text

# Results
results_table = soup.findAll('table')[9]
sentence_time = results_table.findAll('td')[4].text
probation_time = results_table.findAll('td')[11].text

if disposition_code.split()[2] == "Guilty" and len(probation_time.split()) > 2:
    print(case_number.split()[2])
    print(name)
    print(sex)
    print(race)
    print(charge)
    print(code_section)
    print(charge_type)

    print(disposition_code)
    print(disposition_date)

    print(sentence_time)
    print(probation_time)

# .replace('\t', '')