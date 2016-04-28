# coding: utf-8

"""
    mParticle

    mParticle Event API

    OpenAPI spec version: 1.0.1
    Contact: support@mparticle.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into sdk package
from .models.api_response import ApiResponse
from .models.api_response_errors import ApiResponseErrors
from .models.app_event import AppEvent
from .models.application_information import ApplicationInformation
from .models.application_state_transition_event import ApplicationStateTransitionEvent
from .models.attribution_info import AttributionInfo
from .models.batch import Batch
from .models.breadcrumb_event import BreadcrumbEvent
from .models.commerce_event import CommerceEvent
from .models.crash_report_event import CrashReportEvent
from .models.device_current_state import DeviceCurrentState
from .models.device_information import DeviceInformation
from .models.event_base import EventBase
from .models.event_data import EventData
from .models.first_run_event import FirstRunEvent
from .models.geo_location import GeoLocation
from .models.media_info import MediaInfo
from .models.network_performance_event import NetworkPerformanceEvent
from .models.opt_out_event import OptOutEvent
from .models.product import Product
from .models.product_action import ProductAction
from .models.product_impression import ProductImpression
from .models.profile_event import ProfileEvent
from .models.promotion import Promotion
from .models.promotion_action import PromotionAction
from .models.push_message_event import PushMessageEvent
from .models.push_registration_event import PushRegistrationEvent
from .models.screen_view_event import ScreenViewEvent
from .models.session_end_event import SessionEndEvent
from .models.session_start_event import SessionStartEvent
from .models.shopping_cart import ShoppingCart
from .models.source_information import SourceInformation
from .models.user_identities import UserIdentities

# import apis into sdk package
from .apis.events_api import EventsApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration
