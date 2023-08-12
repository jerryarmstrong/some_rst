tests/ui/consts/const-mut-refs/const_mut_address_of.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(const_mut_refs)]
#![feature(raw_ref_op)]

struct Foo {
    x: usize
}

const fn foo() -> Foo {
    Foo { x: 0 }
}

impl Foo {
    const fn bar(&mut self) -> *mut usize {
        &raw mut self.x
    }
}

const fn baz(foo: &mut Foo)-> *mut usize {
    &raw mut foo.x
}

const _: () = {
    foo().bar();
    baz(&mut foo());
};

fn main() {}


