from django.http import HttpResponse
import csv


def export_messages_to_csv(queryset, file_name):
    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(file_name)
    
    writer = csv.writer(response)
    writer.writerow(['Title', 'Body', 'Sent', 'Read', 'Created at'])

    output = []
    for msg in queryset:
        output.append([msg.title, msg.body, msg.flag_sent, msg.flag_read, msg.created_at])

    writer.writerows(output)

    return response
