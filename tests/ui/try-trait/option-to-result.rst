tests/ui/try-trait/option-to-result.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main(){ }

fn test_result() -> Result<(),()> {
    let a:Option<()> = Some(());
    a?;//~ ERROR the `?` operator can only be used
    Ok(())
}

fn test_option() -> Option<i32>{
    let a:Result<i32, i32> = Ok(5);
    a?;//~ ERROR the `?` operator can only be used
    Some(5)
}


