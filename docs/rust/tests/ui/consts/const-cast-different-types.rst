tests/ui/consts/const-cast-different-types.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const a: &str = "foo";
const b: *const u8 = a as *const u8; //~ ERROR casting
const c: *const u8 = &a as *const u8; //~ ERROR casting

fn main() {
}


