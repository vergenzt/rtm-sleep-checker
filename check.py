import os
import rtmapi

def check_for_sleep_today(api):
    timeline = api.rtm.timelines.create().timeline.value

    search = '(tag:+sleep or tag:+wait) and (due:today or dueBefore:today)'
    result = api.rtm.tasks.getList(filter=search)
    for tasklist in result.tasks:
        for taskseries in tasklist:
            print 'Removing due date for "{}"'.format(taskseries.name)
            api.rtm.tasks.setDueDate(
                timeline=timeline,
                list_id=tasklist.id,
                taskseries_id=taskseries.id,
                task_id=taskseries.task.id
            )


if __name__=='__main__':
    api = rtmapi.Rtm(
        api_key = os.environ['RTM_API_KEY'],
        shared_secret = os.environ['RTM_SHARED_SECRET'],
        perms = 'write'
    )
    api.token = os.environ['RTM_TOKEN']

    check_for_sleep_today(api)

