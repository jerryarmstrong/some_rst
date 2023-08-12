tests/ui/macro_backtrace/auxiliary/ping.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the macro backtrace facility works (supporting file)

// a non-local macro
#[macro_export]
macro_rules! ping {
    () => {
        pong!();
    }
}

#[macro_export]
macro_rules! deep {
    () => {
        foo!();
    }
}

#[macro_export]
macro_rules! foo {
    () => {
        bar!();
    }
}

#[macro_export]
macro_rules! bar {
    () => {
        ping!();
    }
}


