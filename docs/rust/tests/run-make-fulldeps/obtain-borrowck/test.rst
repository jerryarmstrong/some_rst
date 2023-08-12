tests/run-make-fulldeps/obtain-borrowck/test.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X {
    fn provided(&self) -> usize {
        5
    }
    fn required(&self) -> u32;
}

struct Bar;

impl Bar {
    fn new() -> Self {
        Self
    }
}

impl X for Bar {
    fn provided(&self) -> usize {
        1
    }
    fn required(&self) -> u32 {
        7
    }
}

const fn foo() -> usize {
    1
}

fn main() {
    let bar: [Bar; foo()] = [Bar::new()];
    assert_eq!(bar[0].provided(), foo());
}


