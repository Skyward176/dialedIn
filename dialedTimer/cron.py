def sendMail():
    send_mail(
        'Test_Email',
        'Test_Message',
        'contact@brandonmartinez.dev',
        ['contact@brandonmartinez.dev'],
        fail_silently=False,
    )
    print('e-mail sent')
