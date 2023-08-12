src/tools/miri/tests/fail/validity/invalid_char.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    assert!(std::char::from_u32(-1_i32 as u32).is_none());
    let _val = match unsafe { std::mem::transmute::<i32, char>(-1) } {
        //~^ ERROR: encountered 0xffffffff, but expected a valid unicode scalar value
        'a' => true,
        'b' => false,
        _ => true,
    };
}


