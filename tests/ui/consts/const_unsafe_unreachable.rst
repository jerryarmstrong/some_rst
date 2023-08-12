tests/ui/consts/const_unsafe_unreachable.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

const unsafe fn foo(x: bool) -> bool {
    match x {
        true => true,
        false => std::hint::unreachable_unchecked(),
    }
}

const BAR: bool = unsafe { foo(true) };

fn main() {
    assert_eq!(BAR, true);
}


