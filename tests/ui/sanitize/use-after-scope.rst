tests/ui/sanitize/use-after-scope.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-sanitizer-support
// needs-sanitizer-address
//
// compile-flags: -Zsanitizer=address
// run-fail
// error-pattern: ERROR: AddressSanitizer: stack-use-after-scope

static mut P: *mut usize = std::ptr::null_mut();

fn main() {
    unsafe {
        {
            let mut x = 0;
            P = &mut x;
        }
        std::ptr::write_volatile(P, 123);
    }
}


