# General settings
MAIN_URL = "https://www.thingiverse.com/"  # Url of the main domain
THINGS_PER_PAGE = 20  # Number of things found in each explore page

# File naming suffix
DATE_SUFFIX = "_%d%m%Y-%H%M"

class ExploreList:
    THING_CARD = "ThingCard__thingCard--fG91n"
    CARD_BODY = "ThingCardBody__cardBodyWrapper--BLLzJ"
    THING_LIKES = "CardActionItem__text--Regp7"


class UserSettings:
    class Elements:
        FOLLOWERS = 'followers'
        FOLLOWING = 'following'
        DESIGNS = 'designs'
        FAVORITES = 'favorites'
        COLLECTIONS = 'collections'
        MAKES = 'makes'
        LIKES = 'likes'
        TITLE = 'title'
        SKILL_LEVEL = 'skill'

    class Properties:
        USERNAME = 'username'
        FOLLOWERS = 'followers'
        FOLLOWING = 'following'
        DESIGNS = 'designs'
        FAVORITES = 'favorites'
        COLLECTIONS = 'collections'
        MAKES = 'makes'
        LIKES = 'likes'
        TITLES = 'titles'
        SKILL_LEVEL = 'skill_level'

    # Urls
    BASE_URL = "https://www.thingiverse.com/{}/designs"
    MAKES_URL = "https://www.thingiverse.com/{}/makes"

    # Regex
    USERNAME_REGEX = r"thingiverse.com/(.*)/"  # Regex string to search for username out of url. Group 1 is taken from this.

    # Classes
    PROFILE_ACTION_POSSIBLE_LABELS = ['followers', 'following', 'designs']
    PROFILE_ACTION_ITEM = "ProfileActionItem__container--1fTdX"
    PROFILE_ACTION_COUNT = "ProfileActionItem__count--1MaXx"
    PROFILE_ACTION_LABEL = "ProfileActionItem__label--2OlG9"

    TAB_POSSIBLE_LABELS = ['favorites', 'designs', 'collections', 'makes', 'likes']
    TAB_BUTTON = "MetricButton__tabButton--2rvo1"
    TAB_TITLE = "MetricButton__tabTitle--2Xau7"
    TAB_METRIC = "MetricButton__metric--FqxBi"

    ABOUT_WIDGET_TITLE = "UserAboutWidget__typesWrapper--1r1kj"
    ABOUT_WIDGET_SKILL = "UserAboutWidget__skillLevelWrapper--3eHjx"


class MakeSettings:
    class Elements:
        SOURCE = 'source'
        PAGE_INFO = 'page_info'
        LIKES = 'like'
        COMMENTS = 'comments'  # as appear in thingiverse
        SHARES = 'share'  # as appear in thingiverse
        VIEWS = 'views'  # as appear in thingiverse
        CATEGORY = 'category'
        PRINT_SETTINGS = 'print_settings'

    class Properties:
        MAKE_ID = 'make_id'
        THING_ID = 'thingiverse_id'
        USERNAME = 'username'
        UPLOADED = 'uploaded'
        LIKES = 'like'  # must be the same as in elements
        COMMENTS = 'comments'   # must be the same as in elements
        SHARES = 'share'   # must be the same as in elements
        VIEWS = 'views'
        CATEGORY = 'category'
        PRINT_SETTINGS = 'print_settings'

    BASE_URL = "https://www.thingiverse.com/make:{}"
    ID_REGEX = r"make:(\d*)"

    # Code in ThingScraper is using indices of the following list, thus - ORDER MATTERS
    POSSIBLE_PRINT_SETTINGS = ["Printer Brand",
                               "Printer Model",
                               "Rafts",
                               "Supports",
                               "Resolution",
                               "Infill",
                               "Filament Brand"]

    # Classes
    SOURCE = "card-img-holder"
    PAGE_INFO = "item-page-info"  ## Made by <username>, uploaded <time>
    INFO_CONTENT = "thing-info-content"  ## Print settings section
    SINGLE_PRINT_SETTING = "detail-setting"

    # LIKES, COMMENTS and SHARES
    POSSIBLE_ICONS = ['like', 'comment', 'share']
    METRIC_ITEM_PATH = "//div[@class='item-list-interactions' and @data-make-id='{make_id}']//a[@title='{icon_title}']"

    # VIEWS AND CATEGORY
    MAKE_INFO = "//h2[@class='section-header']"
    VIEWS = 'icon-views'
    VIEWS_REGEX = r'(\d*) Views'
    CATEGORY = 'icon-category'
    CATEGORY_REGEX = r"Found in (.*)"


class ThingSettings:
    class Elements:
        MODEL_NAME = 'model_name'
        CREATOR = 'created_by'
        TABS = 'tab_buttons'
        TAGS = 'tags'
        PRINT_SETTINGS = 'print_settings'
        LICENSE = 'license'
        REMIX = 'remix'
        CATEGORY = 'category'

    class Properties:
        THING_ID = 'thing_id'
        MODEL_NAME = 'model_name'
        USERNAME = 'username'
        UPLOADED = 'uploaded'
        FILES = 'thing_files'
        COMMENTS = 'comments'   # as appear in thingiverse, lowercase
        MAKES = 'makes'   # as appear in thingiverse, lowercase
        REMIXES = 'remixes'  # as appear in thingiverse, lowercase
        TAGS = 'tags'
        LICENSE = 'license'
        REMIX = 'remix'
        CATEGORY = 'category'
        LIKES = 'likes'
        PRINT_SETTINGS = 'print_settings'

    BASE_URL = r"https://www.thingiverse.com/thing:{}"
    MAKES_URL = BASE_URL + r'/makes'
    REMIXES_URL = BASE_URL + r'/remixes'  # currently not in use due to bug in thingiverse
    REMIX_BUTTON_PATH = "/html/body/div[1]/div/div/div/div[6]/div[1]/div[5]"  # currently not in use
    REMIX_METRIC_INDEX = 4
    ID_REGEX = r"thing:(\d*)"

    POSSIBLE_PRINT_SETTINGS = ["Printer Brand",  # ORDER OF PRINT SETTINGS MATTER
                               "Printer Model",
                               "Rafts",
                               "Supports",
                               "Resolution",
                               "Infill",
                               "Filament Brand",
                               "Filament Color",
                               "Filament Material"]
    FIND_SETTING_REGEX = r"(.*):\n(.*)"
    ENCODE_PRINT_SETTINGS = ['rafts', 'supports']
    PRINT_SETTINGS_ENCODER = {'yes': 1,
                              'no': 0,
                              "doesn't matter": -1}

    # Classes
    CARD_TITLE = "ThingCardHeader__cardNameWrapper--3xgAZ"
    MODEL_NAME = "DetailPageTitle__thingTitleName--sGpkS"
    CREATED_BY = "DetailPageTitle__thingTitleMeta--P5VUn"
    TAB_BUTTON = ".um-button.Tabs__tab--aC64Y"
    TAB_TITLE = "MetricButton__tabTitle--2Xau7"
    METRIC = "MetricButton__metric--FqxBi"
    TAG_LIST = "Tags__tagsList--xZV1A"
    TAG_SINGLE = "//div[@class='Tags__tagsList--xZV1A']/a"
    REMIX_SECTION = "RemixedFromSection__title--1Wb7x"
    REMIX_CARD = "ThingCardBody__cardBodyWrapper--ba5pu"
    CATEGORY_SECTION = "ThingsMoreSection__showMoreHeading--u2OAR"
    CATEGORY_NAME = "ThingsMoreSection__categoryName--3RWut"
    PRINT_SETTINGS = "//div[@id='Print Settings']/ul"
    PRINT_SETTING = "ThingPage__description--14TtH"
    BLOCK_TITLE = "ThingPage__blockTitle--3ZdLu"
    LICENSE = "License__licenseCode--Aezqo"


class Logs:
    FORMAT_LOG = '(%(asctime)s)  |  %(levelname)s  |  FILE:%(filename)s ' \
                 '  FUNC:%(funcName)s   LINE:%(lineno)d :  %(message)s'
    FORMAT_STREAM = '%(asctime)s: %(levelname)s: %(message)s'
    FORMAT_STREAM_V = FORMAT_LOG
    FORMAT_STREAM_Q = FORMAT_STREAM
    LEVEL_GENERAL = 'DEBUG'
    LEVEL_LOG = 'INFO'
    NAME_LOG = 'thingscraper'
    LOG_DIR = 'Logs'
    LOGGER_NAME = 'thingscraper'


class Errors:
    CONSTRUCTION_ERROR = "'url', '{0}' or `properties` (dictionary with '{0}' key) " \
                         "must be provided in order to create User instance."


class DB_builder:
    DB_NAME = 'thingiverse'
    DB_DIR = 'Database'
    SQL_CONSTRUCTION = "thingiverse.sql"


class google_ktree:
    api_address = 'https://kgsearch.googleapis.com/v1/entities:search?'
    main_list_identifier = 'itemListElement'
    res_identifier = 'EntitySearchResult'
    final_id = 'ktree_data'

    class Tags:
        scheme_type = "@type"
        type = "type"
        scheme_id = "@id"
        id = "id"
        dit_desc = "detailedDescription"
        res = 'result'
        res_score = 'resultScore'
