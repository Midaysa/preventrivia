from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Poll, Question, Recommendation, Category, Choice, Answer, \
    Tip
from .serializers import PollSerializer, QuestionSerializer, \
    RecommendationSerializer, CategorySerializer, ChoiceSerializer, \
    AnswerSerializer, TipSerializer


class PollViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    
    def get_queryset(self):
        return self.request.user.profile.get_recommendations()
        

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    

class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
        

class TipViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
