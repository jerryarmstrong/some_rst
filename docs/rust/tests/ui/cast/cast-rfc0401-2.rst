tests/ui/cast/cast-rfc0401-2.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // RFC 401 test extracted into distinct file. This is because some the
// change to suppress "derived" errors wound up suppressing this error
// message, since the fallback for `3` doesn't occur.

fn main() {
    let _ = 3 as bool;
    //~^ ERROR cannot cast as `bool`
}


