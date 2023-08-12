tests/ui/consts/const_unsafe_unreachable_ub.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: evaluation of constant value failed

const unsafe fn foo(x: bool) -> bool {
    match x {
        true => true,
        false => std::hint::unreachable_unchecked(),
    }
}

const BAR: bool = unsafe { foo(false) };

fn main() {
    assert_eq!(BAR, true);
}


