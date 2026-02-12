-- Create the sample table
DROP TABLE IF EXISTS GLOBALDATA_S;
CREATE TABLE GLOBALDATA_S(
    country TEXT,
    yr INTEGER,
    total_consumption FLOAT,
    per_capita FLOAT,
    agr_total FLOAT,
    ind_total FLOAT,
    hou_total FLOAT
);

DROP TABLE IF EXISTS AQTE;
CREATE TABLE AQTE(
    country TEXT,
    yr INTEGER,
    total_resources FLOAT,
);


CREATE TABLE AQUA1 (
    VariableGroup TEXT,
    Subgroup TEXT,
    Variable TEXT,
    Country TEXT,
    Year INTEGER,
    Value FLOAT,
    Unit TEXT
);

CREATE TABLE AQUA2 (
    VariableGroup TEXT,
    Subgroup TEXT,
    Variable TEXT,
    Country TEXT,
    Year INTEGER,
    Value FLOAT,
    Unit TEXT
);
    
CREATE TABLE AQUA_Resources (
    VariableGroup TEXT,
    Subgroup TEXT,
    Variable TEXT,
    Country TEXT,
    Year INTEGER,
    Value FLOAT,
    Unit TEXT
);
    
CREATE TABLE AQUA_Use (
    VariableGroup TEXT,
    Subgroup TEXT,
    Variable TEXT,
    Country TEXT,
    Year INTEGER,
    Value FLOAT,
    Unit TEXT
);

CREATE TABLE cleaned_gwc (
    Country TEXT,
    Year INTEGER,
    TotalConsumption FLOAT,
    PerCapita FLOAT,
    Agricultural FLOAT,
    Industrial FLOAT,
    Household FLOAT
);
