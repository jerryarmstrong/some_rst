tests/ui/rfc-2632-const-trait-impl/trait-where-clause-run.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(const_trait_impl)]

#[const_trait]
trait Bar {
    fn bar() -> u8;
}

#[const_trait]
trait Foo {
    fn foo() -> u8 where Self: ~const Bar {
        <Self as Bar>::bar() * 6
    }
}

struct NonConst;
struct Const;

impl Bar for NonConst {
    fn bar() -> u8 {
        3
    }
}

impl Foo for NonConst {}

impl const Bar for Const {
    fn bar() -> u8 {
        4
    }
}

impl const Foo for Const {}

fn main() {
    const ANS1: u8 = Const::foo();
    let ans2 = NonConst::foo();

    assert_eq!(ANS1 + ans2, 42);
}


