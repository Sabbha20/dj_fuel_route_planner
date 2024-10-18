from django.core.management.base import BaseCommand, CommandError
from api.models import FuelStop
import csv

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to CSV file")
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for i, row in enumerate(reader):
                    try:
                        FuelStop.objects.create(
                            opis_truckstop_id=row['OPIS Truckstop ID'],
                            truckstop_name=row['Truckstop Name'],
                            address=row['Address'],
                            city=row['City'],
                            state=row['State'],
                            rack_id=row['Rack ID'],
                            retail_price=float(row['Retail Price'])
                        )
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error on row {i+2}: {str(e)}"))
            self.stdout.write(self.style.SUCCESS("Data imported successfully!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error Occurred - Data not imported: {e}"))