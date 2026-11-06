---
status: new
---

# Healthcare

!!! success "General patterns"

    - Use the names of HL7 FHIR for the clinical entities: `Patient`, `Encounter`, `Observation`, `Condition`, `MedicationRequest`
    - Keep the request, the event and the result as separate entities: `MedicationRequest`, `MedicationAdministration`, `Observation`
    - Store a coded value as a system, a code and a display text: `code_system`, `code`, `display`
    - Give each resource that has a status the FHIR value set, and a way to mark a wrong entry: `entered_in_error`
    - Keep the clinical time and the record time apart: `effective_at`, `recorded_at`

!!! tip "Useful tips"

    - Use `patient_id` in every table that holds clinical data. Do not use a name or a birth date as a key
    - Use a full coding system for a code: LOINC for tests, SNOMED CT for findings, ICD-10 for diagnoses, RxNorm for drugs
    - Write units with UCUM codes: `mg`, `mmol/L`, `mm[Hg]`
    - Treat the name and the identifiers of a patient as personal data. Keep real values out of the names of tables, columns, indexes and constraints, out of logs and out of URLs

!!! danger "General anti-patterns"

    - `patient_name` as an identifier
    - `diagnosis` as free text with no code
    - `visit` for an appointment, an encounter and an admission at once
    - `result` for the test, the value and the report
    - Deleting a wrong record. Mark it `entered_in_error`

The names follow the HL7 FHIR resources (release R4 and R5). FHIR resource names are `UpperCamelCase`. In a JSON message the field names are `lowerCamelCase`, for example `birthDate`. This page uses `snake_case` for database columns, as in [Columns](../databases/columns.md). Map the names in one place.

## Entities

| Entity | Meaning | Table | Notes |
|---|---|---|---|
| Patient | A person who receives care. | `patients` | FHIR `Patient`. |
| Practitioner | A person who gives care. | `practitioners` | FHIR `Practitioner`. |
| Practitioner role | The role of a practitioner at an organization. | `practitioner_roles` | FHIR `PractitionerRole`. |
| Organization | A hospital, clinic or lab. | `organizations` | FHIR `Organization`. |
| Location | A place where care happens. | `locations` | A ward, a room, a bed. |
| Appointment | A booked time for a meeting. | `appointments` | Before the encounter. |
| Encounter | An interaction between a patient and a provider. | `encounters` | The care event as it happens. |
| Episode of care | A group of encounters for one problem. | `episodes_of_care` | |
| Observation | A measure or a finding. | `observations` | Blood pressure, lab value. |
| Condition | A problem or a diagnosis. | `conditions` | |
| Procedure | An action that was done to a patient. | `procedures` | |
| Diagnostic report | The report of a test or an image. | `diagnostic_reports` | Holds many observations. |
| Service request | An order for a test or a service. | `service_requests` | |
| Medication request | An order for a drug. | `medication_requests` | FHIR `MedicationRequest`. |
| Medication dispense | The hand-over of a drug to a patient. | `medication_dispenses` | FHIR `MedicationDispense`. |
| Medication administration | A record that a drug was given. | `medication_administrations` | |
| Medication | A drug as a product. | `medications` | |
| Allergy intolerance | A risk of a reaction to a substance. | `allergy_intolerances` | |
| Immunization | A record of a vaccine that was given. | `immunizations` | |
| Care plan | A plan of care for a patient. | `care_plans` | |
| Coverage | The insurance of a patient. | `coverages` | |
| Claim | A request to an insurer for payment. | `claims` | |
| Document reference | A pointer to a clinical document. | `document_references` | |
| Consent | The permission of a patient to use data. | `consents` | |
| Specimen | A sample that was taken from a patient. | `specimens` | |

## States

| Entity | FHIR values | Column values in `snake_case` |
|---|---|---|
| Appointment | `proposed`, `pending`, `booked`, `arrived`, `fulfilled`, `cancelled`, `noshow`, `entered-in-error`, `checked-in`, `waitlist` | `proposed`, `pending`, `booked`, `arrived`, `fulfilled`, `cancelled`, `noshow`, `entered_in_error`, `checked_in`, `waitlist` |
| Encounter (R4) | `planned`, `arrived`, `triaged`, `in-progress`, `onleave`, `finished`, `cancelled`, `entered-in-error`, `unknown` | `planned`, `arrived`, `triaged`, `in_progress`, `onleave`, `finished`, `cancelled`, `entered_in_error`, `unknown` |
| Encounter (R5) | `planned`, `in-progress`, `on-hold`, `discharged`, `completed`, `cancelled`, `discontinued`, `entered-in-error`, `unknown` | `planned`, `in_progress`, `on_hold`, `discharged`, `completed`, `cancelled`, `discontinued`, `entered_in_error`, `unknown` |
| Observation | `registered`, `preliminary`, `final`, `amended`, `corrected`, `cancelled`, `entered-in-error`, `unknown` | `registered`, `preliminary`, `final`, `amended`, `corrected`, `cancelled`, `entered_in_error`, `unknown` |
| Medication request | `active`, `on-hold`, `ended` (R5 only), `stopped`, `completed`, `cancelled`, `entered-in-error`, `draft`, `unknown` | `active`, `on_hold`, `ended`, `stopped`, `completed`, `cancelled`, `entered_in_error`, `draft`, `unknown` |

A condition has two fields. `clinical_status`: `active`, `recurrence`, `relapse`, `inactive`, `remission`, `resolved`. `verification_status`: `unconfirmed`, `provisional`, `differential`, `confirmed`, `refuted`, `entered_in_error`.

FHIR spells `cancelled` with two `l`. This is the opposite of the e-commerce page, which uses `canceled`. In a healthcare system, keep the FHIR spelling in the values of FHIR fields.

## Actions

| Action | Function name | Meaning | Trap |
|---|---|---|---|
| Register a patient | `register_patient` | Creates a patient record. | Check for a duplicate first. |
| Book an appointment | `book_appointment` | Reserves a time slot. | |
| Check in | `check_in_patient` | Completes the check-in (`checked_in`). | The arrival is the state `arrived`. |
| Start an encounter | `start_encounter` | Opens the visit. | |
| Discharge | `discharge_patient` | Ends an inpatient stay. | R4 ends with `finished`. R5 ends with `discharged` or `completed`. |
| Record an observation | `record_observation` | Stores a measure. | |
| Amend an observation | `amend_observation` | Changes a final result with a new version. | Never overwrite. |
| Record a condition | `record_condition` | Adds a problem. | |
| Resolve a condition | `resolve_condition` | Sets the clinical status to resolved. | Not a delete. |
| Order a medication | `request_medication` | Creates a medication request. | An order is not an administration. |
| Administer a medication | `administer_medication` | Records that the drug was given. | |
| Order a test | `request_service` | Creates a service request. | |
| Issue a report | `issue_diagnostic_report` | Publishes the results. | |
| Mark as error | `mark_observation_entered_in_error` | Flags a record as wrong. | Do not delete. The same pattern holds for other resources. |
| Submit a claim | `submit_claim` | Sends the bill to an insurer. | |
| Record consent | `record_consent` | Stores a permission or a refusal. | |

## Traps

| Trap | Why it is a problem | Better |
|---|---|---|
| `visit` | An appointment, an encounter and an admission differ. | `appointment` before, `encounter` during. An inpatient stay is an encounter of class `IMP`. |
| `diagnosis` | A condition has a code, a status and a verification. | `condition` with `code`, `clinical_status`, `verification_status`. |
| `result` | A test, a value and a report are different. | `observation` for a value, `diagnostic_report` for the report. |
| `order` | A request for a drug, a test or a procedure. | `medication_request`, `service_request`. |
| `prescription` | A request, a dispense and an administration are different. | `medication_request`, `medication_dispense`, `medication_administration`. |
| `status` | An encounter, a request and a condition have different value sets. | `encounter_status`, `clinical_status`, `verification_status` in code and DTOs. Inside a table the column is `status`. |
| `patient_name` as a key | Names change and repeat. | `patient_id` and a separate identifier with its `system` and `value`. |
| `date` | Birth, onset, recording or effective date? | `birth_date`, `onset_at`, `recorded_at`, `effective_at`. |
| `value` | A number, a text or a code? | `value_quantity`, `value_string`, `value_codeable_concept`. |
| `code` | From which system? | `code_system` and `code`. |
| `unit` | A free text or a UCUM code? | `unit_code` with UCUM. |
| `gender` and `sex` | Administrative gender, sex at birth and gender identity differ. | `administrative_gender`, `birth_sex`. |
| `delete_record` | A clinical record must not be deleted without a trace. | `mark_observation_entered_in_error`. |
| `cancelled` and `canceled` | Two spellings in one code base make queries and checks miss rows. | `cancelled` in FHIR-mapped fields. `canceled` elsewhere (as in e-commerce and Stripe). Map at the boundary. |

## Worked example

```sql
CREATE TABLE patients (
    id                      bigint GENERATED ALWAYS AS IDENTITY,
    birth_date              date,
    administrative_gender   text,
    is_deceased             boolean NOT NULL DEFAULT false,
    created_at              timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_patients PRIMARY KEY (id)
);

CREATE TABLE patient_identifiers (
    patient_id          bigint NOT NULL,
    system              text NOT NULL,
    value               text NOT NULL,
    CONSTRAINT pk_patient_identifiers PRIMARY KEY (system, value),
    CONSTRAINT fk_patient_identifiers_patients FOREIGN KEY (patient_id) REFERENCES patients (id)
);

CREATE INDEX idx_patient_identifiers_patient_id ON patient_identifiers (patient_id);

CREATE TABLE observations (
    id                  bigint GENERATED ALWAYS AS IDENTITY,
    patient_id          bigint NOT NULL,
    encounter_id        bigint,
    status              text NOT NULL,
    code_system         text NOT NULL,
    code                text NOT NULL,
    value_quantity      numeric,
    unit_code           text,
    effective_at        timestamptz NOT NULL,
    recorded_at         timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_observations PRIMARY KEY (id),
    CONSTRAINT fk_observations_patients FOREIGN KEY (patient_id) REFERENCES patients (id),
    CONSTRAINT fk_observations_encounters FOREIGN KEY (encounter_id) REFERENCES encounters (id),
    CONSTRAINT chk_observations_status_allowed CHECK (status IN (
        'registered', 'preliminary', 'final', 'amended', 'corrected',
        'cancelled', 'entered_in_error', 'unknown'
    ))
);

CREATE INDEX idx_observations_patient_id_effective_at ON observations (patient_id, effective_at);
CREATE INDEX idx_observations_encounter_id ON observations (encounter_id);
```

The REST paths of FHIR use the resource name in `UpperCamelCase`. This is a rule of the FHIR standard and it differs from the paths in [REST](../systems/rest.md):

```
GET   /Patient/{id}
GET   /Observation?patient={id}&code=http://loinc.org|8480-6
POST  /MedicationRequest
```

The table `encounters` in the SQL is not shown. A search URL can hold a patient id. Keep such URLs out of logs, and use `POST /Observation/_search` for sensitive queries.

```py
def mark_observation_entered_in_error(observation: Observation, practitioner_id: int) -> Observation:
    if observation.observation_status == "entered_in_error":
        return observation
    return observation.with_status("entered_in_error", changed_by=practitioner_id)
```

## Related patterns

- [Negation and optionality](../patterns/negation-and-optionality.md) for `NULL` as missing, not yet and not applicable
- [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md) for units and the two clock times

!!! info "See also"

    - [Examples overview](index.md), [Tables](../databases/tables.md), [Columns](../databases/columns.md) and [Abbreviations](../common/abbreviations.md)
    - [HL7 FHIR](https://hl7.org/fhir/), [LOINC](https://loinc.org/), [SNOMED CT](https://www.snomed.org/), [UCUM](https://ucum.org/)
