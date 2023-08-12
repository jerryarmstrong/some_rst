tests/ui/consts/const-fn-method.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Foo { value: u32 }

impl Foo {
    const fn new() -> Foo {
        Foo { value: 22 }
    }
}

const FOO: Foo = Foo::new();

pub fn main() {
    assert_eq!(FOO.value, 22);
    let _: [&'static str; Foo::new().value as usize] = ["hey"; 22];
}


