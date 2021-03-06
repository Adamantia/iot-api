from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


def send_mail_to_contact(email_address, context={}):
    to = [email_address, ]

    subject = 'Requested use for IoT device reference {}'.format(context['device_reference'])
    txt_message = get_template('email/contact_iot_owner.txt').render(context)

    return send_mail(
        subject=subject,
        message=txt_message,
        from_email=settings.NOREPLY,
        recipient_list=to,
        fail_silently=False
    )


def send_confirmation_mail(to, context={}):
    subject = 'Confirmation about request to use IoT device reference {}'\
        .format(context['device_reference'])
    txt_message = get_template('email/confirm_iot_request.txt').render(context)

    return send_mail(
        subject=subject,
        message=txt_message,
        from_email=settings.NOREPLY,
        recipient_list=to,
        fail_silently=False
    )


def send_csv_import_report(to, filename, imported, errors):
    context = {
        'imported': imported,
        'errors': errors,
    }

    subject = 'CSV Import rapportage voor bestand {}'.format(filename)
    txt_message = get_template('email/import_csv_report.txt').render(context)

    return send_mail(
        subject=subject,
        message=txt_message,
        from_email=settings.NOREPLY,
        recipient_list=to,
        fail_silently=False
    )
