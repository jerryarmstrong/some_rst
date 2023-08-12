tests/ui/structs/multi-line-fru-suggestion.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Default)]
struct Inner {
    a: u8,
    b: u8,
}

#[derive(Default)]
struct Outer {
    inner: Inner,
    defaulted: u8,
}

fn main(){
    Outer {
        //~^ ERROR missing field `defaulted` in initializer of `Outer`
        inner: Inner {
            a: 1,
            b: 2,
        }
        ..Default::default()
    };
}


