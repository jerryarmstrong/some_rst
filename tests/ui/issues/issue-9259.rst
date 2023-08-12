tests/ui/issues/issue-9259.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

struct A<'a> {
    a: &'a [String],
    b: Option<&'a [String]>,
}

pub fn main() {
    let b: &[String] = &["foo".to_string()];
    let a = A {
        a: &["test".to_string()],
        b: Some(b),
    };
    assert_eq!(a.b.as_ref().unwrap()[0], "foo");
}


