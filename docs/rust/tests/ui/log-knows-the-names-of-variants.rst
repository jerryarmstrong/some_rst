tests/ui/log-knows-the-names-of-variants.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(non_camel_case_types)]
#![allow(dead_code)]
#[derive(Debug)]
enum foo {
  a(usize),
  b(String),
  c,
}

#[derive(Debug)]
enum bar {
  d, e, f
}

pub fn main() {
    assert_eq!("a(22)".to_string(), format!("{:?}", foo::a(22)));
    assert_eq!("c".to_string(), format!("{:?}", foo::c));
    assert_eq!("d".to_string(), format!("{:?}", bar::d));
}


