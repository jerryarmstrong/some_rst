src/tools/miri/tests/fail/reading_half_a_pointer.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

// We use packed structs to get around alignment restrictions
#[repr(packed)]
struct Data {
    pad: u8,
    ptr: &'static i32,
}

// But we need to guarantee some alignment
struct Wrapper {
    align: u64,
    data: Data,
}

static G: i32 = 0;

fn main() {
    let mut w = Wrapper { align: 0, data: Data { pad: 0, ptr: &G } };

    // Get a pointer to the beginning of the Data struct (one u8 byte, then the pointer bytes).
    // Thanks to the wrapper, we know this is aligned-enough to perform a load at ptr size.
    // We load at pointer type, so having a relocation is ok -- but here, the relocation
    // starts 1 byte to the right, so using it would actually be wrong!
    let d_alias = &mut w.data as *mut _ as *mut *const u8;
    unsafe {
        let x = *d_alias;
        let _val = *x; //~ERROR: is a dangling pointer (it has no provenance)
    }
}


