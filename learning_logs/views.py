# learning_logs
from django.shortcuts import render
from .models import Topic


def index(request):
    """Show the home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'subject1': topic.subject1,
        'subject2': topic.subject2,
        'entries': entries,
    }
    # Looked at the instructions again after the update and needed to add a page (topic.html):
    # change the rendered template below from 'learning_logs/topics.html' to 'learning_logs/topic.html'.
    return render(request, 'learning_logs/topic.html', context)