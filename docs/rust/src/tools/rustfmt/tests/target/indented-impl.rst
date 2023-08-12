src/tools/rustfmt/tests/target/indented-impl.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-brace_style: AlwaysNextLine
mod x
{
    struct X(i8);

    impl Y for X
    {
        fn y(self) -> ()
        {
            println!("ok");
        }
    }
}


