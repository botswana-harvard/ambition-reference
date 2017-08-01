from edc_reference import site_reference_configs, ReferenceModelConfig
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

site_reference_configs.register_from_visit_schedule(
    site_visit_schedules=site_visit_schedules)

configs = {
    'ambition_subject.adverseevent': ['ae_severity_grade'],
    'ambition_subject.prnmodel': [
        'adverse_event', 'adverse_event_tmg', 'adverse_event_followup',
        'microbiology', 'radiology', 'protocol_deviation', 'blood_result',
        'lumbar_puncture', 'recurrence_symptom', 'death_report',
        'death_report_tmg1', 'death_report_tmg2'],
    'ambition_subject.clinicnote': ['report_datetime'],
    'ambition_subject.adverseeventfollowup': ['report_datetime'],
    'ambition_subject.adverseeventtmg': ['report_datetime'],
    'ambition_subject.bloodresult': ['report_datetime'],
    'ambition_subject.deathreport': ['report_datetime'],
    'ambition_subject.deathreporttmg1': ['report_datetime'],
    'ambition_subject.deathreporttmg2': ['report_datetime'],
    'ambition_subject.followup': ['report_datetime'],
    'ambition_subject.patienthistory': ['viral_load_date', 'cd4_date'],
    'ambition_subject.protocoldeviationviolation': ['report_datetime'],
    'ambition_subject.microbiology': ['report_datetime'],
    'ambition_subject.radiology': ['report_datetime'],
    'ambition_subject.lumbarpuncturecsf': ['report_datetime'],
    'ambition_subject.recurrencesymptom': ['report_datetime'],
    'ambition_subject.subjectrequisition': ['requisition_datetime'],
    'ambition_subject.week2': ['report_datetime'],
    'ambition_subject.week4': ['report_datetime'],
    'ambition_subject.week16': ['report_datetime'],
    'ambition_subject.studyterminationconclusion': [
        'report_datetime', 'termination_reason'],
}

for model, fields in configs.items():
    print('model:', model, 'fields', fields)
    site_reference_configs.add_fields_to_config(
        model, fields)
