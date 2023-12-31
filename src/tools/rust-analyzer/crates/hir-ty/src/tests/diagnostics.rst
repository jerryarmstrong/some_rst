src/tools/rust-analyzer/crates/hir-ty/src/tests/diagnostics.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::check;

#[test]
fn function_return_type_mismatch_1() {
    check(
        r#"
fn test() -> &'static str {
    5
  //^ expected &str, got i32
}
"#,
    );
}

#[test]
fn function_return_type_mismatch_2() {
    check(
        r#"
fn test(x: bool) -> &'static str {
    if x {
        return 1;
             //^ expected &str, got i32
    }
    "ok"
}
"#,
    );
}

#[test]
fn function_return_type_mismatch_3() {
    check(
        r#"
fn test(x: bool) -> &'static str {
    if x {
        return "ok";
    }
    1
  //^ expected &str, got i32
}
"#,
    );
}

#[test]
fn function_return_type_mismatch_4() {
    check(
        r#"
fn test(x: bool) -> &'static str {
    if x {
        "ok"
    } else {
        1
      //^ expected &str, got i32
    }
}
"#,
    );
}

#[test]
fn function_return_type_mismatch_5() {
    check(
        r#"
fn test(x: bool) -> &'static str {
    if x {
        1
      //^ expected &str, got i32
    } else {
        "ok"
    }
}
"#,
    );
}


