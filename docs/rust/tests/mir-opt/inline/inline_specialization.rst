tests/mir-opt/inline/inline_specialization.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(specialization)]

// EMIT_MIR inline_specialization.main.Inline.diff
fn main() {
    let x = <Vec::<()> as Foo>::bar();
}

trait Foo {
    fn bar() -> u32;
}

impl<T> Foo for Vec<T> {
    #[inline(always)]
    default fn bar() -> u32 { 123 }
}


