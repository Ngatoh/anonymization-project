from django.shortcuts import render
from django.contrib import admin
from .models import Post
from django.http import HttpResponseRedirect

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    def response_change(self, request, obj, post_url_continue =None):
        if '_generate_values' in request.POST:

            return HttpResponseRedirect("post/change/generate_values.html")
        return super().response_change(request, obj)
           #return TemplateResponse('post/chnge/generate_values.html', context {'variable': obj.id})
           #render(request, template_name='admin/anonymizer/post/generate_values.html')
           #context={'variable': 'obj.id'}


    #def detail(request, poll_id):
       #sreturn render(request, 'polls/detail.html', {'poll': p})

    #def get_urls(self):
        #urls = super().get_urls()
        #pattern = path('generate/<int:id>/', self.admin_site.admin_view(self.response_change), name='preview-pdf')
       # urls += pattern
       # return urls

