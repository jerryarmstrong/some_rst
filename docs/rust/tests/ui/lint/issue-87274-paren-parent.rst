tests/ui/lint/issue-87274-paren-parent.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Tests that we properly lint at 'paren' expressions

fn foo() -> Result<(), String>  {
    (try!(Ok::<u8, String>(1))); //~ WARN use of deprecated macro `try`
    Ok(())
}

fn main() {}


