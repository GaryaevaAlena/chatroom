from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import *

from .models import *

@login_required
def profile_edit(request):
    user_form = UserEditForm(instance=request.user, data=request.POST)
    profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/page/profile/')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                        'page/profile_edit.html',
                        {'user_form': user_form,
                        'profile_form': profile_form})

class UserProfile(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'page/myprofile.html'
    context_object_name = 'chats'

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(penPal=user)


class Profile(DetailView):
    model = Profile
    template_name = 'page/profile.html'
    queryset = Profile.objects.all()
    context_object_name = 'Person'



class NewChat(ListView):
    model = Chat
    template_name = 'page/newchat.html'
    queryset = Chat.objects.all()
    context_object_name = 'Chat'

    def post(self, request):
        new_chat = Chat.objects.create(nameChat=request.POST['name'])
        pal = request.POST['user']
        penPal = User.objects.get(username=pal)
        new_chat.penPal.add(penPal)
        new_chat.penPal.add(request.user)
        return redirect('/page/profile/')


class EditChat(LoginRequiredMixin, UpdateView):
    model = Chat
    template_name = 'page/chat_edit.html'
    context_object_name = 'Chatter'
    form_class = ChatEdit

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Chat.objects.get(pk=id)

class Chatter(LoginRequiredMixin, DetailView):
    model = Chat
    context_object_name = 'chatter'
    template_name = 'page/chatter.html'
    queryset = Chat.objects.all()
