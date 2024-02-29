from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter
from .models import Post, Category


class PostFilter(FilterSet):
    post_category = ModelMultipleChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        conjoined=False,
    )

    creation_date_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }
