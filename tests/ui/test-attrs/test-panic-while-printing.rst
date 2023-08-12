tests/ui/test-attrs/test-panic-while-printing.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--test
// run-pass
// needs-unwind

use std::fmt;
use std::fmt::{Display, Formatter};

pub struct A(Vec<u32>);

impl Display for A {
    fn fmt(&self, _f: &mut Formatter<'_>) -> fmt::Result {
        self.0[0];
        Ok(())
    }
}

#[test]
fn main() {
    let result = std::panic::catch_unwind(|| {
        let a = A(vec![]);
        eprintln!("{}", a);
    });
    assert!(result.is_err());
}


