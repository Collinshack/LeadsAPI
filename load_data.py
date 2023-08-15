import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LeadsAPI.settings')
django.setup()

import pandas as pd
from api_app.models import YoutubeLead, RealEstateLead

# def load_youtube_leads_from_excel(file_path):
#     # Load Excel file into a DataFrame
#     df = pd.read_excel(file_path, sheet_name='Sheet1')

#     for index, row in df.iterrows():
#         defaults = {
#             'niche': row['NICHE/DOMAIN'],
#             'subscriber_range': row['SUB-SIZE'],
#             'country': row['COUNTRY']
#         }
#         lead, created = YoutubeLead.objects.update_or_create(
#             email=row['EMAILS'],
#             defaults=defaults
#         )

#         if created:
#             print(f"Lead with email '{lead.email}' created.")
#         else:
#             print(f"Lead with email '{lead.email}' updated.")

#     print(f"{len(df)} leads processed.")

# # Call the function with the Excel file path
# load_youtube_leads_from_excel(r'data\VarsityScape leads.xlsx')


def load_real_estate_leads_from_excel(file_path):
    # Load Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name='Sheet1')

    for index, row in df.iterrows():
        defaults = {
            'website': row['website'],
            'phone': row['phone'],
            'address': row['address']
        }
        lead, created = RealEstateLead.objects.update_or_create(
            business_name=row['business name'],
            defaults=defaults
        )

        if created:
            print(f"Lead with business name '{lead.business_name}' created.")
        else:
            print(f"Lead with business name '{lead.business_name}' updated.")

    print(f"{len(df)} leads processed.")

# Call the function with the Excel file path
load_real_estate_leads_from_excel(r'data\Real Estate Agents New  Y.xlsx')