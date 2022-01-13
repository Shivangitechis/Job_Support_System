USER_STATUS = (
    ('active', 'Active'),
    ('deleted', 'Deleted')
)

USER_ROLE = (
    ('director', 'Director'),
    ('marketing', 'Marketing'),
    ('job_support', 'Job Support'),
    ('development', 'Development')
)

USER_PERMISSION = (
    ('normal', 'Normal'),
    ('manager', 'Manager')
)

GENDER = (
    ('male', 'Male'),
    ('female', 'Female')
)

STATUS = (
    ('graduated', 'Graduated'),
    ('preparing', 'Preaparing'),
    ('started_application', 'Started Application'),
    ('pause_application', 'Pause Application'),
    ('got_offer', 'Got an Offer'),
    ('failed', 'Failed to Get a Job'),
    ('deleted', 'Deleted')
)

APPLICATION_QUESTIONNAIRE_STATUS = (
    ('not_yet', 'Not Yet'),
    ('done', 'Done')
)

PORTFOLIO_STATUS = (
    ('not_started', 'Not Started Creating'),
    ('on_progress', 'On Progress'),
    ('done', 'Done by Developer Team'),
    ('reviewed', 'Reviewed by Job Support')
)

RESUME_STATUS = (
    ('not_started', 'Not Started Creating'),
    ('on_progress', 'On Progress'),
    ('done', 'Done by Developer Team'),
    ('reviewed', 'Reviewed by Job Support')
)

RESUME_QUESTIONNAIRE_STATUS = (
    ('not_yet', 'Not Yet'),
    ('done', 'Done')
)

GITHUB_STATUS = (
    ('not_started', 'Not Started Creating'),
    ('on_progress', 'On Progress'),
    ('done', 'Done by Developer Team'),
    ('reviewed', 'Reviewed by Job Support')
)

WAKEUP_SERVER_STATUS = (
    ('not_yet', 'Not Yet'),
    ('done', 'Done')
)

COURSE = (
    ('web', 'Web Development'),
    ('data', 'Data Science')
)

APPLIED_BY = (
    ('tech_is', 'TECH I.S.'),
    ('student', 'Student')
)

APPLICATIONS_STATUS = (
    ('applied', 'Applied'),
    ('offered', 'Offered'),
    ('deleted', 'Deleted')
)

JOB_PORTAL = (
    ('linkedin', 'LinkedIn'),
    ('indeed', 'Indeed'),
    ('monster', 'Monster'),
    ('glassdoor', 'Glassdoor'),
    ('work_day', 'Work Day'),
    ('smart_work', 'Smart Work'),
    ('dice', 'Dice')
)
INTERVIEW_STATUS = (
    ('scheduling', 'Scheduling'),
    ('scheduled', 'Scheduled'),
    ('done', 'Done and Waiting for the Result'),
    ('canceled', 'Canceled Interview by Company'),
    ('missed', 'Missed Interview by Student'),
    ('rejected', 'Rejected'),
    ('passed', 'Passed'),
    ('offered', 'Offered'),
    ('deleted', 'Deleted')
)
INTERVIEW_TYPE = (
    ('phone_call', 'Phone call'),
    ('assessment', 'Assessment'),
    ('video_call', 'Video Call'),
    ('onsite_interview', 'Onsite Interview')
)
INTERVIEW_STUDENT_TIMEZONE = (
    ('usa_eastern', 'USA/Eastern'),
    ('usa_central', 'USA/Central'),
    ('usa_mountain', 'USA/Mountain'),
    ('usa_pacific', 'USA/Pacific'),
    ('usa_arizona', 'USA/Arizona'),
    ('usa_alaska', 'USA/Alaska'),
    ('usa_hawaii', 'USA/Hawaii'),
)
