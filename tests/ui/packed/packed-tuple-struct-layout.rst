tests/ui/packed/packed-tuple-struct-layout.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::mem;

#[repr(packed)]
#[allow(unused_tuple_struct_fields)]
struct S4(u8,[u8; 3]);

#[repr(packed)]
#[allow(unused_tuple_struct_fields)]
struct S5(u8,u32);

pub fn main() {
    unsafe {
        let s4 = S4(1, [2,3,4]);
        let transd : [u8; 4] = mem::transmute(s4);
        assert_eq!(transd, [1, 2, 3, 4]);

        let s5 = S5(1, 0xff_00_00_ff);
        let transd : [u8; 5] = mem::transmute(s5);
        // Don't worry about endianness, the u32 is palindromic.
        assert_eq!(transd, [1, 0xff, 0, 0, 0xff]);
    }
}


