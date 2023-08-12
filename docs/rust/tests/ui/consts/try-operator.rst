tests/ui/consts/try-operator.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(try_trait_v2)]
#![feature(const_trait_impl)]
#![feature(const_try)]
#![feature(const_convert)]

fn main() {
    const fn result() -> Result<bool, ()> {
        Err(())?;
        Ok(true)
    }

    const FOO: Result<bool, ()> = result();
    assert_eq!(Err(()), FOO);

    const fn option() -> Option<()> {
        None?;
        Some(())
    }
    const BAR: Option<()> = option();
    assert_eq!(None, BAR);
}


