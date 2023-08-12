tests/ui/rfcs/rfc-2005-default-binding-mode/ref-region.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn foo<'a, 'b>(x: &'a &'b Option<u32>) -> &'a u32 {
    let x: &'a &'a Option<u32> = x;
    match x {
        Some(r) => {
            let _: &u32 = r;
            r
        },
        &None => panic!(),
    }
}

pub fn main() {
    let x = Some(5);
    foo(&&x);
}


