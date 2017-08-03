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
    'ambition_subject.clinicnote': ['vital_signs'],
    'ambition_subject.adverseeventfollowup': ['outcome'],
    'ambition_subject.adverseeventtmg': ['ae_received_datetime'],
    'ambition_subject.bloodresult': ['wbc'],
    'ambition_subject.deathreport': ['death_datetime'],
    'ambition_subject.deathreporttmg1': ['cause_of_death_tmg1_opinion'],
    'ambition_subject.deathreporttmg2': ['cause_of_death_tmg2_opinion'],
    'ambition_subject.followup': ['fluconazole_dose'],
    'ambition_subject.patienthistory': ['viral_load_date', 'cd4_date'],
    'ambition_subject.protocoldeviationviolation': ['deviation_or_violation'],
    'ambition_subject.microbiology': ['urine_culture_performed'],
    'ambition_subject.radiology': ['is_cxr_done'],
    'ambition_subject.lumbarpuncturecsf': ['reason_for_lp'],
    'ambition_subject.recurrencesymptom': ['meningitis_symptom'],
    'ambition_subject.subjectconsent': ['version'],
    'ambition_subject.subjectrequisition': ['requisition_datetime'],
    'ambition_subject.week2': ['discharged'],
    'ambition_subject.week4': ['fluconazole_dose'],
    'ambition_subject.week16': ['patient_alive'],
    'ambition_subject.studyterminationconclusion': [
        'report_datetime', 'termination_reason'],
    'ambition_subject.subjectvisit': ['reason_unscheduled'],
}

for model, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        model, fields)
