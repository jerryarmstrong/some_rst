src/std/src/sys/windows/path/tests.rs
=====================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use super::*;

#[test]
fn test_parse_next_component() {
    assert_eq!(
        parse_next_component(OsStr::new(r"server\share"), true),
        (OsStr::new(r"server"), OsStr::new(r"share"))
    );

    assert_eq!(
        parse_next_component(OsStr::new(r"server/share"), true),
        (OsStr::new(r"server/share"), OsStr::new(r""))
    );

    assert_eq!(
        parse_next_component(OsStr::new(r"server/share"), false),
        (OsStr::new(r"server"), OsStr::new(r"share"))
    );

    assert_eq!(
        parse_next_component(OsStr::new(r"server\"), false),
        (OsStr::new(r"server"), OsStr::new(r""))
    );

    assert_eq!(
        parse_next_component(OsStr::new(r"\server\"), false),
        (OsStr::new(r""), OsStr::new(r"server\"))
    );

    assert_eq!(
        parse_next_component(OsStr::new(r"servershare"), false),
        (OsStr::new(r"servershare"), OsStr::new(""))
    );

    assert_eq!(
        parse_next_component(OsStr::new(r"server/\//\/\\\\/////\/share"), false),
        (OsStr::new(r"server"), OsStr::new(r"share"))
    );

    assert_eq!(
        parse_next_component(OsStr::new(r"server\\\\\\\\\\\\\\share"), true),
        (OsStr::new(r"server"), OsStr::new(r"\\\\\\\\\\\\\share"))
    );
}


