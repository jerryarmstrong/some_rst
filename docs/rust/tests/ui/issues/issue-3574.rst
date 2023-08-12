tests/ui/issues/issue-3574.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// rustc --test match_borrowed_str.rs.rs && ./match_borrowed_str.rs


fn compare(x: &str, y: &str) -> bool {
    match x {
        "foo" => y == "foo",
        _ => y == "bar",
    }
}

pub fn main() {
    assert!(compare("foo", "foo"));
}


