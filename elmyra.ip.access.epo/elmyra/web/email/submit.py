# -*- coding: utf-8 -*-
# (c) 2016-2017 Andreas Motl, Elmyra UG <andreas.motl@elmyra.de>
import logging
from email.utils import formataddr
from validate_email import validate_email
from pyramid.threadlocal import get_current_request
from elmyra.ip.util.config import read_config, read_list, to_list
from elmyra.ip.util.data.container import SmartBunch
from elmyra.ip.util.email.message import EmailMessage

log = logging.getLogger(__name__)


def message_factory(**kwargs):

    request = get_current_request()
    application_settings = request.registry.application_settings

    # EmailMessage builder
    message = EmailMessage(application_settings['smtp'], application_settings['email'])

    if 'reply' in application_settings['email']:
        message.add_reply(read_list(application_settings['email']['reply']))

    is_support_email = False
    if 'recipients' in kwargs:
        for recipient in kwargs['recipients']:
            if recipient == 'support':
                is_support_email = True
            if recipient in application_settings['email-recipients']:
                message.add_recipient(read_list(application_settings['email-recipients'][recipient]))
            else:
                log.warning('Could not add recipient {}'.format(recipient))

    # Extend "To" and "Reply-To" addresses by email address of user
    #request.user.username = 'test@example.org'; request.user.fullname = 'Hello World'   # debugging
    if request.user.username:
        username = request.user.username
        if validate_email(username):
            if request.user.fullname:
                pair = (request.user.fullname, username)
            else:
                pair = (None, username)

            try:
                user_email = formataddr(pair)
            except Exception as ex:
                log.warning('Computing "user_email" failed: Could not decode email address from "{}": {}'.format(username, ex))
                return message

            # Add user email as "Reply-To" address
            message.add_reply(user_email)

            # If it's a support email, also add user as recipient
            if is_support_email:
                message.add_recipient(user_email)

        else:
            log.warning('Computing "user_email" failed: Email address "{}" is invalid'.format(username))

    return message


def email_issue_report(report, recipients):

    recipients = to_list(recipients)

    identifier = None
    if isinstance(report, SmartBunch):
        identifier = report.meta.id

    # Build reasonable subject
    subject = u'Product issue'
    if 'dialog' in report and 'what' in report.dialog:
        subject = u'[{}] '.format(report.dialog.what) + subject
    if identifier:
        subject += u' #' + identifier

    # Build reasonable message
    message = u''
    if 'dialog' in report and 'remark' in report.dialog:
        message = report.dialog.remark

    # Add JSON report as attachment
    files = {u'report.json': report.pretty()}

    email = message_factory(recipients=recipients)
    email.send(
        subject     = subject,
        message     = message,
        files       = files
    )

