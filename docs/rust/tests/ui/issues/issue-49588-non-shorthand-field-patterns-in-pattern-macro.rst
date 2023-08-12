tests/ui/issues/issue-49588-non-shorthand-field-patterns-in-pattern-macro.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
#![deny(non_shorthand_field_patterns)]

pub struct Value<A> { pub value: A }

#[macro_export]
macro_rules! pat {
    ($a:pat) => {
        Value { value: $a }
    };
}

fn main() {
    let pat!(value) = Value { value: () };
}


