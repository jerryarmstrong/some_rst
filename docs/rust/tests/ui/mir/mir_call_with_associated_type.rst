tests/ui/mir/mir_call_with_associated_type.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
trait Trait {
    type Type;
}

impl<'a> Trait for &'a () {
    type Type = u32;
}

fn foo<'a>(t: <&'a () as Trait>::Type) -> <&'a () as Trait>::Type {
    t
}

fn main() {
    assert_eq!(foo(4), 4);
}


