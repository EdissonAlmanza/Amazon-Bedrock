from summary import handler
import json

event = {"body": json.dumps(
    {
        "text": """
            Dear Friend,

            You asked for advice about your life path. I believe no one can give you a perfect answer, since everyone’s truth is different. We all have to choose whether to drift along or swim toward a goal. But goals themselves are tricky; they can change as we change.

            The most important thing is to find a way of life that suits who you are—one that allows your abilities and desires to flourish. Don’t shape yourself to fit someone else’s idea of success; instead, pursue what gives your life meaning.

            Each of us must create our own path. Decide how you want to live, and let your work fit that vision.

            Your friend,
            Hunter
            """
        }
    ),
    "queryStringParameters": {
        "points":"3"
    }
}

response = handler(event, {})

