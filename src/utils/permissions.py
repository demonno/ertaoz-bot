from functools import wraps


def group_required(func):
    """Make sure that handler is used in group"""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        chat_id = update.message.chat_id

        if chat_id > 0:
            context.bot.sendMessage(chat_id=chat_id, text="ჯერ ჯგუფში დამამატე!")
            return False
        return func(update, context, *args, **kwargs)

    return command_func


def admin_required(*args, **kwargs):

    func = None
    if len(args) == 1:
        func = args[0]

    if not func:
        db = kwargs.get("db")

    def callable(func):
        @wraps(func)
        def wrapped(update, context, *args, **kwargs):
            chat_id = update.message.chat_id
            chat_str = str(chat_id)
            if db.get(chat_str + "_adm") != update.message.from_user.id:
                context.bot.sendMessage(
                    chat_id=chat_id,
                    text="ამ სურვილს მხოლოდ იმას შევუსრულებ ვინც ჯგუფში მომიწვია!",
                )
                return False

            return func(update, context, *args, **kwargs)

        return wrapped

    return callable(func) if func else callable
