import os

import gmail
from pytest import fixture

email = os.environ["GMAIL_ADDR"]
password = os.environ["GMAIL_PASSWORD"]
to = os.environ["GMAIL_TO"]


@fixture
def gmail_client():
    gm = gmail.Gmail()
    gm.login(email, password)
    return gm


def test_smtp_login():
    gm = gmail.Gmail()
    gm._connect_smtp()
    gm.smtp.login(email, password)


def test_smtp_send_text_email(gmail_client):
    message = gmail.Message.create("Hello", to, text="Hello world")
    gmail_client.send(message)


def test_get_inbox_email(gmail_client):
    inbox = gmail_client.inbox()
    assert inbox is not None

    inbox_email = inbox.mail()


def test_get_all_email(gmail_client):
    all_mail_box = gmail_client.all_mail()
    assert all_mail_box is not None

    all_mail = all_mail_box.mail()


def test_that_emails_have_content(gmail_client):
    emails = gmail_client.inbox().mail()
    assert len(emails) > 0

    first_email = emails[0]
    assert first_email.subject is not None
    assert first_email.body is not None
