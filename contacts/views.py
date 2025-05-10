from django.views.generic import CreateView, DetailView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy

from contacts.forms import ContactsForm
from contacts.models import Contacts
from utils.models import SlugMixin


class ContactsCreateView(CreateView):
    model = Contacts
    form_class = ContactsForm
    template_name = 'contacts/contacts.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('contacts_answer', kwargs={'slug': self.object.url})


class ContactsDetailView(SlugMixin, DetailView):
    model = Contacts
    template_name = 'contacts/answer_contacts.html'
    context_object_name = 'contact'


class ContactsUpdateView(SlugMixin, UpdateView):
    model = Contacts
    form_class = ContactsForm
    template_name = 'contacts/update_contact.html'
    context_object_name = 'contact'

    def get_success_url(self):
        return reverse_lazy('contacts_answer', kwargs={'slug': self.object.url})


class ContactsDeleteView(SlugMixin, DeleteView):
    model = Contacts
    template_name = 'contacts/delete_contact.html'
    context_object_name = 'contact'
    success_url = reverse_lazy('contacts')
