tests/ui/consts/const-eval/promoted_const_fn_fail_deny_const_err.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(C)]
union Bar {
    a: &'static u8,
    b: usize,
}

const fn bar() -> u8 {
    unsafe {
        // This will error as long as this test is run on a system whose
        // pointers need more than 8 bits.
        Bar { a: &42 }.b as u8
    }
}

fn main() {
    // This will compile, but then hard-abort at runtime.
    // FIXME(oli-obk): this should instead panic (not hard-abort) at runtime.
    let x: &'static u8 = &(bar() + 1);
    //~^ ERROR temporary value dropped while borrowed
    let y = *x;
    unreachable!();
}


