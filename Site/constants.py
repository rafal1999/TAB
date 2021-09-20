SEX_FEMALE = 'F'
SEX_MALE = 'M'
SEX_UNSURE = 'U'

SEX_OPTIONS = (
    (SEX_UNSURE, 'Unsure'),
    (SEX_FEMALE, 'Female'),
    (SEX_MALE, 'Male'),
    )

STAGE_ZERO   = '0' # kandydat zg�oszony
STAGE_FIRST  = '1' # test napisany               #TODO mo�e zmieni� na inty w bazie �atwiej sortowa�??
STAGE_SECOND = '2' # po rozmowie rekrutacyjnej
STAGE_THIRD  = '3' # po rozmowie finalnej po kt�rej dostaje odp tak/nie

STAGE_OPTIONS = (     #TODO W miejsca 0,1,2 nada� opisy jakie by by�y fajne (to co ma si� wy�wietla�)
    (STAGE_ZERO, '0'),      #!
    (STAGE_FIRST, '1'),     #!
    (STAGE_SECOND, '2'),    #!
    (STAGE_THIRD, '3')      #!
    )

HIRED_YES        = 'Y'
HIRED_NO         = 'N'
HIRED_IN_PROCESS = 'P'

HIRED_OPTIONS = (
    (HIRED_IN_PROCESS, 'In process'),
    (HIRED_YES, 'Yes'),
    (HIRED_NO, 'No'),
    )

PRESENT_YES =  'Y'
PRESENT_NO = 'N'
PRESENT_UNKNOWN = 'U'

PRESENT_OPTIONS = (
    (PRESENT_UNKNOWN, 'Unknown'),
    (PRESENT_YES, 'Yes'),
    (PRESENT_NO, 'No'),
)

MEETING_TYPE_TEST = 'T'
MEETING_TYPE_JOB_INTERVIEW = 'R'

MEETING_TYPE_OPTIONS = (
    (MEETING_TYPE_TEST,'Test'),
    (MEETING_TYPE_JOB_INTERVIEW,'Job interview'),
)

MEETING_STATUS_PLANNED = 'P'
MEETING_STATUS_CANCELLED = 'C'
MEETING_STATUS_CONFIRMED = 'N'

MEETING_STATUS_OPTIONS = (
    (MEETING_STATUS_PLANNED, 'Upcoming'),
    (MEETING_STATUS_CANCELLED, 'Cancelled'),
    (MEETING_STATUS_CONFIRMED, 'Confirmed'),
)