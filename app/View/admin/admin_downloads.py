
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Participant, Tournament
import csv
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import io


def downloads_home(request):
    context = {
        'active_tab': "admin_downloads",
        'tournaments': Tournament.objects.all(),
        'status_choices': Participant.STATUS_CHOICES,
    }
    return render(request, 'admin/downloads.html',context)

@login_required
def export_participants_csv(request):
    # Accept POSTed filters
    tournament_id = request.POST.get('tournament_id', 'all')
    status = request.POST.get('status', 'all')
    download_type = request.POST.get('download_type', 'csv')

    participants = Participant.objects.select_related('tournament').all()
    if tournament_id and tournament_id != 'all':
        participants = participants.filter(tournament_id=tournament_id)
    if status and status != 'all':
        participants = participants.filter(status=status)

    headers = [
        'Full Name','Phone', 'WhatsApp','Status', 'Tournament', 'Registration Date'
    ]
    rows = [
        [
            p.full_name,
            p.phone,
            p.wp,
            p.status,
            p.tournament.title if p.tournament else '',
            p.registration_date.strftime('%Y-%m-%d %H:%M:%S') if p.registration_date else '',
        ] for p in participants
    ]

    if download_type == 'excel':
        try:
            import openpyxl
            from openpyxl.utils import get_column_letter
        except ImportError:
            return HttpResponse('openpyxl is required for Excel export.', status=500)
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(headers)
        for row in rows:
            ws.append(row)
        # Auto-width columns
        for col in ws.columns:
            max_length = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            ws.column_dimensions[col_letter].width = max_length + 2
        output = io.BytesIO()
        wb.save(output)
        output.seek(0)
        response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="participants.xlsx"'
        return response
    elif download_type == 'pdf':
        try:
            from reportlab.lib.pagesizes import letter, landscape
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
            from reportlab.lib import colors
            from reportlab.lib.styles import getSampleStyleSheet
        except ImportError:
            return HttpResponse('reportlab is required for PDF export.', status=500)
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=landscape(letter), leftMargin=30, rightMargin=30, topMargin=30, bottomMargin=30)
        data = [headers] + rows
        table = Table(data, repeatRows=1)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#00838f')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,0), 9),
            ('FONTSIZE', (0,1), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,0), 8),
            ('TOPPADDING', (0,0), (-1,0), 8),
            ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ]))
        elements = []
        styles = getSampleStyleSheet()
        elements.append(Paragraph('Participants Record', styles['Title']))
        elements.append(Spacer(1, 12))
        elements.append(table)
        doc.build(elements)
        pdf = buffer.getvalue()
        buffer.close()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="participants.pdf"'
        return response
    else:  # CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="participants.csv"'
        writer = csv.writer(response)
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)
        return response