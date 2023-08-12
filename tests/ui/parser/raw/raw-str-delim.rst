tests/ui/parser/raw/raw-str-delim.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static s: &'static str =
    r#~"#"~# //~ ERROR found invalid character; only `#` is allowed in raw string delimitation
;


