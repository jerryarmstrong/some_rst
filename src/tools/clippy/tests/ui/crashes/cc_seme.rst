src/tools/clippy/tests/ui/crashes/cc_seme.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(dead_code)]

/// Test for https://github.com/rust-lang/rust-clippy/issues/478

enum Baz {
    One,
    Two,
}

struct Test {
    t: Option<usize>,
    b: Baz,
}

fn main() {}

pub fn foo() {
    use Baz::*;
    let x = Test { t: Some(0), b: One };

    match x {
        Test { t: Some(_), b: One } => unreachable!(),
        Test { t: Some(42), b: Two } => unreachable!(),
        Test { t: None, .. } => unreachable!(),
        Test { .. } => unreachable!(),
    }
}


