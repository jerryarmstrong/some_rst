src/tools/clippy/tests/ui/cmp_owned/comparison_flip.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

use std::fmt::{self, Display};

fn main() {
    let a = Foo;

    if a.to_string() != "bar" {
        println!("foo");
    }

    if "bar" != a.to_string() {
        println!("foo");
    }
}

struct Foo;

impl Display for Foo {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "foo")
    }
}

impl PartialEq<&str> for Foo {
    fn eq(&self, other: &&str) -> bool {
        "foo" == *other
    }
}


