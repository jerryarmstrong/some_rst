src/tools/rustfmt/tests/source/else-if-brace-style-always-next-line.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-control_brace_style: AlwaysNextLine

fn main() {
    if false
    {
        ();
        ();
    }

    if false // lone if comment
    {
        ();
        ();
    }


    let a =
        if 0 > 1 {
            unreachable!()
        }
        else
        {
            0x0
        };


    if true
    {
        ();
    } else if false {
        ();
        ();
    }
    else {
        ();
        ();
        ();
    }

    if true // else-if-chain if comment
    {
        ();
    }
    else if false // else-if-chain else-if comment
    {
        ();
        ();
    } else // else-if-chain else comment
    {
        ();
        ();
        ();
    }
}


