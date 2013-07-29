from django.http import HttpResponse
from django.shortcuts import render
from webapp2.models import Mice , Images
from django.core import serializers
import matplotlib , StringIO
matplotlib.use('Agg')




def search_form(request):
    return render(request,'search_form.html')



def sql(id):
    sql1 = Mice.objects.get(pk=id).gender
    mouse_id = id
    return sql1,mouse_id





def search(request):
    from matplotlib import pyplot as plt
    datalist =[]
    givenlist =[]
    inputlist= []
    fulldata_list = []
    invalidlist =[]
    errors = []
    if 'q' in request.GET and request.GET['q']:
       query = request.GET.get("q",None)
       givenlist = query.splitlines()
       for x in givenlist:
           if x not in inputlist:
              inputlist.append(x)

       inputlist = filter(lambda name: name.strip(), inputlist)
       inputlist = [x.strip() for x in inputlist]
       input_count = len(inputlist)
       if input_count < 100:
          for item in reversed(inputlist):
              if item.isdigit() == False or ( len(item) > Mice._meta.get_field('mouse_id').max_length):
                 invalidlist.append(item)
                 inputlist.remove(item)
          for item in inputlist:
              if Mice.objects.filter(pk=item).exists() == False:
                 invalidlist.append(item)
                 inputlist.remove(item)

          for item in inputlist:
              gender , mouseid = sql(item)
              if (gender == 'M'):
                      width = 0.01
                      height = 1
                      toenumber = Mice.objects.get(pk=item).toe_number
                      fig1 = plt.figure()
                      ax = fig1.add_subplot(111)
                      rects1 = ax.bar(0,1,width, color='r')
                      ax.set_ylabel('toe_number')
                      ax.set_title('Graph for mouseid :%s' %mouseid )
                      ax.legend( (rects1), ('Males'))
                      fig1.add_axes(ax)
                      buffer = StringIO.StringIO()
                      fig1.savefig(buffer,format='png')
                      data=(buffer.getvalue()).encode('base64')
                      buffer.close()
                      datalist.append(data)
              elif (gender == 'F'):
                        width = 0.5
                        toenumber = Mice.objects.get(pk=item).toe_number
                        fig2 = plt.figure()
                        ax = fig2.add_subplot(111)
                        rects1 = ax.bar(0, 1, width, color='y')
                        ax.set_ylabel('toe_number')
                        ax.set_title('graph for mouseid : %s' %mouseid)
                        ax.legend( (rects1), ('Females'))
                        buffer = StringIO.StringIO()
                        fig2.savefig(buffer,format='png')
                        data=(buffer.getvalue()).encode('base64')
                        buffer.close()
                        datalist.append(data)
              else:
                  data = serializers.serialize('python',Mice.objects.filter(pk = item))
                  datalist.append(data)
                  fulldata_list.append(data)
                      #tables.append(fulldata_list)
          #for fig in figurelist:
           #   buffer = StringIO.StringIO()
           #  fig.savefig(buffer,format='png')
            #  data=(buffer.getvalue()).encode('base64')
            #  buffer.close()
             # imagedata.append(data)
       else:
           return HttpResponse("Your input exceeded the maximum value possible. You can only search for 100 values at a time ")
       return render(request, 'search_results.html',{'datalist':datalist,'invalidlist':invalidlist,'inputlist':inputlist,'input_count':input_count,'fulldata_list':fulldata_list},)
    else:
        errors.append("Please enter a valid id ")
        return render(request,'search_form.html',{'errors':errors})

                        
