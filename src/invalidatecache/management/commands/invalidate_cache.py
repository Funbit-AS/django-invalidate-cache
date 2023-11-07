from django.core.management.base import BaseCommand, CommandError

from invalidatecache.utils import InvalidateTagError, invalidate_tag


class Command(BaseCommand):
    help = "Invalidate cache for a given tag"

    def add_arguments(self, parser):
        parser.add_argument("tag", type=str)

    def handle(self, tag: str, *args, **options):
        try:
            invalidate_tag(tag)
        except InvalidateTagError as e:
            raise CommandError(f"Error invalidating cache for tag {tag}") from e
        self.stdout.write(
            self.style.SUCCESS(f"Successfully invalidated cache for tag {tag}")
        )
