from edc_reference import site_reference_configs
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

site_reference_configs.register_from_visit_schedule(
    site_visit_schedules=site_visit_schedules)

site_reference_configs.unregister('ambition_subject.enrollment')
site_reference_configs.unregister('ambition_subject.disenrollment')

configs = {
    'ambition_subject.adverseevent': ['ae_severity_grade'],
    'ambition_subject.prnmodel': [
        'adverse_event', 'adverse_event_tmg', 'adverse_event_followup',
        'microbiology', 'radiology', 'protocol_deviation', 'blood_result',
        'lumbar_puncture', 'recurrence_symptom', 'death_report',
        'death_report_tmg1', 'death_report_tmg2'],
    'ambition_subject.patienthistory': ['cd4_date', 'viral_load_date'],
    'ambition_subject.protocoldeviationviolation': ['deviation_or_violation'],
    'ambition_subject.studyterminationconclusion': ['termination_reason'],
}

for model, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        model, fields)
