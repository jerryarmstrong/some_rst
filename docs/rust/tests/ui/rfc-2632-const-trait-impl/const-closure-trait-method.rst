tests/ui/rfc-2632-const-trait-impl/const-closure-trait-method.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(const_trait_impl)]

#[const_trait]
trait Tr {
    fn a(self) -> i32;
}

impl const Tr for () {
    fn a(self) -> i32 { 42 }
}

const fn need_const_closure<T: ~const FnOnce(()) -> i32>(x: T) -> i32 {
    x(())
}

const _: () = assert!(need_const_closure(Tr::a) == 42);

fn main() {}


