tests/ui/pattern/issue-68393-let-pat-assoc-constant.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum EFoo {
    A,
}

pub trait Foo {
    const X: EFoo;
}

struct Abc;

impl Foo for Abc {
    const X: EFoo = EFoo::A;
}

struct Def;
impl Foo for Def {
    const X: EFoo = EFoo::A;
}

pub fn test<A: Foo, B: Foo>(arg: EFoo, A::X: EFoo) {
    //~^ ERROR associated consts cannot be referenced in patterns
    let A::X = arg;
    //~^ ERROR associated consts cannot be referenced in patterns
}

fn main() {}


