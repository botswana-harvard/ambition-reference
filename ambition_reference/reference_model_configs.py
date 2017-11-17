from edc_reference import site_reference_configs
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

site_reference_configs.register_from_visit_schedule(
    site_visit_schedules=site_visit_schedules)

configs = {
    'ambition_subject.adverseevent': ['ae_severity_grade', 'ae_cm_recurrence'],
    'ambition_subject.bloodresult': ['abnormal_results_in_ae_range'],
    'ambition_subject.prnmodel': [
        'adverse_event', 'adverse_event_tmg', 'adverse_event_followup',
        'microbiology', 'radiology', 'protocol_deviation', 'blood_result',
        'lumbar_puncture', 'recurrence_symptom', 'death_report'],
    'ambition_subject.deathreport': ['cause_of_death'],
    'ambition_subject.deathreporttmg1': ['cause_of_death'],
    'ambition_subject.patienthistory': ['cd4_date', 'viral_load_date'],
    'ambition_subject.protocoldeviationviolation': ['deviation_or_violation'],
    'ambition_subject.medicalexpenses': ['care_before_hospital'],
    'ambition_subject.recurrencesymptom': ['patient_readmitted', 'lp_completed'],
    'ambition_subject.studyterminationconclusion': ['termination_reason'],
    'ambition_subject.week16': ['patient_alive'],
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)
