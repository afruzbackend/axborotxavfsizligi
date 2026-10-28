"""Asosiy darslikning «Materiallar» bo'limini to'ldiradi (ro'yxat: lectures/fan.py, MATERIALS).

    python manage.py materiallar

Qonunlar va rasmiy saytlarga havolalar hamda to'liq ma'ruzalar matni (data/maruza.docx) qo'shiladi.
Avval qo'shilganlari takrorlanmaydi; o'qituvchi Studiyada qo'shgan materiallarga tegilmaydi.
"""
from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from lectures import fan
from lectures.models import Course, Resource

DOCX_TITLE = 'To‘liq ma’ruzalar matni (Word)'


class Command(BaseCommand):
    help = "Darslikka qonunlar, rasmiy saytlar va ma'ruzalar faylini qo'shadi (lectures/fan.py)."

    def handle(self, *args, **opts):
        course = Course.objects.get(slug=fan.SLUG)
        added = 0
        for title, url, note, n in getattr(fan, 'MATERIALS', []):
            if Resource.objects.filter(course=course, kind='material', url=url).exists():
                continue
            topic = course.topics.filter(number=n).first() if n else None
            Resource.objects.create(course=course, topic=topic, kind='material', title=title, url=url, note=note)
            added += 1
        if not Resource.objects.filter(course=course, kind='material', title=DOCX_TITLE).exists():
            with open(settings.LECTURE_DOCX, 'rb') as fh:
                res = Resource(course=course, kind='material', title=DOCX_TITLE,
                               note='Barcha mavzular: o‘quv texnologiyasi, ma’ruza matni, savollar va testlar · chop etish uchun')
                res.file.save(f'{fan.SLUG}-maruzalar.docx', File(fh), save=True)
            added += 1
        total = Resource.objects.filter(course=course, kind='material').count()
        self.stdout.write(self.style.SUCCESS(f'Materiallar: {added} ta qo‘shildi, jami {total} ta.'))
