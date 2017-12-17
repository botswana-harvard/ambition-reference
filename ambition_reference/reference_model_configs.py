from edc_reference import site_reference_configs
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

site_reference_configs.register_from_visit_schedule(
    site_visit_schedules=site_visit_schedules)

configs = {
    'ambition_subject.prnmodel': [
        'blood_result', 'microbiology', 'radiology', 'lumbar_puncture',
        'cd4', 'viral_load', 'fbc', 'chemistry'],
    'ambition_subject.education': ['household_head'],
    'ambition_subject.patienthistory': ['cd4_date', 'viral_load_date'],
    'ambition_subject.medicalexpenses': ['care_before_hospital'],
    'ambition_subject.week16': ['patient_alive'],
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)
