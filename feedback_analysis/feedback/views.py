from django.shortcuts import render
from .forms import FeedbackForm
from .models import CustomerFeedback
from textblob import TextBlob

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.sentiment = get_sentiment(review.review)
            review.save()
            return render(request, 'result.html', {'review': review})
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'form': form})

# Create your views here.
