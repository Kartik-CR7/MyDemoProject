from django.shortcuts import render # Renders the request to the url or Other page Specified
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.db.models import Avg#if we want to import aggregrate function from models table
from django.db import connection
import socket #Imports the Host Ip Name and Address of Local Request PC
from mydemoapp.models import Like
# To import tables from models
from django.http import HttpResponse
from mydemoapp.models import BT_Contact
from mydemoapp.models import BT_Imageupload
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.conf import settings
from MyDemoProject.settings import MEDIA_URL
from MyDemoProject.settings import MEDIA_ROOT
from django.core.files.images import get_image_dimensions
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from smtplib import SMTPException
def firstpage(req):
    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        host_ip = x_forwarded_for.split(',')[0]
    else:
        host_ip = req.META.get('REMOTE_ADDR')
    #host_name = socket.gethostname()
    #host_ip = socket.gethostbyname(host_name)
        # btn_id = req.GET.get('btn_id')
        # btn_name= req.GET.get('btn_name')
        # print(str(btn_id)+ " btnidnew")
        # print(str(btn_name) + " btn_namenew")
        # btn = str(btn_id)
    # curb2 = connection.cursor()
    # curb2.execute("select count(distinct sess_response) from mydemoapp_like where button_id = 2")
    # Rec_newip_loadb2 = curb2.fetchone()

    cur_flag = connection.cursor()
    cur_flag.execute("select distinct button_id,case when (count(1) over(partition by sess_response,button_id))% 2 <> 0 then 'L' when (count(1) over(partition by sess_response,button_id))% 2 = 0 then 'U' end as Result,sess_response from mydemoapp_like where sess_response = '"+host_ip+"'")
    Flag_value = cur_flag.fetchall()
    connection.commit()
    Flag_btn_sess = [tup[0:2] for tup in Flag_value]
    Flagbtn_sess_val = dict(Flag_btn_sess)
    if Flag_value is not None:
         Flag = Flagbtn_sess_val
         print("flag is dict:" + str(Flag))
    else:
         Flag = 0
    print(Flag)

    # curb2_flag = connection.cursor()
    # curb2_flag.execute(
    #     "select distinct case when (count(1) over(partition by sess_response))% 2 <> 0 then 'L' when (count(1) over(partition by sess_response))% 2 = 0 then 'U' end as Result from mydemoapp_like where button_id = 2 and sess_response ='" + host_ip + "'")
    # Flag_valueb2 = curb2_flag.fetchone()
    # if Flag_valueb2 is not None:
    #     Flagb2 = Flag_valueb2[0]
    # else:
    #     Flagb2 = 0
    # print(Flagb2)

    cur1 = connection.cursor()
    cur1.execute("select final_tab.button_id,sum(final_tab.bin_cnt) from (select t2.button_id,t2.sess_response,t2.flag,case when t2.flag = 'O' then 1 when t2.flag = 'E' then 0 end as bin_cnt from  (select t1.button_id,t1.sess_response,t1.flag from (select distinct case when (count(1) over(partition by button_id,sess_response))% 2 <> 0 then 'O' when (count(1) over(partition by button_id,sess_response))% 2 = 0 then 'E' end as flag,sess_response,button_id from mydemoapp_like )t1 order by sess_response desc)t2) as final_tab group by final_tab.button_id")
    Rec_newip_load = cur1.fetchall()
    connection.commit()
    Newip_btn_cnt = [tup[0:2] for tup in Rec_newip_load]
    Newip_dic_btn_x_cnt = dict(Newip_btn_cnt)
    # print(Rec_newip_load)
    #
    # cur = connection.cursor()
    # cur.execute("select distinct button_id,case when (count(1) over(partition by sess_response,button_id))% 2 <> 0 then (select count(distinct sess_response) from mydemoapp_like) when (count(1) over(partition by sess_response,button_id))% 2 = 0 then (select count(distinct sess_response) from mydemoapp_like)-1 else 0 end as Result,sess_response from mydemoapp_like where sess_response ='" + host_ip + "'")
    # Record = cur.fetchall()
    # print(Record)
    # connection.commit()
    # btn_x_cnt_tup = [tup[0:2] for tup in Record]
    # print(btn_x_cnt_tup)
    # dic_btn_x_cnt = dict(btn_x_cnt_tup)
    # print(dic_btn_x_cnt)
    Cnt_x_btn_list = []
    # for i in Count_button_rec:
    #     for j in i:
    #         Cnt_x_btn_list.append(j)
    #     print (Cnt_x_btn_list)
    #
    # if Record:
    #     Rec1 = dic_btn_x_cnt
    #     print("Rec1 is Record:"+str(Rec1))
    #          # Record[0]
    # else:
    Rec1 = Newip_dic_btn_x_cnt
    print("newip record:"+str(Rec1))

    # if not Rec1:
    #     Rec1 = {'1':0,'2':0}
    #     print(Rec1)
         # Rec_newip_load[0]

    # curb2_rec = connection.cursor()
    # curb2_rec.execute(
    #     "select distinct case when (count(1) over(partition by sess_response))% 2 <> 0 then (select count(distinct sess_response) from mydemoapp_like) when (count(1) over(partition by sess_response))% 2 = 0 then (select count(distinct sess_response) from mydemoapp_like)-1 else 0 end as Result from mydemoapp_like where button_id = 2 and sess_response ='" + host_ip + "'")
    # Record_b2 = curb2_rec.fetchone()
    # connection.commit()
    # if Record_b2 is not None:
    #     Recb2 = Record_b2[0]
    # else:
    #     Recb2 = Rec_newip_loadb2[0]

    # print(str(Rec1)+ "On load likes")
    # cur1 = connection.cursor()
    # cur1.execute("select distinct case when (count(1) over(partition by sess_response))% 2 <> 0 then 'Y' else 'N' end as Result from MilieWebapp_like where sess_response ='" + host_ip + "'")
    # FLag_is_liked = cur1.fetchone()[0]
    print(req.method)
    # if req.method == 'POST':
    return render(req, 'mydemoapp/firstpage.html', {"message": Rec1, "flag": Flag})
    # else:
    # return render(req, 'mydemoapp/firstpage.html', {"message": Rec1, "flag": Flag})
        # "messageb2":Recb2,"flagb2":Flagb2})
# ,{"flag": FLag_is_liked}




def like_request(request):
    #host_name = socket.gethostname()
    #host_ip = socket.gethostbyname(host_name)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(request.method)

    btn_id = request.GET.get('btn_id')
    btn_name= request.GET.get('btn_name')
    print(str(btn_id)+ " btnid")
    print(str(btn_name) + " btn_name")

    #print(" NO btnid")
    if x_forwarded_for:
        host_ip = x_forwarded_for.split(',')[0]
    else:
        host_ip = request.META.get('REMOTE_ADDR')
    id = request.POST.get("idno")#Everytime entry primary key to a database wih sequnece incremental by 1
    aref = Like(id = id,sess_response = host_ip,button_id = btn_id)#posting values to database
    aref.save()# Saving  values to database
    #We can use Raw Query but its better to use cursor query by importing connections
    cur = connection.cursor()
    # cur.execute("select sum(final_tab.bin_cnt) from (select t2.button_id,t2.sess_response,t2.flag,case when t2.flag = 'O' then 1 when t2.flag = 'E' then 0 end as bin_cnt from  (select t1.button_id,t1.sess_response,t1.flag from (select distinct case when (count(1) over(partition by button_id,sess_response))% 2 <> 0 then 'O' when (count(1) over(partition by button_id,sess_response))% 2 = 0 then 'E' end as flag,sess_response,button_id from mydemoapp_like )t1 order by sess_response desc)t2) as final_tab where button_id = '"+btn_id+"'"+"group by button_id")
    cur.execute("select coalesce(sum(final_tab.bin_cnt),0) as cnt from mydemoapp_bt_imageupload left join (select t2.button_id,t2.sess_response,t2.flag,case when t2.flag = 'O' then 1 when t2.flag = 'E' then 0 end as bin_cnt from  (select t1.button_id,t1.sess_response,t1.flag from (select distinct case when (count(1) over(partition by button_id,sess_response))% 2 <> 0 then 'O'  when (count(1) over(partition by button_id,sess_response))% 2 = 0 then 'E' end as flag,sess_response,button_id from mydemoapp_like )t1  order by sess_response desc)t2) as final_tab on mydemoapp_bt_imageupload."+'"'+"Image_id"+'"'+"::varchar"+" = final_tab.button_id where mydemoapp_bt_imageupload."+'"'+"Image_id"+'"' +"= '" + btn_id + "'" + "group by mydemoapp_bt_imageupload."+'"'+"Image_id"+'"'+" order by mydemoapp_bt_imageupload."+'"'+"Image_id"+'"' +"desc")
        # "select distinct case when (count(1) over(partition by sess_response,button_id))% 2 <> 0 then (select count(distinct sess_response) from mydemoapp_like) when (count(1) over(partition by sess_response,button_id))% 2 = 0 then (select count(distinct sess_response) from mydemoapp_like)-1 else 0 end as Result from mydemoapp_like where sess_response ='"+ host_ip + "'"+"and button_id ="+ btn_id)
    # cur.execute("select distinct case when (count(1) over(partition by sess_response))%2<> 0 then (select count(distinct sess_response) from MilieWebapp_like) else (select count(distinct sess_response) from MilieWebapp_like)- 1 end from MilieWebapp_like  where sess_response ="+str(host_ip))
    Rec = cur.fetchone()[0]#For First location of RawQueryset
    # Rec = Like.objects.all().count()--- just to count all values of table like select count(*) from table
    print (str(Rec)+"from db")
    # cur1 = connection.cursor()
    # cur1.execute("select distinct case when (count(1) over(partition by sess_response))% 2 <> 0 then 'Y' else 'N' end as Result from MilieWebapp_like where sess_response ='" + host_ip + "'")
    # FLag_is_liked = cur1.fetchone()[0]
    return JsonResponse({"message": Rec})
    # , {"Flag": FLag_is_liked}
    #return jsonify({"message": Rec})
    # return render(request,'firstpage.html',{"message": Rec})


def ContactUsPage(request):
    return render(request, 'ContactU.html')
    print(request.method)


def ContactUsSubmit(request):
    Contact_id = request.POST.get("Contact_id")
    FirstName = request.POST.get("First_Name")
    LastName = request.POST.get("Last_Name")
    Emailid = request.POST.get("Emailid")
    Message = request.POST.get("Message")
    print(Emailid)
    # try:
    # validate_email(Emailid)
    # return (request, 'ContactU.html', {"Alert": "Email Is Correct"})
    to = EMAIL_HOST_USER
    email = EmailMessage((FirstName+' '+LastName+'- Email_ID:'+ Emailid),Message,'DONOTREPLY<milieshankhdharblog@gmail.com>',[to])
    try:
        email.send(fail_silently = False)#if false then would redirect to error but if set true then it will silently show it on terminal but not on page.
    except SMTPException as e:
        #print('There was an error sending an email: ', e)
        msg = "Not a valid Email!!"
        # Detail_valid = 'I'
        #return HttpResponse('Invalid email found!',e)
    except socket.gaierror:
        return HttpResponse('<html><body><h2>Please check your internet Connection!</h2></body></html>')
    else:

            aref = BT_Contact(Contact_id=Contact_id, First_Name=FirstName, Last_Name=LastName, Emailid=Emailid,
                              Message=Message)
            aref.save()
            # Detail_valid = 'V'
            # return HttpResponseRedirect('/ContactUSubmit/')
            msg = "Thanks for your valuable feedback/Interest!"
    return render(request,'ContactU.html',{"message": msg,"First_Name":FirstName,"Last_Name": LastName,"Messagecode":Message})
    #(request, 'ContactU.html',
    # send_mail(FirstName, Message, Emailid, ['sharmakartik717@gmail.com'])
#############################################################################################################

def TravelPage(request):
    return render(request,'mydemoapp/Travel_page.html')

#############################################################################################################

def TravelImagePost(request):
    # list = []  # myfile is the key of a multi value dictionary, values are the uploaded files
    Image_id = request.POST.get("id")
    Image_name = request.POST.get("About_Upload")
    # Files = request.FILES['Files']# for only single uploaded files
    for f in request.FILES.getlist('Images'):  # myfile is the name of your html file button
        print('filename'+str(f.name))#both same
        print('value of f:'+str(f))#both same
        aref = BT_Imageupload(Image_id = Image_id,Image_name = Image_name,Image = f)
        aref.save()
    #Start: New patch for handling 404 error when using unwanted server request    
    try:
        HttpResponse("Your Upload in progress!!")
    except:
           raise Http404("<h1>Page not found!!</h1>")    
    #end: New patch for handling 404 error when using unwanted server request       
    # return HttpResponse("file uploaded")
    return redirect('/TravelImagePagerefresh/')
    #render(request,'mydemoapp/TravelImageDisplay.html',{"All_Images":All_Images,"media_url": MEDIA_URL,"message":Rec1})

def TravelImageRefresh(request):
    # All_Images = BT_Imageupload.objects.all()
    cur_image = connection.cursor()
    cur_image.execute("select mydemoapp_bt_imageupload."+'"'+"Image_name"+'"'+",mydemoapp_bt_imageupload."+'"'+"Image_id"+'"'+",mydemoapp_bt_imageupload."+'"'+"Image"+'"'+",coalesce(sum(final_tab.bin_cnt),0) as cnt,coalesce(final_tab.flag,'N') as flag from mydemoapp_bt_imageupload left outer join (select t2.button_id,t2.sess_response,t2.flag,case when t2.flag = 'O' then 1 when t2.flag = 'E' then 0 end as bin_cnt from (select t1.button_id,t1.sess_response,t1.flag from (select distinct case when (count(1) over(partition by button_id,sess_response))% 2 <> 0 then 'O' when (count(1) over(partition by button_id,sess_response))% 2 = 0 then 'E' end as flag, sess_response, button_id from mydemoapp_like )t1 order by sess_response desc)t2) as final_tab on mydemoapp_bt_imageupload."+'"'+"Image_id"+'"'+"::varchar = final_tab.button_id group by mydemoapp_bt_imageupload."+'"'+"Image_id"+'"'+",final_tab.flag order by mydemoapp_bt_imageupload."+'"'+"Image_id"+'"'+" desc")
    Images = cur_image.fetchall()
    print(Images)
    # tup_image_x_btn = [tup[0:5] for tup in Images]
    # Pagination_lst = [tup[2:3] for tup in Images]
    qry_list = list(Images)
    print("qry_list:"+str(qry_list))
    ############################################################################pagination
    paginator = Paginator(qry_list,1)  # Show 1 image per page
    page = request.GET.get('page')
    try:
        qry_list = paginator.page(page)
        print(qry_list)
    except PageNotAnInteger:
    #if page is not an integer deliver first page
        qry_list = paginator.page(1)
    except EmptyPage:
        #if page is out of range then deliver last page of result
        qry_list = paginator.page(paginator.num_pages)
    # return render(request, 'list.html', {'contacts': contacts})

    # print("here tuples:"+str(tup_image_x_btn))
    # # All_Images = dict(Images)
    # print(All_Images)
    # cur1 = connection.cursor()
    # cur1.execute("select final_tab.button_id,sum(final_tab.bin_cnt) from (select t2.button_id,t2.sess_response,t2.flag,case when t2.flag = 'O' then 1 when t2.flag = 'E' then 0 end as bin_cnt from  (select t1.button_id,t1.sess_response,t1.flag from (select distinct case when (count(1) over(partition by button_id,sess_response))% 2 <> 0 then 'O' when (count(1) over(partition by button_id,sess_response))% 2 = 0 then 'E' end as flag,sess_response,button_id from mydemoapp_like )t1 order by sess_response desc)t2) as final_tab group by final_tab.button_id")
    # Rec_newip_load = cur1.fetchall()
    # connection.commit()
    # Newip_btn_cnt = [tup[0:2] for tup in Rec_newip_load]
    # Newip_dic_btn_x_cnt = dict(Newip_btn_cnt)
    # Rec1 = Newip_dic_btn_x_cnt
    # for Rec1_value in Rec1.values():
    #     print(Rec1_value)
    # print("newip record HERE:" + str(Rec1))
    prod_url = 'https://karsharma.s3.amazonaws.com'+ MEDIA_URL
    return render(request,'mydemoapp/TravelImageDisplay.html',{"media_url": prod_url,"qry_list": qry_list})
#"message": Rec1,
#"All_Images":All_Images,

#############################################################################################################
