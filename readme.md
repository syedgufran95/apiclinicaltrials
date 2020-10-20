# Api For ClinicalTrial Data <br><br>
We defined five endpoints in our API using python flask and request modules<br>
1: Endpoint 1 was created to convert XML files to a single CSV.<br>
2: Endpoint 2  was created to upload an XML file from the source to the destination on<br> 
   the local machine<br>
3. Endpoint 3 was created to append uploaded files to an already created CSV.<br>
4. Endpoint 4 was created to parse the file. It can take arguments and return those specified<br>
   fields or can return all the field if no argument is supplied<br>
5. Endpoint 5 was created to find the nct_id and return its information.<br>

## EndPoints<br>
### / <br>
### /upload <br>
### /append <br>
### /parse <br>
### /find <br>

## Description
---------------------
### / <br>
This Function Converts all the XML files into CSV and returns the message. <br>
http://127.0.0.1:5000/ <br>


<p align="center">
  <img src="https://user-images.githubusercontent.com/43085010/96542367-90a94d00-12bf-11eb-8131-ef65fdd51986.JPG" width="540" height="400">
</p> <br>
<br>

### /append <br> 

It takes the XML file and searches its nct_id 
If found returns message already present
And if not, it appends the XML file to the CSV. <br>
http://127.0.0.1:5000/append <br>


<p align="center">
  <img src="https://user-images.githubusercontent.com/43085010/96543299-b0417500-12c1-11eb-9582-31510d2ed43c.JPG" width="540" height="400">
</p> <br>

### /parse <br>
If no argument is supplied it returns the all the data in the CSV in JSON format
If the argument is supplied it returns all the columns specified with nct_id.<br>
CSV has total of 9 fields(nct_id, overall_status, start_date, completion_date, condition,  Study design info, eligibility, has_expanded_access, enrollment). <br>
http://127.0.0.1:5000/parse <br>
http://127.0.0.1:5000/parse?parsearg1=condition&arg2=start_date <br>


<p align="center">
  <img src="https://user-images.githubusercontent.com/43085010/96543415-f696d400-12c1-11eb-8410-2c8c973f01c3.JPG" width="270" height="400">
    <img src="https://user-images.githubusercontent.com/43085010/96543466-11694880-12c2-11eb-8800-f812b4411be3.JPG" width="270" height="400">
</p> <br>


### /find <br>
It takes nct_id and finds the nct_id in the CSV and return all the data relating to nct_id <br> 

<p align="center">
  <img src="https://user-images.githubusercontent.com/43085010/96543333-c7806280-12c1-11eb-849e-044884f3cbb7.JPG" width="270" height="400">
  <img src="https://user-images.githubusercontent.com/43085010/96543369-d830d880-12c1-11eb-83e4-bcba290d3b0d.JPG" width="270" height="400">
</p> <br>





