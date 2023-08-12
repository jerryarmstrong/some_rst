tests/ui/consts/large_const_alloc.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-64bit
// on 32bit and 16bit platforms it is plausible that the maximum allocation size will succeed

const FOO: () = {
    // 128 TiB, unlikely anyone has that much RAM
    let x = [0_u8; (1 << 47) - 1];
    //~^ ERROR evaluation of constant value failed
};

static FOO2: () = {
    let x = [0_u8; (1 << 47) - 1];
    //~^ ERROR could not evaluate static initializer
};

fn main() {
    let _ = FOO;
    let _ = FOO2;
}


