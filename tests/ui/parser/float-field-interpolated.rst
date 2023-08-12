tests/ui/parser/float-field-interpolated.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S(u8, (u8, u8));

macro_rules! generate_field_accesses {
    ($a:tt, $b:literal, $c:expr) => {
        let s = S(0, (0, 0));

        s.$a; // OK
        { s.$b; } //~ ERROR unexpected token: `1.1`
                  //~| ERROR expected one of `.`, `;`, `?`, `}`, or an operator, found `1.1`
        { s.$c; } //~ ERROR unexpected token: `1.1`
                  //~| ERROR expected one of `.`, `;`, `?`, `}`, or an operator, found `1.1`
    };
}

fn main() {
    generate_field_accesses!(1.1, 1.1, 1.1);
}


