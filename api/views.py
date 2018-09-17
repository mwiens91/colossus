"""
Created on July 25, 2017

@author: Jessica Ngo (jngo@bccrc.ca)

Updated by Spencer Vatrt-Watts (github.com/Spenca)
"""
#============================
# Django & Django rest framework imports
#----------------------------
import django_filters
from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny


#============================
# App imports
#----------------------------
from .serializers import (
    SampleSerializer,
    LibrarySerializer,
    LaneSerializer,
    SequencingSerializer,
    SublibraryInformationSerializer,
    AnalysisInformationSerializer,
    AnalysisRunSerializer,
    ChipRegionSerializer
)

from core.models import (
    Sample,
    DlpLibrary,
    DlpSequencing,
    DlpLane,
    SublibraryInformation,
    ChipRegion
)

from sisyphus.models import DlpAnalysisInformation, AnalysisRun


#============================
# Other imports
#----------------------------


class SmallResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class SampleViewSet(viewsets.ModelViewSet):
    """
    View for Sample that is queryable by sample_ID.
    Try adding "?sample_id=SA928" without the quotes to the end of the url.
    """

    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_fields = (
        'sample_id',
    )


class LaneViewSet(viewsets.ModelViewSet):
    """
    View for Lanes.

    Lanes are queryable by its flowcell id.
    Try adding "?flow_cell_id=HKNHHALXX_8" without the quotes to the end of the url.

    See documentation here:
    https://www.bcgsc.ca/wiki/display/MO/Colossus+Documentation#ColossusDocumentation-ColossusRESTAPI
    """
    queryset = DlpLane.objects.all()
    serializer_class = LaneSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_fields = (
        'flow_cell_id',
        'sequencing',
    )


class SequencingViewSet(viewsets.ModelViewSet):
    """
    View for Sequencings.

    Sequencings are queryable by GSC library id.
    Try adding "?sequencingdetail__gsc_library_id=PX0566" without the quotes to the end of the url.

    See documentation here:
    https://www.bcgsc.ca/wiki/display/MO/Colossus+Documentation#ColossusDocumentation-ColossusRESTAPI
    """
    queryset = DlpSequencing.objects.all()
    serializer_class = SequencingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_fields = (
        'dlpsequencingdetail__gsc_library_id',
    )


class LibraryViewSet(viewsets.ModelViewSet):
    """
    View for Library that is queryable by pool_id (aka chip ID) and sample it belongs to.

    See documentation here:
    https://www.bcgsc.ca/wiki/display/MO/Colossus+Documentation#ColossusDocumentation-ColossusRESTAPI
    """

    queryset = DlpLibrary.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_fields = (
        'id',
        'pool_id',
        'sample__sample_id',
        'jira_ticket',
    )


class SublibraryViewSet(viewsets.ModelViewSet):
    """
    View for Library's Sublibraries that is queryable by Library's pool_id (aka chip id)
    """
    queryset = SublibraryInformation.objects.all()
    serializer_class = SublibraryInformationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_fields = (
        'library__pool_id',
    )


class AnalysisInformationFilter(django_filters.FilterSet):
    """"
    https://django-filter.readthedocs.io/en/latest/guide/usage.html
    DateFromToRangeFiler() :it uses datetime format values instead of numerical values.
    It can be used with DateTimeField.
    """
    analysis_run__last_updated = django_filters.DateFromToRangeFilter()

    class Meta:
        model = DlpAnalysisInformation
        fields = [
        'priority_level',
        'analysis_jira_ticket',
        'version',
        'analysis_submission_date',
        'reference_genome',
        'analysis_run',
        'analysis_run__last_updated',
        'id',
        'analysis_run__run_status',
         'library__pool_id'
        ]


class AnalysisInformationViewSet(viewsets.ModelViewSet):
    """
    View for Analysis Objects
    Analysis Objects are queryable by Jira ticket
    """
    queryset = DlpAnalysisInformation.objects.all()
    serializer_class = AnalysisInformationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_class = AnalysisInformationFilter
    lookup_field = 'analysis_jira_ticket'


class AnalysisRunViewSet(viewsets.ModelViewSet):
    """
    View for AnalaysisRun Objects
    Should be be AllowAll so that Sisyphus can modify it
    """
    queryset = AnalysisRun.objects.all()
    serializer_class = AnalysisRunSerializer
    permission_classes = (AllowAny,)
    filter_fields = (
        'id',
        'last_updated',
        'run_status',
        'dlpanalysisinformation',
        'log_file'
    )


class ExperimentalMetadata(viewsets.ModelViewSet):
    """
    View for ChipRegion Objects
    ChipRegion Objects are queryable by Jira ticket or library pool id
    """
    queryset = ChipRegion.objects.all()
    serializer_class = ChipRegionSerializer
    permission_classes = (AllowAny,)
    filter_fields = (
        'library__jira_ticket',
        'library__pool_id',
    )
