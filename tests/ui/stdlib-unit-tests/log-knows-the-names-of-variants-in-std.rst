tests/ui/stdlib-unit-tests/log-knows-the-names-of-variants-in-std.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(non_camel_case_types)]
#![allow(dead_code)]
#[derive(Clone, Debug)]
enum foo {
  a(usize),
  b(String),
}

fn check_log<T: std::fmt::Debug>(exp: String, v: T) {
    assert_eq!(exp, format!("{:?}", v));
}

pub fn main() {
    let mut x = Some(foo::a(22));
    let exp = "Some(a(22))".to_string();
    let act = format!("{:?}", x);
    assert_eq!(act, exp);
    check_log(exp, x);

    x = None;
    let exp = "None".to_string();
    let act = format!("{:?}", x);
    assert_eq!(act, exp);
    check_log(exp, x);
}


