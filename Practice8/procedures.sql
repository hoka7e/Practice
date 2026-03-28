-- 1.
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE first_name = p_name;
    ELSE
        INSERT INTO phonebook(first_name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

-- 2. 
CREATE OR REPLACE PROCEDURE bulk_upsert_contacts(
    p_names TEXT[], 
    p_phones TEXT[], 
    OUT invalid_entries TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    bad_data TEXT[];
BEGIN
    bad_data := ARRAY[]::TEXT[];

    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] ~ '^\d{7,15}$' THEN
            PERFORM upsert_contact(p_names[i], p_phones[i]);
        ELSE
            bad_data := array_append(bad_data, p_names[i] || ':' || p_phones[i]);
        END IF;
    END LOOP;

    invalid_entries := bad_data;
END;
$$;

-- 3. 
CREATE OR REPLACE PROCEDURE delete_contact(p_name VARCHAR DEFAULT NULL, p_phone VARCHAR DEFAULT NULL)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE first_name = p_name;
    END IF;

    IF p_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = p_phone;
    END IF;
END;
$$;