tests/ui/borrowck/borrowck-union-uninitialized.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    a: u8,
}

union U {
    a: u8,
}

fn main() {
    unsafe {
        let mut s: S;
        let mut u: U;
        s.a = 0; //~ ERROR E0381
        u.a = 0; //~ ERROR E0381
        let sa = s.a;
        let ua = u.a;
    }
}


