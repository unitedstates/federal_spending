CREATE OR REPLACE FUNCTION usaspending_contract_insert_child()
RETURNS TRIGGER AS $$
DECLARE tablename TEXT;
BEGIN
    tablename := 'usaspending_contract_' || trim(to_char(NEW.fiscal_year, '9999'));
    EXECUTE 'INSERT INTO ' || tablename || ' VALUES (($1).*);' USING NEW;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract'
    AND trigger_name = 'before_insert_usaspending_contract_trigger'
) THEN
    CREATE TRIGGER before_insert_usaspending_contract_trigger
        BEFORE INSERT ON usaspending_contract
        FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_insert_child();
END IF;
END $$;

-- The above will duplicate insert into the master table, so we delete it
CREATE OR REPLACE FUNCTION usaspending_contract_delete_master()
RETURNS TRIGGER AS $$
    BEGIN
        DELETE FROM ONLY usaspending_contract WHERE id = NEW.id;
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

DO $$
BEGIN
IF NOT EXISTS(
    SELECT 1 
    FROM information_schema.triggers
    WHERE event_object_table = 'usaspending_contract'
    AND trigger_name = 'after_insert_usaspending_contract_trigger'
)THEN
    CREATE TRIGGER after_insert_usaspending_contract_trigger
        AFTER INSERT ON usaspending_contract
        FOR EACH ROW EXECUTE PROCEDURE usaspending_contract_delete_master();
END IF;
END $$;


