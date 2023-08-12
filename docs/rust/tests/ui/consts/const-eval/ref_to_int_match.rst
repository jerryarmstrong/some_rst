tests/ui/consts/const-eval/ref_to_int_match.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // stderr-per-bitwidth

fn main() {
    let n: Int = 40;
    match n {
        0..=10 => {},
        10..=BAR => {}, //~ ERROR could not evaluate constant pattern
                        //~| ERROR could not evaluate constant pattern
        _ => {},
    }
}

#[repr(C)]
union Foo {
    f: Int,
    r: &'static u32,
}

#[cfg(target_pointer_width="64")]
type Int = u64;

#[cfg(target_pointer_width="32")]
type Int = u32;

const BAR: Int = unsafe { Foo { r: &42 }.f };
//~^ ERROR constant


