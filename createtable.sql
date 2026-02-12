-- Create the sample table

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
