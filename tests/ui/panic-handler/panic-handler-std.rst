tests/ui/panic-handler/panic-handler-std.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test "loaded from .*libstd-.*.rlib" -> "loaded from SYSROOT/libstd-*.rlib"
// error-pattern: found duplicate lang item `panic_impl`


use std::panic::PanicInfo;

#[panic_handler]
fn panic(info: PanicInfo) -> ! {
    loop {}
}

fn main() {}


