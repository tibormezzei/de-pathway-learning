-- Session 11 reference: physical model (DuckDB dialect) for the survey field operation.
-- 3NF: every non-key column depends on the key, the whole key, and nothing but the key.

CREATE TABLE region (
    region_code   VARCHAR PRIMARY KEY,
    region_name   VARCHAR NOT NULL
);

CREATE TABLE survey (
    survey_code   VARCHAR PRIMARY KEY,
    survey_name   VARCHAR NOT NULL
);

CREATE TABLE outcome (
    outcome_code         VARCHAR PRIMARY KEY,
    outcome_description  VARCHAR NOT NULL
);

CREATE TABLE interviewer (
    interviewer_id   VARCHAR PRIMARY KEY,
    interviewer_name VARCHAR NOT NULL,
    region_code      VARCHAR NOT NULL REFERENCES region (region_code)
);

CREATE TABLE address (
    address_id    INTEGER PRIMARY KEY,          -- surrogate key: no reliable natural key
    address_line  VARCHAR NOT NULL,
    postcode      VARCHAR NOT NULL,
    region_code   VARCHAR NOT NULL REFERENCES region (region_code),
    UNIQUE (address_line, postcode)
);

CREATE TABLE survey_case (                      -- "case" is a reserved word in SQL
    case_id         VARCHAR PRIMARY KEY,
    survey_code     VARCHAR NOT NULL REFERENCES survey (survey_code),
    period          VARCHAR NOT NULL,           -- yyyy-mm
    address_id      INTEGER NOT NULL REFERENCES address (address_id),
    interviewer_id  VARCHAR NOT NULL REFERENCES interviewer (interviewer_id)
);

CREATE TABLE visit (
    case_id       VARCHAR NOT NULL REFERENCES survey_case (case_id),
    visit_no      INTEGER NOT NULL,
    visit_date    DATE    NOT NULL,
    outcome_code  VARCHAR NOT NULL REFERENCES outcome (outcome_code),
    PRIMARY KEY (case_id, visit_no)             -- composite key: a visit only exists within a case
);
