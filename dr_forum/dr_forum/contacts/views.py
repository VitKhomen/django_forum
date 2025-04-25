from django.views.generic import CreateView, DetailView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy

from contacts.forms import ContactsForm
from contacts.models import Contacts


class ContactsCreateView(CreateView):
    model = Contacts
    form_class = ContactsForm
    template_name = 'main/contacts.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('contacts_answer', kwargs={'pk': self.object.pk})


class ContactsDetailView(DetailView):
    model = Contacts
    template_name = 'main/answer_contacts.html'
    context_object_name = 'contact'


class ContactsUpdateView(UpdateView):
    model = Contacts
    form_class = ContactsForm
    template_name = 'main/update_contact.html'

    def get_success_url(self):
        return reverse_lazy('contacts_answer', kwargs={'pk': self.object.pk})


class ContactsDeleteView(DeleteView):
    model = Contacts
    template_name = 'main/delete_contact.html'
    success_url = reverse_lazy('contacts')
